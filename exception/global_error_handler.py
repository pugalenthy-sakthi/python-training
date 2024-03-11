from common import response_functions,response_strings

def global_error_handler(error:Exception):
    custom_error = ['DataBaseError','DataNotPresentError','DuplicateDataError','InvalidDataError','ForbiddenError']
    print(error)
    
    if type(error).__name__ in custom_error:
        
        error_name = type(error).__name__
        if error_name == custom_error[0]:
            return response_functions.server_error_sender([],str(error))
        elif error_name == custom_error[1]:
            return response_functions.not_found_sender([],str(error))
        elif error_name == custom_error[2]:
            return response_functions.conflict_error_sender([],str(error))
        elif error_name == custom_error[3]:
            return response_functions.bad_request_sender([],str(error)) 
        elif error_name == custom_error[4]:
            return response_functions.forbidden_response_sender([],str(error))
        else:
            return response_functions.server_error_sender([],response_strings.server_error_message)
        
    
    else :
        
        return response_functions.server_error_sender([],response_strings.server_error_message)