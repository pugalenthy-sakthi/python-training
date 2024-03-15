
from models.base import Base
from sqlalchemy import Column,String,Integer,DateTime,Text,func,null,ForeignKey,Boolean,Table
from sqlalchemy.orm import relationship
from factory import bcrypt
from geoalchemy2.types import Geometry

service_provider_restaurent_association = Table(
    'service_provider_restaurent_table',
    Base.metadata,
    Column('restaurent_id',Integer,ForeignKey('restaurent_table.id')),
    Column('service_provider_id',Integer,ForeignKey('service_provider_table.id'))
)


class User(Base):
    
    __tablename__ = 'user_table'
    
    name = Column(String(50),nullable=False)
    
    email = Column(String(60),nullable=False,unique=True)
    
    password = Column(Text,nullable=False)
    
    role_id = Column(Integer,ForeignKey('user_role_table.id'),nullable=False)
    
    uploads = relationship('Uploads',uselist=True,back_populates='user')
    
    activities = relationship('Activity',uselist=True, back_populates='user')
    
    role = relationship('Role', backref='users')
    
    def __init__(self,name,email,password) -> None:
        self.name = name
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.email = email

class Activity(Base):
    
    __tablename__ = 'user_activity_table'
    
    user_id = Column(Integer,ForeignKey('user_table.id'),nullable=False)
    
    login_at = Column(DateTime(timezone=True),default=func.now())
    
    logout_at = Column(DateTime(timezone=True))
    
    session_id = Column(String(50),nullable=False)
    
    def __init__(self,user):
        self.user = user
    
    user = relationship('User', back_populates='activities')

    
    
class Role(Base):
    
    __tablename__ = 'user_role_table'
    
    role_name = Column(String(10),nullable=False,unique=True)
    
    
class Uploads(Base):
    
    __tablename__ = 'upload_table'
    
    def __init__(self,file_path,user):
        self.file_path = file_path
        self.user = user
    
    file_path = Column(Text,nullable=False)
    
    user_id = Column(Integer,ForeignKey('user_table.id'),nullable=False)
    
    user = relationship('User',back_populates='uploads') 
    
    
class ServiceProvider(Base):
    
    __tablename__ = 'service_provider_table'
    
    name = Column(String(40),unique=True)
    
    regions = relationship('Region',uselist=True,back_populates='service_provider')
    
    restaurents = relationship('Restaurent', secondary=service_provider_restaurent_association, back_populates='service_providers')
    
    def __init__(self,name):
        self.name = name
    
    
class Region(Base):
    
    __tablename__ = 'region_table'
    
    name = Column(String(40),unique=True)
    
    service_provider_id = Column(Integer,ForeignKey('service_provider_table.id'))
    
    geometry = Column(Geometry(geometry_type='POLYGON', srid=4326),nullable=False)
    
    service_provider = relationship('ServiceProvider',back_populates='regions')
    
    def __init__(self,name,service_provider,geometry):
        self.name = name
        self.service_provider = service_provider
        self.geometry = str(geometry)
        
class Restaurent(Base):
    
    __tablename__ = 'restaurent_table'
    
    name = Column(String(40),unique=True)
        
    point = Column(Geometry(geometry_type='POINT', srid=4326),nullable=False) 
    
    service_providers = relationship('ServiceProvider', secondary=service_provider_restaurent_association, back_populates='restaurents')
    
    def __init__(self,name,point):
        self.name = name
        self.point = point   