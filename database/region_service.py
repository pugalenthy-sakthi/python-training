from models.models import Region
from sqlalchemy.exc import IntegrityError
from common import response_strings,response_functions
from geoalchemy2 import functions as func
def create_region(region:Region,session):
  
  try:
    session.add(region)
    session.commit()
    return True
  except IntegrityError as e:
    print(e)
    return False
  except Exception:
    return response_functions.server_error_sender(None,response_strings.server_error_message)
  
def get_region(point,service_provider):
  
  try:
    point = func.ST_GeomFromText(point,4326)
    return Region.query.filter(func.ST_Contains(Region.geometry,point) , Region.service_provider == service_provider).first()
  except Exception as e:
    return response_functions.server_error_sender(None,response_strings.server_error_message)