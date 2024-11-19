from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()
users = []

class User(BaseModel):
    id : int
    username : str
    age : int

@app.get("/users")
async def all_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}")
async def new_user(username : User,age : User):
    User.id = len(users) + 1
    users.append(User)
    return User

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id : int, username : str, age : int):
    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id : int):
    try:
        edit_user = users[user_id]
        users[user_id].pop()
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")




