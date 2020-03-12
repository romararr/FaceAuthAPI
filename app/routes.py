from app import app
from app.controllers import UserController
import flask


# route user
@app.route('/users')
def users():
    return UserController.index()


@app.route('/users/create', methods=['POST'])
def userCreate():
    return UserController.store()


@app.route('/users/<id>')
def userDetail(id):
    print(id)
    return UserController.user(id)


@app.route('/users/update/<id>', methods=['POST'])
def userUpdate(id):
    return UserController.update(id)


@app.route('/users/delete/<id>', methods=['POST'])
def userDelete(id):
    return UserController.delete(id)


@app.route('/login', methods=['POST'])
def login():
    return UserController.login()
