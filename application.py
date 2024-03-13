from exception import global_error_handler
from factory import create_app
from config import db
from models.models import User,Activity
from flask_migrate import Migrate
from common import response_functions,response_strings
from util.scheduler import scheduler
import asyncio

app = create_app()
migrate = Migrate(app,db)


@app.errorhandler(404)
def invlaid_route_handle(error):
    return response_functions.not_found_sender([],response_strings.wrong_url_message)


@app.errorhandler(Exception)
def global_error(error):
    return global_error_handler.global_error_handler(error)


if __name__=='__main__':
    # scheduler.start()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.run(host='0.0.0.0',port=app.config['PORT']))