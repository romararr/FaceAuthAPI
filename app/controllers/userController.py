from app.models.user import Users
from app import response, app, db
from flask import request


# get all data
def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)


# get single user
def user(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], "Empty data")

        data = singleTransfrom(users)
        return response.ok(data, "Success Get User")
    except Exception as e:
        print(e)


# store new user
def store():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        users = Users(name=name, email=email)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.ok('', 'User added successfully')
    except Exception as e:
        print(e)


# update user data
def update(id):
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        user = Users.query.filter_by(id=id).first() # get user by id
        user.name = name
        user.email = email
        user.setPassword(password)

        db.session.commit()

        return response.ok('', 'Update user successfully')
    except Exception as e:
        print(e)


def delete(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'User not found')
        
        db.session.delete(user)
        db.session.commit()

        return response.ok('', 'User absolutely deleted')
    except Exception as e:
        print(e)

def transform(users):
    array = []
    for i in users:
        array.append(singleTransfrom(i))
    return array


def singleTransfrom(users):
    data = {
        'id': users.id,
        'name': users.name,
        'email': users.email
    }
    return data
