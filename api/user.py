from flask import Blueprint,request
from services import user_services
from models.Models import User

user_route = Blueprint('routes',__name__)

@user_route.route('/',methods = {"GET"})
def get_all_users():
    return user_services.get_users_data()


@user_route.route('/update/<email>',methods = {"PUT"})
def update_user(email):
    user_details = request.get_json()
    user = User()
    user.name = user_details['name']
    user.email_id = user_details['email_id']
    user.dob = user_details['dob']
    return user_services.update_user_data(user,email)



@user_route.route('/add',methods = {"POST"})
def create_user():
    user_details = request.get_json()
    user = User()
    user.name = user_details['name']
    user.email_id = user_details['email_id']
    user.dob = user_details['dob']
    return user_services.create_user(user)

@user_route.route('/delete/<email>',methods = {"DELETE"})
def delete_user(email):
    return user_services.delete_user_data(email)
    