from flask import Blueprint
from .auth import login, register

auth_blueprint = Blueprint('auth', __name__)

# Aquí puedes registrar tus rutas
auth_blueprint.add_url_rule('/login', view_func=login, methods=['POST'])
auth_blueprint.add_url_rule('/register', view_func=register, methods=['POST'])
