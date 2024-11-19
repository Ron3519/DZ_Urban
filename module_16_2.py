from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
@app.get("/")
async def title():
    return {"message":"Главная страница"}

@app.get("/user/admin")
async def admin():
    return {"message":"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user(user_id : int = Path(ge=0, le=100, description= "Enter User ID",example="15" )) -> dict:
    return {"message":f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
async def user_info(username : str = Path(min_length=5, max_length=20, description="Enter username", example="Frodo"),
                    age : int = Path(ge=17, le = 120, description="Enter age", example="36")) -> dict:
    return {"message":f"Имя: {username}, Возраст {age}"}

