from flask import Blueprint, jsonify, request
from models.user import User
from models.database import db

users_routes = Blueprint('user_routes', __name__)

"""Users routes"""
@users_routes.route('/new_user', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']
    usr = User(name=name, email=email, password=password)
    db.session.add(usr)
    db.session.commit()
    return jsonify({'message': 'User created succesfully'})

@users_routes.route('/get_users')   
def get_users():
    users =  User.query.all()
    return jsonify([user.to_dict() for user in users])


@users_routes.route('/update_user/<string:id>', methods=['PUT'])
def update_user(id):
    us = User.query.get(id)
    if not us:
        return jsonify({'error': 'User not found' }), 404
    data = request.get_json()
    us.name = data.get('name', us.name)
    us.email = data.get('email', us.email)
    us.password = data.get('password', us.password)
    db.session.commit()
    return jsonify(us.to_dict())

@users_routes.route('/delete_user/<string:id>', methods=['DELETE'])
def del_need(id):
    u = User.query.get(id)
    if u:
        db.session. delete(u)
        db.session.commit()
        return jsonify({'message': f'User belonging to {id} deleted successfully'})
    else:
        return jsonify({'error': f'User with {id} not found'}), 404