from app import response, db
from app.models.order import Orders as Order
from app.models.orderStuff import OrderStuff as Stuff
from app.controllers import UserController
from flask import request, jsonify


def index():
    try:
        userId = request.args.get('userId')

        if not userId:
            order = Order.query.all()
        else:
            order = Order.query.filter_by(userId=userId).all()

        data = transform(order)

        return response.ok(data, 'Your orders here')
    except Exception as e:
        print(e)


# create order
def store():
    try:
        orderId = request.json['orderId']
        userId = request.json['userId']

        order = Order(userId=userId, orderId=orderId)
        db.session.add(order)
        db.session.commit()

        return response.ok('', 'Your order has been added')
    except Exception as e:
        print(e)


# update order
def update(id):
    try:
        # init changes value
        orderId = request.json['orderId']

        # process updating
        order = Order.query.filter_by(orderId=id).first()
        if not order:
            return response.badRequest('', 'Invalid order')
        order.orderId = orderId

        db.session.commit()

        return response.ok(order, 'Update data successfully')

    except Exception as e:
        print(e)


# delete order
def delete(id):
    try:
        order = Order.query.filter_by(orderId=id).first()
        if not order:
            return response.badRequest('', 'Invalid order')

        db.session.delete(order)
        db.session.commit()

        return response.ok('', 'Order deleted successcfully')
    except Exception as e:
        print(e)


# === Order Items ===
# index
def itemIndex():
    try:
        id = request.args.get('orderId')
        item = Stuff.query.filter_by(orderId=id).all()
        data = transform(item)
        return response.ok(data, 'Your order items here')
    except Exception as e:
        print(e)


# add new stuff
def itemStore():
    try:
        stuffName = request.json['stuffName']
        count = request.json['count']
        price = request.json['price']
        total = count * price
        orderId = request.json['orderId']

        stuff = Stuff(stuffName=stuffName, count=count,
                      total=total, orderId=orderId)
        db.session.add(stuff)
        db.session.commit()

        return response.ok(stuff, 'Stuff added')
    except Exception as e:
        print(e)


# update order stuff
def itemUpdate(id):
    try:
        stuffName = request.json['stuffName']
        count = request.json['count']

        # process updating
        stuff = Stuff.query.filter_by(id=id).first()
        if not stuff:
            return response.badRequest('', 'Invalid order')
        stuff.count = count
        stuff.total = count * stuff.price
        stuff.stuffName = stuffName

        db.session.commit()

    except Exception as e:
        print(e)


# delete stuff
def itemDelete(id):
    try:
        stuff = Stuff.query.filter_by(id=id).first()
        if not stuff:
            return response.badRequest('', 'Stuff not found')

        db.session.remove(stuff)
        db.session.commit()

        return response.ok('', 'Stuff deleted successfully')
    except Exception as e:
        print(e)


def transform(data):
    array = []
    for i in data:
        array.append(singleTransform(i))
    return array


def singleTransform(data):
    data = {
        'id': data.id,
        'userId': data.userId,
        'orderId': data.orderId,
        'created_at': data.created_at,
        'updated_at': data.updated_at,
        'user': UserController.singleTransfrom(data.users, withOrder=False)
    }
    return data
