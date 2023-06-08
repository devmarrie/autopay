from flask import Blueprint, jsonify, request
from models.need import Need
from models.database import db

need_routes = Blueprint('need_routes', __name__)

"""Needs routes"""
@need_routes.route('/add_need', methods=['POST'])
def add_need():
    data = request.get_json()
    need = data['need']
    amount = data['amount']
    duedate = data['duedate']
    reminderdate = data['reminderdate']
    ned = Need(need=need, amount=amount, duedate=duedate, reminderdate=reminderdate)
    db.session.add(ned)
    db.session.commit()
    return jsonify({'message': 'New need created successfully'})


@need_routes.route('/get_needs')
def get_needs():
    needs =  Need.query.all()
    return jsonify([n.to_dict() for n in needs])