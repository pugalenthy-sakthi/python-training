from flask import request
from exception.DataNotPresentError import DataNotPresentError
from exception.DuplicateDataError import DuplicateDataError
from exception.InvalidDataError import InvalidDataError
from util import verify_data
from models.models import User,Role,Activity
from database import user_db_services
from common import response,response_strings,error_strings
from http import HTTPStatus
from flask_jwt_extended import create_access_token,create_refresh_token
from sqlalchemy import func
import datetime 


def user_sign_up():
    
    required_fields = ['name','password','email']  
    sign_up_details = request.get_json()
    if all(field in sign_up_details for field in required_fields):
        if verify_data.validate_signup_data(sign_up_details):
            print(user_db_services.get_user(sign_up_details['email']))
            if user_db_services.get_user(sign_up_details['email']) != None:
                raise DuplicateDataError(error_strings.user_data_exist_error)
            user_role = user_db_services.get_user_role()
            user = User(sign_up_details['name'],sign_up_details['email'],sign_up_details['password'])
            user.role = user_role
            user_db_services.create_user(user)
            return response.response_builder(HTTPStatus.CREATED,[],response_strings.user_created_success)
            
        else:
            raise InvalidDataError(error_strings.invalid_data_error)
    else:
        raise DataNotPresentError(error_strings.data_not_present_error)
    

def user_login():
    
    required_fields = ['password','email']
    login_details = request.get_json()
    if all(field in login_details for field in required_fields):
        if verify_data.validate_login_data(login_details):
            user = user_db_services.get_user(login_details['email'])
            if user == None:
                raise DataNotPresentError(error_strings.user_data_exist_error)
            
            if verify_data.validate_user_login(login_details,user):
                
                access_token = create_access_token(user.email)
                refresh_token = create_refresh_token(user.email)
                token_response = {
                    'access_token':access_token,
                    'refresh_token':refresh_token
                 }
                user_activity = Activity(user,access_token,refresh_token)
                user_db_services.create_user_activity(user_activity)
                return response.response_builder(HTTPStatus.OK,token_response,response_strings.user_login_success)
            else:
                raise InvalidDataError(error_strings.invalid_password_error)
        else:
            raise InvalidDataError(error_strings.invalid_data_error)
    else:
        raise DataNotPresentError(error_strings.data_not_present_error)
    


def role_creation(role_name):
    
        role = Role()
        role.role_name = role_name
        user_db_services.create_role(role)
        return "Role Created",200
    
    
def user_logout():
    
    access_token = request.headers['Authorization']
    activity = user_db_services.get_user_activity(access_token)
    activity.logout_at = datetime.datetime.now()
    user_db_services.update_user_activity(activity)
    
    return response.response_builder(HTTPStatus.OK,{},response_strings.user_login_success)


def get_refreshed_token():
    
    if 'Authorization' not in request.headers:
        return "FORDIBBEN",403
    
    refresh_token = request.headers['Authorization']
    activity = user_db_services.get_user_activity_refresh(refresh_token)
    if activity != None and activity.logout_at == None:
        user = activity.user
        access_token = create_access_token(user.email)
        refresh_token = create_refresh_token(user.email)
        token_response = {
            'access_token':access_token,
            'refresh_token':refresh_token
        }
        activity.access_token = access_token
        activity.refresh_token = refresh_token
        user_db_services.update_user_activity(activity)
        return response.response_builder(HTTPStatus.OK,token_response,response_strings.user_login_success)
    else:
        return "FORBIDDEN",403