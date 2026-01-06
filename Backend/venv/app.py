from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return{"status":"ok"}

@app.get("/health")
def health():
    return{"health":"ok"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message":f"Hello,{name}!"}