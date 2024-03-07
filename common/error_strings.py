from http import HTTPStatus

data_not_present_error = {'error_phrase':'The Required Data is not Present in the Request','http_status':HTTPStatus.BAD_REQUEST}
invalid_data_error = {'error_phrase':'The Request Data is Invalid','http_status':HTTPStatus.BAD_REQUEST}
user_data_exist_error = {'error_phrase':'The User Email Exist','http_status':HTTPStatus.CONFLICT}
duplicate_data_error = {'error_phrase':'The Data Already Exist','http_status':HTTPStatus.CONFLICT}
database_error = {'error_phrase':'Error with DB connection','http_status':HTTPStatus.SERVICE_UNAVAILABLE}
invalid_password_error = {'error_phrase':'Invalid Password','http_status':HTTPStatus.FORBIDDEN}
email_not_found = {'error_phrase':'Email Address Not Found','http_status':HTTPStatus.NOT_FOUND}