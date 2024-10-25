from flask import request, jsonify
from werkzeug.security import check_password_hash
from src.core.models.usuario import User 
from flask_jwt_extended import create_access_token

def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Login failed"}), 401

def register():
    data = request.json
    return jsonify({"msg": "Usuario registrado"}), 201
