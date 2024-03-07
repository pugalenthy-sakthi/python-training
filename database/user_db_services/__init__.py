
from exception.DataBaseError import DataBaseError
from factory import db
from models.models import User,Role,Activity
from common import error_strings
from exception.InvalidDataError import InvalidDataError


def create_user(user:User):
    
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        raise InvalidDataError(error_strings.duplicate_data_error)


def create_role(role:Role):
    
    try:
        db.session.add(role)
        db.session.commit()
    except Exception as e:
        raise InvalidDataError(error_strings.duplicate_data_error)
    
    
def get_user_role():
    try:
        user_role = db.session.query(Role).filter_by(role_name='User').first()
        return user_role
    except Exception as e:
        raise DataBaseError(error_strings.database_error)
    
    
def get_user(email):
    try:
        user = db.session.query(User).filter_by(email=email).first()
        return user
    except Exception as e:
        raise DataBaseError(error_strings.database_error)
    
    
def create_user_activity(activity:Activity):
    try:
        db.session.add(activity)
        db.session.commit()
    except:
        raise DataBaseError(error_strings.database_error)
    