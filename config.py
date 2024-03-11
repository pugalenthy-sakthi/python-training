from datetime import timedelta
import os
import dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
dotenv.load_dotenv()
from flask_jwt_extended import JWTManager
from flask_apscheduler import APScheduler
from flask_mail import Mail


class config:
    
    PORT = os.getenv('PORT')
    SQLALCHEMY_DATABASE_URI = os.getenv('MYSQL_DB_URL')
    JWT_SECRET_KEY = os.getenv('APP_JWT_SECRET')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES'))
    
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
mail = Mail()
scheduler = APScheduler()