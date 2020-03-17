from app import db
from datetime import datetime
from app.models.order import Orders


class OrderStuff(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    stuffName = db.Column(db.String(250), nullable=False)
    count = db.Column(db.Integer, nullable=False)
    total = db.Column(db.BigInteger, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    orderId = db.Column(db.BigInteger, db.ForeignKey(Orders.id))

    def __repr__(self):
        return '<OrderStuff {}>'.format(self.stuffName)
