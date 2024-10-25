import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    USER = os.getenv('MYSQLUSER')  # Asegúrate de que este nombre coincida
    PASSWORD = os.getenv('MYSQLPASSWORD')  # Lo mismo aquí
    HOST = os.getenv('MYSQLHOST')  # Asegúrate de que esto esté configurado correctamente
    DB_NAME = os.getenv('MYSQL_DATABASE')  # Cambia esto si es necesario
    
    # Define la cadena de conexión usando las variables de Railway
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{os.getenv("MYSQLPORT")}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    