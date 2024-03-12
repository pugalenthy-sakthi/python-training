from authlib.integrations.flask_client import OAuth
import os
import dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_apscheduler import APScheduler
from flask_mail import Mail
from flask_caching import Cache
import redis
import pymongo
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




dotenv.load_dotenv()


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
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    APP_SECRET_KEY = os.getenv('SECRET_KEY')
    MONGODB_URI = os.getenv('MONGODB_URI')
    MONGODB_DB = os.getenv('MONGODB_DB')
    
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
mail = Mail()
scheduler = APScheduler()
cache = Cache()
redis_client = redis.Redis(host=config.CACHE_REDIS_HOST,port=config.CACHE_REDIS_PORT,db=config.CACHE_REDIS_DB)
oauth = OAuth()
myclient = pymongo.MongoClient(config.MONGODB_URI)
mdb = myclient[config.MONGODB_DB]
read_slave = create_engine(config.SQLALCHEMY_DATABASE_URI)
read_head = sessionmaker(bind=read_slave)