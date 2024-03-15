from models.models import Restaurent,Region,ServiceProvider
from sqlalchemy.exc import IntegrityError
from exception.DataBaseError import DataBaseError
from common import response_strings
from geoalchemy2 import functions as func
from geoalchemy2.comparator import Comparator
from sqlalchemy import and_,asc

def create_restaurent(restaurent:Restaurent,session):
  try:
    session.add(restaurent)
    session.commit()
    return True
  except IntegrityError:
    return False
  except Exception:
    raise DataBaseError(response_strings.server_error_message)
  
  
def get_nearest_restaurents(service_provider,point):
  try:

    point = func.ST_GeomFromText(point,4326)
    nearest_points = Restaurent.query.filter(Restaurent.service_providers.contains(service_provider)).order_by(
          func.ST_Distance(Restaurent.point, point)
        ).all()
    return nearest_points
  except Exception:
    raise DataBaseError(response_strings.server_error_message)
  
  
def get_restaurents_by_region_and_points(region:Region,service_provider:ServiceProvider,point,page_no,max_per_page):
  
  try:
    point = func.ST_GeomFromText(point,4326)
    return Restaurent.query.filter(and_(Restaurent.service_providers.contains(service_provider),func.ST_Contains(region.geometry,Restaurent.point))).order_by(
      asc(func.ST_Distance(Restaurent.point,point))
    ).paginate(page=page_no,error_out=False,max_per_page=max_per_page)
    
  except:
    raise DataBaseError(response_strings.server_error_message)
  
  