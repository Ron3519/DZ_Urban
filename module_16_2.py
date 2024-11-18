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
async def user(user_id : int = Path(ge=1, le=100, description= "Enter User ID",examples="15" )) -> dict:
    return {"message":f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
async def user_info(username : str = Path(min_length=5, max_length=20, description="Enter username", examples="Frodo"),
                    age : int = Path(ge=18, le = 120, description="Enter age", examples="101")) -> dict:
    return {"message":f"Имя: {username}, Возраст {age}"}

