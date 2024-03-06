
from flask import jsonify
from models.Models import User
from config import db

def get_users_data():
    users = User.query.all()
    
    return jsonify({
        "data":[
            {
                "name":user.name,
                "email":user.email_id,
                "date_of_birth":user.dob
            }
            for user in users
        ],
    }),200


def create_user(user):
    db.session.add(user)
    db.session.commit()
    return "Created",201


def update_user_data(user,email):
    
    old_data = db.session.query(User).filter(User.email_id.__eq__(email)).all()[0]
    old_data.dob = user.dob
    old_data.name = user.name
    
    db.session.add(old_data)
    db.session.commit()
    return "OK",200


def delete_user_data(email):
    
    old_data = db.session.query(User).filter(User.email_id.__eq__(email)).all()[0]
    
    
    db.session.delete(old_data)
    db.session.commit()
    
    return "DELETED",200