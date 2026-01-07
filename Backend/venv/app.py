from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

users =[]

class User(BaseModel):
    name:str
    email:str

@app.get("/")
def root():
    return{"status":"ok"}

@app.get("/health")
def health():
    return{"health":"ok"}

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return{"message":"User added successfully","total_users": len(users)}
    
@app.get("/users")
def get_users():
    return users

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message":f"Hello,{name}!"}