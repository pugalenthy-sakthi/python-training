from flask import request
from flask_jwt_extended import decode_token

def token_reqiured(*args,**kwargs):
        if 'Authorization' not in request.headers:
            return "FORBIDDEN",403
        else:
            token = request.headers['Authorization']
            try:
                data = decode_token(token)
                request.environ['HTTP_USER_DATA'] = data['sub']
            except Exception as e:
                print(e)
                return "FORBIDDEN",403