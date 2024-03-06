from factory import create_app
from config import Config as config
from config import db
from models import Models
from api.user import user_route
app = create_app()
app.register_blueprint(user_route,url_prefix='/user')

if(__name__=='__main__'):
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=config.PORT)