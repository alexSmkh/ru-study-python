from flask import Flask, request
from http import HTTPStatus


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    STORE = {}

    @staticmethod
    def configure_routes(app: Flask) -> None:
        @app.post('/user')
        def create_user():
            name = request.json.get('name')

            if name is None:
                return (
                    {'errors': {'name': 'This field is required'}},
                    HTTPStatus.UNPROCESSABLE_ENTITY,
                )

            FlaskExercise.STORE[name] = {}
            return {'data': f'User {name} is created!'}, HTTPStatus.CREATED

        @app.get('/user/<name>')
        def get_user(name):
            user = FlaskExercise.STORE.get(name)

            if user is None:
                return (
                    {'errors': {'name': 'User with this name does not exist'}},
                    HTTPStatus.NO_CONTENT,
                )

            return {'data': f'My name is {name}'}, HTTPStatus.OK

        @app.patch('/user/<name>')
        def update_user_name(name):
            user = FlaskExercise.STORE.get(name)

            if user is None:
                return (
                    {'errors': {'name': 'User with this name does not exist'}},
                    HTTPStatus.UNPROCESSABLE_ENTITY,
                )

            new_name = request.json.get('name')

            if new_name is None:
                return (
                    {'errors': {'new_name': 'This field is required'}},
                    HTTPStatus.UNPROCESSABLE_ENTITY,
                )

            FlaskExercise.STORE[new_name] = user
            del FlaskExercise.STORE[name]

            return {'data': f'My name is {new_name}'}, HTTPStatus.OK
