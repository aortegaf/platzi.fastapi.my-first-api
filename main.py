from fastapi import FastAPI

app = FastAPI()
app.title = "My FastAPI"
app.version = "1.0"

@app.get('/')
def message():
    return "Hello World!"