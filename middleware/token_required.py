from flask import request
from flask_jwt_extended import decode_token
from database import user_services
from exception.ForbiddenError import ForbiddenError
from common import response_strings,response_functions


open_paths = [
    '/auth/signup/',
    '/auth/login/'
]

def token_reqiured(*args,**kwargs):
    if request.path in open_paths:
        pass
    else:
        if 'Authorization' not in request.headers:
            raise ForbiddenError(response_strings.invalid_credentials)
        else:
            token = request.headers['Authorization']
            try:
                data = decode_token(token)
                session = user_services.get_activity_by_session(data['session_id'])
                if session == None or session.logout_at !=None:
                    return response_functions.forbidden_response_sender([],response_strings.invalid_credentials)
                request.environ['HTTP_USER_DATA'] = data['sub']
                request.environ['HTTP_SESSION_ID'] = data['session_id']
            except Exception as e:
                raise ForbiddenError(response_strings.invalid_credentials)