import dotenv
import os

dotenv.load_dotenv()

class Config:
    port = os.getenv('FLASK_PORT')
    host = os.getenv('FLASK_MYSQL_HOST')
    user = os.getenv('FLASK_MYSQL_USER')
    password = os.getenv('FLASK_MYSQL_PASSWORD')
    database = os.getenv('FLASK_MYSQL_DB')