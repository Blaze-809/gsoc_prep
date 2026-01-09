from fastapi import FastAPI,HTTPException, status
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

users =[]
user_id_counter=1

class User(BaseModel):
    name:str
    email:str
    
class Update_User(BaseModel):
    name:Optional[str]=None
    email:Optional[str]=None
    
@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    global user_id_counter

    new_user = {
        "id": user_id_counter,
        "name": user.name,
        "email": user.email
    }

    users.append(new_user)
    user_id_counter += 1

    return new_user

@app.patch("/users/{user_id}", status_code=status.HTTP_200_OK)
def patch_user(user_id:int, patch_user:Update_User):
    if(patch_user.name is None and patch_user.email is None):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Atleast one field is required"
        )
    for user in users:
        if user["id"]==user_id:
            if patch_user.name is not None:
                user["name"]=patch_user.name
            if patch_user.email is not None:
                user["email"]=patch_user.email
            return user
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )


@app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id:int , update_user: User):
    for user in users:
        if user["id"]==user_id:
            user["name"]=update_user.name
            user["email"]=update_user.email
            return user
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )


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