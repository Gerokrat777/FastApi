from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async  def welcome() -> dict:
    return {'message': "Главная страница"}

@app.get("/admin")
async def welcome() -> dict:
    return {'message': 'Вы вошли как АДМИНИСТРАТОР'}

@app.get('/id')
async def id_pagi(username: str = 'Ilya', age: int = 24) ->dict:
    return {'Информация о пользователе. Имя=': username, 'Возраст = ': age}

@app.get("/user/{user_id}")
async def news(user_id: str) -> dict:
    return {'message': f'Вывошли как пользователь, {user_id}'}