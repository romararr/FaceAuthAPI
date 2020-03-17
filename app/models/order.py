from app import db
from datetime import datetime
from app.models.user import Users


class Orders(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    orderId = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    userId = db.Column(db.BigInteger, db.ForeignKey(Users.id))

    # user relation
    users = db.relationship("Users", backref="userId")

    def __repr__(self):
        return '<Order {}>'.format(self.orderId)
