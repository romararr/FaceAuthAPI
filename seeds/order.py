# from app.models.order import Orders
# from app.models.orderStuff import OrderStuff as Stuff
# import string
# from flask_seeder import Seeder, Faker, generator


# # SQLAlchemy db model
# class User(Users):
#     def __init__(self, name=None, email=None, password=None):
#         self.name = name
#         self.email = email
#         self.password = password

#     def __str__(self):
#         return "Name=%s, Email=%s, Password=%s" % (self.name, self.email, self.password)


# # main order db model
# class Order(Orders):
#     def __init__(self, orderId=None, userId=None):
#         self.orderId = orderId
#         self.userId = userId

#     def __str__(self):
#         return "OrderId=%s, UserId=%s" % (self.orderId, self.userId)


# class OrderStuff(Stuff):
#     def __init__(self, ):
        


# class UserSeeder(Seeder):
#     # run() will be called by Flask-Seeder
#     def run(self):
#         # Create a new Faker and tell it how to create User objects
#         name = generator.Name()
#         faker = Faker(
#             cls=User,
#             init={
#                 "name": name,
#                 "email": ''.join(random.choice(string.ascii_letters) for i in range(10)) + "@gmail.com",
#                 "password": "secret"
#             }
#         )

#         # Create 1 user
#         for user in faker.create(1):
#             print("Adding user: %s" % user)
#             self.db.session.add(user)
