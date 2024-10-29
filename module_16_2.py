from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return {'message': 'Главная страница'}

@app.get('/user/admin')
async def admin() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def id_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', examples=47)]) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user/{username}/{age}')
async def info(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', examples=35)]) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}