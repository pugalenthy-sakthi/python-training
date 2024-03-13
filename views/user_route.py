from flask import Blueprint, jsonify, request
from database import user_services,task_services,uploads_services
from common import response_strings,response_functions
from config import redis_client
from config import cache
from util import session_genarator,async_function
import datetime
import os
from models.models import Uploads

user_route = Blueprint('user_route',__name__,url_prefix='/user')


@user_route.get('/')
@cache.cached(timeout=3000,make_cache_key=session_genarator.get_curent_session)
def get_user():
    print("Hei")
    user_email = request.headers['User-Data']
    user = user_services.get_user(user_email)
    response_body = {
            "name":user.name,
            "email":user.email,
            "is_Admin": user.role.role_name == 'Admin'
    }
    return response_functions.success_response_sender(response_body,response_strings.user_data_fetch_success)


# @user_route.post('/redis/<string:key>/<string:value>')
# def save_into_redis(key,value):
#         try:
#                 # redis_client.set('foo','far')
#                 redis_client.set(key,value)
#                 return "200"
#         except Exception as e:
#                 print(e)
#                 return "500"
        
        
        
# @user_route.get('/redis/<string:key>')
# def get_from_redis(key):
#         try:
#                 value = redis_client.get(key)
#                 if value is None:
#                         return "None"
#                 return value
#         except Exception as e:
#                 print(e)
#                 return "500"


@user_route.post("/createTask")
def create_task():
        data = request.json
        data['created_by'] = request.headers['User-Data']
        data['created_at'] = datetime.datetime.now()
        data['updated_at'] = datetime.datetime.now()
        id =  str(task_services.create_task(data))
        return response_functions.created_response_sender(id,response_strings.task_created_success)
        



@user_route.get('/getTask')
def get_task():
        data = task_services.get_tasks(request.headers['User-Data'])
        response_data = [
                {
                        "task_id": str(task['_id']),
                        "task_name": task['t_name'],
                        "task_status": task['status']
                        }
                        for task in data
                ]
        return response_functions.success_response_sender(response_data,response_strings.tasks_fetch_success)

@user_route.put('/updateTask/<task_id>')
def update_task(task_id):
        task = task_services.get_task(task_id)
        task['updated_at'] = datetime.datetime.now()
        task['t_name'] = request.get_json()['t_name']
        task['status'] = request.get_json()['status']
        task_services.update_task(task_id,task)
        return response_functions.success_response_sender({},response_strings.task_update_success)
        

@user_route.delete('/deleteTask/<task_id>')
def delete_task(task_id):
        task_services.delete_task(task_id)
        return response_functions.success_response_sender({},response_strings.task_delete_success)
        
                
@user_route.post("/singleUpload")
def upload_single_file():
        
        base_path = '/home/divum/Documents/python training/Flask_Crud_App_Security/'
        if not os.path.exists(os.path.join(base_path,'uploads')):
                os.mkdir(os.path.join(base_path,'uploads'))
        base_path = os.path.join(base_path,'uploads')
        user_name = request.headers['User-Data']
        if not os.path.exists(os.path.join(base_path,user_name)):
               os.mkdir(os.path.join(base_path,user_name))
        base_path = os.path.join(base_path,user_name)
        file = request.files['file']
        file_name = str(session_genarator.millis())+file.filename
        file.save(os.path.join(base_path,file_name))
        user_email = request.headers['User-Data']
        user = user_services.get_user(user_email)
        upload = Uploads(os.path.join(base_path,file_name),user)
        uploads_services.save_upload(upload)
        return response_functions.created_response_sender(None,response_strings.upload_success)

@user_route.post('/fileUpload')
def multi_upload():
        base_path = '/home/divum/Documents/python training/Flask_Crud_App_Security/'
        if not os.path.exists(os.path.join(base_path,'uploads')):
                os.mkdir(os.path.join(base_path,'uploads'))
        base_path = os.path.join(base_path,'uploads')
        user_name = request.headers['User-Data']
        if not os.path.exists(os.path.join(base_path,user_name)):
               os.mkdir(os.path.join(base_path,user_name))
        base_path = os.path.join(base_path,user_name)
        files = request.files.getlist('file')
        for file in files:
                file_name = str(session_genarator.millis())+file.filename
                file.save(os.path.join(base_path,file_name))
                user_email = request.headers['User-Data']
                user = user_services.get_user(user_email)
                upload = Uploads(os.path.join(base_path,file_name),user)
                uploads_services.save_upload(upload)
                
        return response_functions.created_response_sender(None,response_strings.upload_success)

@user_route.post('/asyncUpload')
async def async_upload():
    files = request.files.getlist('file')
    await async_function.async_main(request.headers['Authorization'], files)
    return "200"



