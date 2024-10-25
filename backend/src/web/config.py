from os import environ
from dotenv import load_dotenv
import os

load_dotenv()  

class Config(object):
    """Base configuration."""
    SECRET_KEY = "secret"
    DEBUG = True
    TESTING = False
    SCHEDULER_API_ENABLED = True
    JWT_SECRET_KEY = "secret_key"
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_ACCESS_COOKIE_NAME = "access_token_cookie"


class DevelopmentConfig(Config):
    """Development configuration."""

    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    DB_NAME = os.getenv('DB_NAME')
    DB_PORT = os.getenv('DB_PORT', 3306)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

config = DevelopmentConfig
