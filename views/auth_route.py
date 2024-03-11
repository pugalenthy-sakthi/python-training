from flask import Blueprint,request
from middleware.custome_decorator import token_required
from exception.DataNotPresentError import DataNotPresentError
from exception.DuplicateDataError import DuplicateDataError
from exception.InvalidDataError import InvalidDataError
from util import verify_data
from models.models import User,Role,Activity
from database import user_services
from common import response_strings,response_functions
from flask_jwt_extended import create_access_token,create_refresh_token
from util import session_genarator,caching
import datetime



auth_route = Blueprint('auth_route',__name__,url_prefix='/auth')


@auth_route.post('/signup/')
def sign_up():
    
    try:
        required_fields = ['name','password','email']  
        sign_up_details = request.get_json()
        if all(field in sign_up_details for field in required_fields):
            if verify_data.validate_signup_data(sign_up_details):
                if user_services.get_user(sign_up_details['email']) != None:
                    raise DuplicateDataError(response_strings.data_already_exist_message)
                user_role = user_services.get_user_role()
                user = User(sign_up_details['name'],sign_up_details['email'],sign_up_details['password'])
                user.role = user_role
                user_services.create_user(user)
                return response_functions.created_response_sender([],response_strings.user_created_success)
            
            else:
                raise InvalidDataError(response_strings.invalid_data_string)
        else:
            raise DataNotPresentError(response_strings.invalid_data_string)
        
    except Exception as e:
        print(e)
        return "Error"


@auth_route.post('/login/')
def login():
    required_fields = ['password','email']
    login_details = request.get_json()
    if all(field in login_details for field in required_fields):
        if verify_data.validate_login_data(login_details):
            user = user_services.get_user(login_details['email'])
            if user == None:
                raise DataNotPresentError(response_strings.user_not_found)
            session_id = session_genarator.get_random_id()
            if verify_data.validate_user_login(login_details,user):
                access_token = create_access_token(user.email,additional_claims={'session_id':session_id})
                refresh_token = create_refresh_token(user.email,additional_claims={'session_id':session_id})
                token_response = {
                    'access_token':access_token,
                    'refresh_token':refresh_token
                 }
                
                user_activity = Activity(user)
                user_activity.session_id=session_id
                user_services.create_user_activity(user_activity)
                caching.activity_cache(user_activity,session_id)
                print(session_id)
                return response_functions.success_response_sender(token_response,response_strings.user_login_success)
            else:
                return response_functions.forbidden_response_sender([],response_strings.invalid_credentials)
        else:
            raise InvalidDataError(response_strings.invalid_data_string)
    else:
        raise DataNotPresentError(response_strings.invalid_data_string)


# @auth_route.post('/create_role/<role_name>/')
# def create_role(role_name):
#     role = Role()
#     role.role_name = role_name
#     user_services.create_role(role)
#     return "Role Created",200


@auth_route.get('/logout')
def logout():
    
    session_id = request.headers['Session_Id']
    activity = user_services.get_activity_by_session(session_id)
    activity.logout_at = datetime.datetime.now()
    user_services.update_user_activity(activity)
    return response_functions.success_response_sender({},response_strings.user_logout_success)


@auth_route.get('/refresh')
def refresh():
    
    session_id = request.headers['Session_Id']
    activity = user_services.get_activity_by_session(session_id)
    if activity != None and activity.logout_at == None:
        user = activity.user
        access_token = create_access_token(user.email,additional_claims={'session_id':session_id})
        refresh_token = create_refresh_token(user.email,additional_claims={'session_id':session_id})
        token_response = {
            'access_token':access_token,
            'refresh_token':refresh_token
        }
        return response_functions.success_response_sender(token_response,response_strings.refresh_token_success)
    else:
        return response_functions.forbidden_response_sender([],response_strings.invalid_credentials)
    
