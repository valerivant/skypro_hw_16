import json
from flask import request, jsonify
from classes import Users, Orders, Offers, db, app


@app.route("/users")
def users():
    data = Users.query.all()
    output = [usr.to_dict() for usr in data]
    return jsonify(output)


@app.route("/user/<int:number>")
def user(number):
    data = Users.query.get(number)
    output = [data.to_dict()]
    return jsonify(output)


@app.route("/orders")
def orders():
    data = Orders.query.all()
    output = [usr.to_dict() for usr in data]
    return jsonify(output)


@app.route("/order/<int:number>")
def order(number):
    data = Users.query.get(number)
    output = [data.to_dict()]
    return jsonify(output)


@app.route("/offers")
def offers():
    data = Offers.query.all()
    output = [usr.to_dict() for usr in data]
    return jsonify(output)


@app.route("/offer/<int:number>")
def offer(number):
    data = Offers.query.get(number)
    output = [data.to_dict()]
    return jsonify(output)


# users

@app.post("/users")
def users_post():
    data_user = json.loads(request.data)
    output = Users(**data_user)
    db.session.add(output)
    db.session.commit()
    return 201


@app.put("/user/<uid>")
def user_put(uid):
    data_user = json.loads(request.data)
    output = Users.query.get(uid)

    output.first_name = data_user["first_name"]
    output.last_name = data_user["last_name"]
    output.role = data_user["role"]
    output.phone = data_user["phone"]
    output.email = data_user["email"]
    output.age = data_user["age"]

    db.session.add(output)
    db.session.commit()
    return "yessss", 200


@app.delete("/user/<uid>")
def user_delete(uid):
    user = Users.query.get(uid)
    db.session.delete(user)
    db.session.commit()
    return "yessss", 200


#  orders

@app.post("/orders")
def orders_post():
    data_user = json.loads(request.data)
    output = Orders(**data_user)
    db.session.add(output)
    db.session.commit()
    return "yessss", 201


@app.put("/order/<uid>")
def order_put(uid):
    data_user = json.loads(request.data)
    output = Orders.query.get(uid)

    output.name = data_user["name"]
    output.description = data_user["description"]
    output.start_date = data_user["start_date"]
    output.end_date = data_user["end_date"]
    output.address = data_user["address"]
    output.price = data_user["price"]
    output.customer_id = data_user["customer_id"]
    output.executor_id = data_user["executor_id"]

    db.session.add(output)
    db.session.commit()
    return 200


@app.delete("/order/<uid>")
def order_delete(uid):
    user = Orders.query.get(uid)
    db.session.delete(user)
    db.session.commit()
    return 200


#   offers

@app.post("/offers")
def offers_post():
    data_user = json.loads(request.data)
    output = Offers(**data_user)
    db.session.add(output)
    db.session.commit()
    return 201


@app.put("/offer/<uid>")
def offer_put(uid):
    data_user = json.loads(request.data)
    output = Offers.query.get(uid)

    output.order_id = data_user["order_id"]
    output.executor_id = data_user["executor_id"]

    db.session.add(output)
    db.session.commit()
    return 201


@app.delete("/offer/<uid>")
def offer_delete(uid):
    user = Offers.query.get(uid)
    db.session.delete(user)
    db.session.commit()
    return 200


if __name__ == "__main__":
    app.run()
