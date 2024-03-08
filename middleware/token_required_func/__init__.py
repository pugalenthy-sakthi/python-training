from flask import request
from flask_jwt_extended import decode_token
from database import user_db_services

def token_reqiured(*args,**kwargs):
        if 'Authorization' not in request.headers:
            return "FORBIDDEN",403
        else:
            token = request.headers['Authorization']
            try:
                data = decode_token(token)
                activity = user_db_services.get_user_activity(token)
                if activity ==None or activity.logout_at != None :
                    return 'FORBIDDEN',403
                request.environ['HTTP_USER_DATA'] = data['sub']
            except Exception as e:
                print(e)
                return "FORBIDDEN",403