from datetime import timedelta
import os
import dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
dotenv.load_dotenv()
from flask_jwt_extended import JWTManager
from flask_apscheduler import APScheduler
from flask_mail import Mail
from flask_caching import Cache
import redis


class config:
    
    PORT = os.getenv('PORT')
    SQLALCHEMY_DATABASE_URI = os.getenv('MYSQL_DB_URL')
    JWT_SECRET_KEY = os.getenv('APP_JWT_SECRET')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES'))
    MAIL_USERNAME = os.getenv('EMAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    MAIL_SERVER = os.getenv('EMAIL_PROVIDER')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_PORT = os.getenv('EMAIL_PORT')
    CACHE_TYPE = os.getenv('FLASK_CACHE_TYPE')
    CACHE_REDIS_HOST = os.getenv('FLASK_CACHE_REDIS_HOST')
    CACHE_REDIS_PORT = os.getenv('FLASK_CACHE_REDIS_PORT')
    CACHE_REDIS_DB = os.getenv('FLASK_CACHE_REDIS_DB')
    
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
mail = Mail()
scheduler = APScheduler()
cache = Cache()
redis_client = redis.Redis(host=config.CACHE_REDIS_HOST,port=config.CACHE_REDIS_PORT,db=config.CACHE_REDIS_DB,password='password')