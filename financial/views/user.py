from flask import Blueprint, jsonify, request
from financial.models import User, users_schema
from financial import db

user = Blueprint('user', __name__, url_prefix='')


@user.route("/user", methods=['GET'])
def get():
    users = User.query.all()

    result = users_schema.dump(users)
    return jsonify(user=result.data)


@user.route('/user', methods=['POST'])
def create():
    name = request.json['name']
    username = request.json['username']
    password = request.json['password']

    user = User(
        name,
        username,
        password
    )
    db.session.add(user)
    db.session.commit()

    return user_schema.jsonify(user)
