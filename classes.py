from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from data import offers, orders, users

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["JSON_AS_ASCII"] = False
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(150))
    age = db.Column(db.Integer)
    email = db.Column(db.String(300), unique=True)
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100), unique=True)

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class Orders(db.Model):
    __tablename__ = "Orders"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(500))
    start_date = db.Column(db.String(20))
    end_date = db.Column(db.String(20))
    address = db.Column(db.String(20))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("Orders.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("Users.id"))

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class Offers(db.Model):
    __tablename__ = "Offers"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("Orders.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("Users.id"))

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


with app.app_context():
    db.drop_all()
    db.create_all()

    for user in users:
        user_new = Users(id=user["id"],
                         first_name=user["first_name"],
                         last_name=user["last_name"],
                         age=user["age"],
                         email=user["email"],
                         role=user["role"],
                         phone=user["phone"]
                         )

        db.session.add(user_new)
        db.session.commit()

    for order in orders:
        order_new = Orders(id=order["id"], name=order["name"],
                           description=order["description"],
                           start_date=order["start_date"],
                           end_date=order["end_date"],
                           address=order["address"],
                           price=order["price"],
                           customer_id=order["customer_id"],
                           executor_id=order["executor_id"]
                           )

        db.session.add(order_new)
        db.session.commit()

    for offer in offers:
        offer_new = Offers(id=offer["id"],
                           order_id=offer["order_id"],
                           executor_id=offer["executor_id"])
        db.session.add(offer_new)
        db.session.commit()
