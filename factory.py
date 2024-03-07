from flask import Flask
from config import config,db,bcrypt,jwt
from api import admin,auth,user


def create_app():
    
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(admin.admin_route)
    app.register_blueprint(auth.auth_route)
    app.register_blueprint(user.user_route)
    return app
