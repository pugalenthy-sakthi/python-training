from config import redis_client
from flask import jsonify
import json
import traceback

from models.models import Activity

def activity_cache(activity:Activity,session_id:str):
    
    # activity_dict = {
    #     "session_id":activity.session_id,
    #     "user_id":activity.user_id,
    #     "login_at":str(activity.login_at),
    #     "logout_at":str(activity.logout_at)
    # }

    # jstr = (json.dumps(activity_dict))
    try:
        
        redis_client.set("foo","far")
        
    except Exception as e:
        print(traceback.print_exception(e))
    # print(jstr)
    # print(session_id)
    
    # set 152d75488fce42e19890e73878762f45 '{\"session_id\": \"152d75488fce42e19890e73878762f45\", \"user_id\": 2, \"login_at\": \"2024-03-11 14:59:26\", \"logout_at\": \"None\"}'
    
    
def get_activity_cache(session_id):
    return redis_client.get(session_id)


def delete_activity_cache(session_id):
    redis_client.delete(session_id)
    