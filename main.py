from fastapi import FastAPI, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import List
from jwt_manager import create_token

app = FastAPI()

#config
app.title = "My FastAPI"
app.version = "1.0"


#models

class User(BaseModel):
    email: str
    password: str
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


#data
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


#main
@app.get('/', tags=["home"])
def message():
    return HTMLResponse('<h1>This is my first API with FastAPI</h1>')

@app.post('/login', tags=["auth"])
def login(user: User):
    return user

@app.get('/movies', tags=["movies"], response_model=List[Movie])
def get_movies() -> List[Movie]:
    return JSONResponse(content=movies)

@app.get('/movies/', tags=["movies"], response_model=List[Movie])
def get_movies_by_year(year: int = Query(ge=2000)) -> List[Movie]:
    data = []
    for m in movies:
        if(m["year"] == year):
            data.append(m)
    return JSONResponse(content=data)

@app.get('/movies/{id}', tags=["movies"], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=10)) -> Movie:
    data = []
    for m in movies:
        if(m["id"] == id):
            data.append(m)
    return JSONResponse(content=data)
        
@app.post('/movies', tags=["movies"], response_model=dict)
def add_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(content={"message": "Movie succesfully created!"})

@app.put('/movies', tags=["movies"], response_model=dict)
def update_movie(id: int, movie: Movie) -> dict:
    for m in movies:
        if(m["id"] == id):
            m["title"] = movie.title
            m["year"] = movie.year
    return JSONResponse(content={"message": "Movie succesfully updated!"})

@app.delete('/movies', tags=["movies"], response_model=dict)
def delete_movie(id: int) -> dict:
    for m in movies:
        if(m["id"] == id):
            movies.remove(m)
    return JSONResponse(content={"message": "Movie succesfully deleted!"})





