from flask import Blueprint, request
from database import user_services
from middleware.token_required import token_reqiured
from common import response_strings,response_functions

user_route = Blueprint('user_route',__name__,url_prefix='/user')


@user_route.get('/')
def get_user():
    user_email = request.headers['User-Data']
    user = user_services.get_user(user_email)

    response_body = {
            "name":user.name,
            "email":user.email,
            "is_Admin": user.role.role_name == 'Admin'
    }
    return response_functions.success_response_sender(response_body,response_strings.user_data_fetch_success)



