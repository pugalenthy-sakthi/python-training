from flask import jsonify
from Response import ResponseBuilder

def ResponseSender(http_status,msg,data,status_code):
    response = ResponseBuilder(http_status,msg,data)
    return jsonify(response.getResponse()),status_code