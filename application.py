
from exception.DataBaseError import DataBaseError
from exception.DataNotPresentError import DataNotPresentError
from exception.DuplicateDataError import DuplicateDataError
from exception.InvalidDataError import InvalidDataError
from factory import create_app
from config import db
from models.models import User,Activity
from flask_migrate import Migrate
from common import response


app = create_app()
migrate = Migrate(app,db)


@app.errorhandler(DataNotPresentError)
def date_not_present_error(error):
    return response.response_builder(error.error_data['http_status'],[],error.error_data['error_phrase'])

@app.errorhandler(InvalidDataError)
def invalid_data_error(error):
    return response.response_builder(error.error_data['http_status'],[],error.error_data['error_phrase'])

@app.errorhandler(DataBaseError)
def database_error(error):
    return response.response_builder(error.error_data['http_status'],[],error.error_data['error_phrase'])

@app.errorhandler(DuplicateDataError)
def duplicate_data_error(error):
    return response.response_builder(error.error_data['http_status'],[],error.error_data['error_phrase'])

if __name__=='__main__':
    app.run(host='0.0.0.0',port=app.config['PORT'])