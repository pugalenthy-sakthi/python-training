
from models.base import Base
from sqlalchemy import Column,String,Integer,DateTime,Text,func,null,ForeignKey,Boolean
from sqlalchemy.orm import relationship
from factory import bcrypt


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
    
    
    

    
    
