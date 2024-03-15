from flask import Blueprint,request
from geoalchemy2 import WKTElement
from config import db
from exception.DataNotPresentError import DataNotPresentError
from exception.DuplicateDataError import DuplicateDataError
from exception.InvalidDataError import InvalidDataError
from common import response_strings,response_functions
from models.models import ServiceProvider,Restaurent,Region
from database import provider_service,restaurent_service,region_service
from shapely.geometry import Point,Polygon
from pyproj import Proj, transform

admin_route = Blueprint('admin_route',__name__,url_prefix='/admin')


@admin_route.post('/provider/create')
def create_service_provider():
  service_provider_date = request.get_json()
  if 'service_provider_name' in service_provider_date:
    service_provider = ServiceProvider(service_provider_date['service_provider_name'])
    session = db.session
    status = provider_service.create_service_provider(service_provider,session)
    if status :
      session.commit()
      return response_functions.created_response_sender(None,response_strings.service_provider_created)
    else:
      session.rollback()
      raise DuplicateDataError(response_strings.data_already_exist_message)
  else:
    raise DataNotPresentError(response_strings.invalid_data_string)
  
  
@admin_route.post('/restaurent/create')
def create_restaurent():
  restaurent_data = request.get_json()
  required_fields = ['restaurent_name','latitude','longitude','service_providers']  
  if all(field in restaurent_data for field in required_fields):
    point = f'POINT({restaurent_data['longitude']} {restaurent_data['latitude']})'
    restaurent = Restaurent(restaurent_data['restaurent_name'],point)
    providers = restaurent_data['service_providers']
    for provider in providers:
      provider = provider_service.get_provider(provider)
      if provider is None:
        raise DataNotPresentError(response_strings.provider_not_found)
      if provider in restaurent.service_providers:
        raise DuplicateDataError(response_strings.duplicate_provider_message)
      restaurent.service_providers.append(provider)
    session = db.session
    state = restaurent_service.create_restaurent(restaurent,session)
    if not state:
      session.rollback()
      raise DuplicateDataError(response_strings.data_already_exist_message)
    else:
      session.commit()
      return response_functions.created_response_sender(None,response_strings.restaurent_create_message)
  else:
    raise InvalidDataError(response_strings.invalid_data_string)


@admin_route.post('/region/create')
def create_region():
  region_data = request.get_json()
  required_fields = ['region_name','service_provider','region_points']
  if all(field in region_data for field in required_fields ):
    if len(region_data['region_points']) >= 3:
      region_points = region_data['region_points']
      points_list = []
      for region_point in region_points:
        point = Point(region_point['longitude'], region_point['latitude'])
        points_list.append(point)
      polygon = Polygon(points_list)
      provider = provider_service.get_provider(region_data['service_provider'])
      region = Region(name=region_data['region_name'],service_provider=provider,geometry=polygon)
      session = db.session
      state = region_service.create_region(region,session)
      if state :
        session.commit()
        return response_functions.created_response_sender(None,response_strings.region_created_error)
      else :
        session.rollback()
        raise DuplicateDataError(response_strings.data_already_exist_message)
    else:
      raise InvalidDataError(response_strings.region_points_error)
  else:
    raise InvalidDataError(response_strings.invalid_data_string)
  

