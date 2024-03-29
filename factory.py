from flask import Flask
from config import config,db,bcrypt,jwt,mail,scheduler,cache,oauth
from views.admin_route import admin_route
from views.user_route import user_route
from views.auth_route import auth_route
from middleware.token_required import token_reqiured



def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = config.APP_SECRET_KEY
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(admin_route)
    app.register_blueprint(auth_route)
    app.register_blueprint(user_route)
    app.before_request(token_reqiured)
    scheduler.init_app(app)
    mail.init_app(app)
    cache.init_app(app)
    oauth.init_app(app)
    return app

