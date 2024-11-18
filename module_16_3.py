from fastapi import FastAPI, Path
from typing import Annotated
users = {'1': 'Имя: Example, возраст: 18'}
app = FastAPI()

@app.get("/users")
async def all_users():
    return users

@app.post("/users/{username}/{age}")
async def new_user(username : str,age : int):
    user_id = str(int(max(users,key=int))+1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/users/{user_id}/{username}/{age}")
async def update_user(user_id : int, username : str, age : int):
    users[int(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/users/{user_id}")
async def delete_user(user_id : str):
    users.pop(user_id)
    return f"The user {user_id} is deleted"