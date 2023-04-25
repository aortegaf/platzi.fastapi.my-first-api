from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "My FastAPI"
app.version = "1.0"

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





