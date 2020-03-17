from app import app
from app.controllers import UserController, OrderController
import flask


# === USERS ===
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


# === Orders ===
@app.route('/orders')
def order():
    return OrderController.index()


@app.route('/orders/create', methods=['POST'])
def orderCreate():
    return OrderController.store()


@app.route('/orders/update/<id>', methods=['POST'])
def orderUpdate(id):
    return OrderController.update(id)


@app.route('/orders/delete/<id>', methods=['POST'])
def orderDelete(id):
    return OrderController.delete(id)


# === ORDER STUFF ===
@app.route('/stuff')
def stuff():
    return OrderController.itemIndex()


@app.route('/stuff/create')
def stuffCreate():
    return OrderController.itemStore()


@app.route('/stuff/update/<id>')
def stuffUpdate(id):
    return OrderController.itemUpdate(id)


@app.route('/stuff/delete/<id>')
def stuffDelete(id):
    return OrderController.itemDelete(id)
