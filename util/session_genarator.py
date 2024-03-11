import uuid
from flask import request

def get_random_id():
    return uuid.uuid4().hex


def get_curent_session():
    return request.headers['Session-Id']