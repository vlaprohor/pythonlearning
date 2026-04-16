from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}"}

@app.get("/sum")
def calculate(a: int, b: int):
    return {"result": a + b}