from flask import request
from database import user_db_services
from common import response,response_strings
from http import HTTPStatus

def get_user_data():
    
    user_email = request.headers['User-Data']
    user = user_db_services.get_user(user_email)

    response_body = {
            "name":user.name,
            "email":user.email,
            "is_Admin": user.role.role_name == 'Admin'
    }
    return response.response_builder(HTTPStatus.OK,response_body,response_strings.user_data_fetch_success)
    
    
    