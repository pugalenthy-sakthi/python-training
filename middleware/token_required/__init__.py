from functools import wraps
from flask import request
from flask_jwt_extended import decode_token

def token_required(func):
    @wraps(func)
    def handle_function(*args,**kwargs):
        if 'Authorization' not in request.headers:
            return "FORBIDDEN",403
        else:
            token = request.headers['Authorization']
            try:
                data = decode_token(token)
                data = decode_token(token)
                request.environ['HTTP_USER_DATA'] = data['sub']
                return func(*args,**kwargs)
            except Exception as e:
                return "FORBIDDEN",403
        
    return handle_function
        