from fastapi import FastAPI
app = FastAPI()


@app.get("/user/admin")
async def admin():
    return {'message':'Вы вошли как администратор'}

@app.get("/user/{user_id}")
async def user(user_id : str) -> dict:
    return {"message":f"Вы вошли как пользователь № {user_id}"}

@app.get("/")
async def title():
    return {"message":'Главная страница'}