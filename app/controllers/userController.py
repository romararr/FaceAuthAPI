from app.models.user import Users
from app import response, app, db
from flask import request
from flask_jwt_extended import *
import datetime


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

        user = Users.query.filter_by(id=id).first()  # get user by id
        user.name = name
        user.email = email
        user.setPassword(password)

        db.session.commit()

        return response.ok('', 'Update user successfully')
    except Exception as e:
        print(e)


# delete user
def delete(id):
    try:
        user = Users.query.filter_by(id=id).first()  # get user by id
        if not user:
            return response.badRequest([], 'User not found')

        db.session.delete(user)
        db.session.commit()

        return response.ok('', 'User absolutely deleted')
    except Exception as e:
        print(e)


# user login
def login():
    try:
        email = request.json['email']
        password = request.json['password']

        user = Users.query.filter_by(email=email).first()
        # email valid check
        if not user:
            return response.badRequest([], 'User not found')

        # password valid check
        if not user.checkPassword(password):
            return response.badRequest([], 'Invalid password')

        data = singleTransfrom(user)

        exp = datetime.timedelta(days=1)
        exp_refresh = datetime.timedelta(days=3)
        access_token = create_access_token(data, fresh=True, expires_delta=exp)
        refresh_token = create_refresh_token(data, expires_delta=exp_refresh)

        return response.ok({
            "data": data,
            "token_access": access_token,
            "token_refresh": refresh_token
        }, 'Welcome to Isekai')

    except Exception as e:
        print(e)


# transform data to array
def transform(users):
    array = []
    for i in users:
        array.append(singleTransfrom(i))
    return array


# get single data
def singleTransfrom(users, withOrder=True):
    data = {
        'id': users.id,
        'name': users.name,
        'email': users.email
    }

    # if withOrder:
    #     orders = []
    #     for i in users.orders:
    #         orders.append({
    #             'id': i.id,
    #             'orderId': i.orderId,
    #         })
    #     data['orders'] = orders

    return data
