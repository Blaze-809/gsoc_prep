from fastapi import FastAPI,HTTPException, status
from pydantic import BaseModel

app=FastAPI()

users =[]
user_id_counter=1

class User(BaseModel):
    name:str
    email:str
    
@app.post("/users",status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    global user_id_counter
    
    new_user={
        "id":user_id_counter,
        "name":User.name,
        "email":User.email
    }
    
    users.append(new_user)
    user_id_counter+=1
    
    return new_user


@app.delete("/user/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id:int):
    for user in users:
        if user["id"]==user_id:
            users.remove(user)
            return{"message" : "User deleted successfully"}
        
    raise HTTPException(
        status_code=status_HTTP_404_NOT_FOUND,
        detail= "User not found"
    )

@app.get("/")
def root():
    return{"status":"ok"}

@app.get("/health")
def health():
    return{"health":"ok"}


    
@app.get("/users")
def get_users():
    return users

@app.get("/hello/{name}")
def say_hello(name: str):  
    return {"message":f"Hello,{name}!"}