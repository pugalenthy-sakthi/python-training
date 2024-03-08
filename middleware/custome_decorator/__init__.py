from functools import wraps
from flask import request
from flask_jwt_extended import decode_token

from database import user_services

def token_required(func):
    @wraps(func)
    def handle_function(*args,**kwargs):
        if 'Authorization' not in request.headers:
            return "FORBIDDEN",403
        else:
            token = request.headers['Authorization']
            try:
                data = decode_token(token)
                activity = user_services.get_user_activity(token)
                if activity ==None or activity.logout_at != None :
                    return 'FORBIDDEN',403
                request.environ['HTTP_USER_DATA'] = data['sub']
                return func(*args,**kwargs)
            except Exception as e:
                return "FORBIDDEN",403
        
    return handle_function
        