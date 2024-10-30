from fastapi import FastAPI, HTTPException

app = FastAPI()

# Словарь для хранения пользователей
users = {'1': 'Имя: Example, возраст: 18'}

# GET запрос: возвращает всех пользователей
@app.get('/users')
async def get_users():
    return users

# POST запрос: добавляет нового пользователя
@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int):
    # Находим максимальный ключ
    new_id = str(max(int(key) for key in users.keys()) + 1)
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return f"User {new_id} is registered."

# PUT запрос: обновляет информацию о пользователе
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is registered."

# DELETE запрос: удаляет пользователя
@app.delete('/user/{user_id}')
async def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return f"User {user_id} has been deleted."
