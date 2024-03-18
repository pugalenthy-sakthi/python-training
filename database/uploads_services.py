from config import db
from common import response_strings,response_functions
from models.models import Uploads


def save_upload(uploads:Uploads):
    try:
        
        db.session.add(uploads)
        db.session.commit()
        
    except Exception as e:
        # print(e)
        return response_functions.server_error_sender(None,response_strings.server_error_message)