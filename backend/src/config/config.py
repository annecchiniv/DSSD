import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    USER = os.getenv('DATABASE_USER')
    PASSWORD = os.getenv('DATABASE_PASSWORD')
    HOST = os.getenv('DATABASE_HOST')
    DB_NAME = os.getenv('DATABASE_NAME')
    
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@localhost/ecocycle-grupo13'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    