import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

class Config:
    # Si Railway proporciona `DATABASE_URL`, úsalo; de lo contrario, usa las variables individuales.
    if os.getenv("DATABASE_URL"):
        SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL").replace("mysql://", "mysql+pymysql://")
    else:
        USER = os.getenv('MYSQLUSER')
        PASSWORD = os.getenv('MYSQLPASSWORD')
        HOST = os.getenv('MYSQLHOST')
        DB_NAME = os.getenv('MYSQL_DATABASE')
        MYSQLPORT = os.getenv("MYSQLPORT")
        SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{MYSQLPORT}/{DB_NAME}'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
