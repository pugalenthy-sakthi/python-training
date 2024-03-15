from sqlalchemy.exc import IntegrityError
from models.models import ServiceProvider
from exception.DataBaseError import DataBaseError
from common import response_strings

def create_service_provider(service_provider:ServiceProvider,session):
  
  try:
    session.add(service_provider)
    session.commit()
    return True
  except IntegrityError:
    return False
  except Exception:
    raise DataBaseError(response_strings.server_error_message)
  
  
  
def get_provider(provide_name):
  try:
    provider = ServiceProvider.query.filter_by(name = provide_name).first()
    return provider
  except Exception:
    raise DataBaseError(response_strings.server_error_message)
  
  