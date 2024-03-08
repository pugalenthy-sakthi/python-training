from flask import Blueprint,request
auth_route = Blueprint('auth_route',__name__,url_prefix='/auth')
from services import auth_service
from middleware.token_required import token_required


@auth_route.post('/signup')
def sign_up():
    return auth_service.user_sign_up()


@auth_route.post('/login')
def login():
    return auth_service.user_login()


@auth_route.post('/create_role/<role>')
def create_role(role):
    return auth_service.role_creation(role)


@auth_route.get('/logout')
@token_required
def logout():
    return auth_service.user_logout()


@auth_route.get('/refresh')
def refresh():
    return auth_service.get_refreshed_token()
    
