
from flask import make_response,jsonify



def response_builder(http_status,data,message):
    
    response_body = {
        'http_status':http_status.phrase,
        'message':message,
        'data':data,
        }
    response = make_response(jsonify(response_body))
    response.headers['content-type'] = 'application/json'
    response.status_code = http_status.value
    
    return response