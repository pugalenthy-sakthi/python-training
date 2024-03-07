from functools import wraps

def custom_logger(func):
    
    @wraps(func)
    def handle_function(*args,**kwargs):
        print("user--->logging")
        return func(*args,**kwargs)
        
    return handle_function
        