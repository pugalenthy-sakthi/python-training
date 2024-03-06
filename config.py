import dotenv
import os
from flask_sqlalchemy import SQLAlchemy
dotenv.load_dotenv()


class Config():
    PORT = os.getenv('FLASK_PORT')
    SQLALCHEMY_DATABASE_URI = os.getenv('FLASK_MYSQL_URL')

db = SQLAlchemy()