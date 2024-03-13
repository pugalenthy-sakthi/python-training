from exception.DataBaseError import DataBaseError
from exception.DuplicateDataError import DuplicateDataError
from models.models import User,Role,Activity
from common import response_strings
from exception.InvalidDataError import InvalidDataError
from factory import db

def create_user(user:User):
    
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        raise InvalidDataError(response_strings.data_already_exist_message)


def create_role(role:Role):

    try:
        db.session.add(role)
        db.session.commit()
    except Exception as e:
        raise DuplicateDataError(response_strings.data_already_exist_message)

    
    
def get_user_role():
    try:
        user_role = Role.query.filter_by(role_name='User').first()
        return user_role
    except Exception as e:
        raise DataBaseError(response_strings.server_error_message)
    
def get_user(email:str):
    try:
        user = User.query.filter_by(email=email).first()
        return user
    except Exception as e:
        raise DataBaseError(response_strings.server_error_message)
    
    
def get_activity_by_session(session_id:str):
    
    try:
        activity = Activity.query.filter_by(session_id=session_id).first()
        return activity
    except Exception as e:
        raise DataBaseError(response_strings.server_error_message)
    
    
def create_user_activity(activity:Activity):
    try:
        db.session.add(activity)
        db.session.commit()
    except Exception as e:
        print(e)
        raise DataBaseError(response_strings.server_error_message)
    

    
    
def update_user_activity(activity):
    try:
        db.session.add(activity)
        db.session.commit()
    except Exception as e:
        raise DataBaseError(response_strings.server_error_message)
    
    
def get_users():
    
    try:
        data = User.query.all()
        return data
    except Exception as e:
        raise DataBaseError(response_strings.server_error_message)
    
    
    