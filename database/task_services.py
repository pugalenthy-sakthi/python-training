
from bson import ObjectId
from config import mdb

def create_task(data):
    
    tasks=mdb['tasks']
    inserted_task = tasks.insert_one(data)
    return inserted_task.inserted_id


def get_tasks(email):
    
    task = mdb['tasks']
    return task.find({'created_by':email},{'create_at':0,'updated_at':0,'created_by':0})

def get_task(id):
    
    task = mdb['tasks']
    return task.find_one({'_id':ObjectId(id)})


def update_task(id,task_update):
    
    task = mdb['tasks']
    task.update_one({'_id':ObjectId(id)},{'$set':task_update})
    
    
def delete_task(task_id):

    task = mdb['tasks']
    task.delete_one({'_id':ObjectId(task_id)})
    


    
    