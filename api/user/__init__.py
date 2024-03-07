from flask import Blueprint
from services import user_service
from middleware.token_required_func import token_reqiured
user_route = Blueprint('user_route',__name__,url_prefix='/user')
user_route.before_request(token_reqiured)

@user_route.get('/')
def get_user():
    return user_service.get_user_data()



