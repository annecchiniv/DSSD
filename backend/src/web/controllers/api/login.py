from flask import jsonify, Blueprint, abort, request
from src.core.services import user as u
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies
from flask_jwt_extended import unset_jwt_cookies, jwt_required
from flask_jwt_extended import get_jwt_identity

auth_api = Blueprint("auth", __name__, url_prefix="/auth")

@auth_api.post('/login_jwt')
def login_jwt():
    data = request.get_json()
    user = u.authenticate_user(data)
    if user:
        access_token = create_access_token(identity=user.id)
        response = jsonify()
        set_access_cookies(response, access_token)
        return response, 201
    else:
        return jsonify(message='Usuario o contraseña incorrectos'), 401

@auth_api.get('/user_jwt')
@jwt_required()
def user_jwt():
    id_current_user = get_jwt_identity()
    user = u.get(id_current_user)
    response = jsonify(user.name)
    return response, 200

@auth_api.get('/logout_jwt')
@jwt_required()
def logout_jwt():
    response = jsonify()
    unset_jwt_cookies(response)
    return response, 200