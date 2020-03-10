from app import app
from app.controllers import userController

@app.route('/users')
def users():
    return userController.index()