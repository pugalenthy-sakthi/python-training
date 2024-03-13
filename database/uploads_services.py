
from config import db
from exception import DataBaseError
from common import response_strings
from models.models import Uploads


def save_upload(uploads:Uploads):
    try:
        
        db.session.add(uploads)
        db.session.commit()
        
    except Exception as e:
        print(e)
        raise DataBaseError(response_strings.server_error_message)