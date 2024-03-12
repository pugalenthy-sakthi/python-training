from flask import request
from flask_jwt_extended import decode_token
from database import user_services
from exception.ForbiddenError import ForbiddenError
from common import response_strings,response_functions
from util import caching

open_paths = [
    '/auth/signup/',
    '/auth/login/',
    '/auth/google/login/',
    '/auth/oauth/',
    '/favicon.ico'
    
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
                session_id = data['session_id']
                user_activity = caching.get_activity_cache(session_id)
                session = None
                if user_activity == None :
                    session = user_services.get_activity_by_session(data['session_id'])
                    if session == None :
                        return response_functions.forbidden_response_sender([],response_strings.invalid_credentials)
                    caching.activity_cache(session,session_id)
                    session = caching.get_activity_cache(session_id)
                else:
                    session = user_activity
                if session['logout_at'] != 'None':
                    return response_functions.forbidden_response_sender([],response_strings.invalid_credentials)
                request.environ['HTTP_USER_DATA'] = data['sub']
                request.environ['HTTP_SESSION_ID'] = data['session_id']
            except Exception as e:
                print(e)
                raise ForbiddenError(response_strings.invalid_credentials)