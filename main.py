from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

app = FastAPI()
app.title = "My FastAPI"
app.version = "1.0"

class Movie(BaseModel):
    id: int = Field(ge=1, le=10)
    title: str = Field(max_length=20)
    year: int = Field(ge=2000)

    class Config: 
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Movie Title",
                "year": 2000
            }
        }

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "year": 2009
    },
    {
        "id": 2,
        "title": "Avengers: Infinity War",
        "year": 2018
    }
]

@app.get('/', tags=["home"])
def message():
    return HTMLResponse('<h1>This is my first API with FastAPI</h1>')

@app.get('/movies', tags=["movies"])
def get_movies():
    return movies

@app.get('/movies/', tags=["movies"])
def get_movies_by_year(year: int):
    for m in movies:
        if(m["year"] == year):
            return m

@app.get('/movies/{id}', tags=["movies"])
def get_movie(id: int = Path(ge=1, le=10)):
    for m in movies:
        if(m["id"] == id):
            return m
        
@app.post('/movies', tags=["movies"])
def add_movie(movie: Movie):
    movies.append(movie)
    return movies

@app.put('/movies', tags=["movies"])
def update_movie(id: int, movie: Movie):
    for m in movies:
        if(m["id"] == id):
            m["title"] = movie.title
            m["year"] = movie.year
    return movies

@app.delete('/movies', tags=["movies"])
def delete_movie(id: int):
    for m in movies:
        if(m["id"] == id):
            movies.remove(m)
    return movies





