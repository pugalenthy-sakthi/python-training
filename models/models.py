
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
    is_deleted = Column(Boolean,default=False)
    
    activities = relationship('Activity',uselist=True, back_populates='user')
    role = relationship('Role', backref='users')
    
    
    def __init__(self,name,email,password) -> None:
        self.name = name
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.email = email

class Activity(Base):
    
    __tablename__ = 'user_activity_table'
    user_id = Column(Integer,ForeignKey('user_table.id'),nullable=False)
    access_token = Column(Text,nullable=False)
    refresh_token = Column(Text,nullable=False)
    login_at = Column(DateTime(timezone=True),default=func.now())
    logout_at = Column(DateTime(timezone=True),default=null)
    
    def __init__(self,user,access,refresh):
        self.user = user
        self.access_token = access
        self.refresh_token = refresh
    
    user = relationship('User', back_populates='activities')

    
    
class Role(Base):
    
    __tablename__ = 'user_role_table'
    role_name = Column(String(10),nullable=False,unique=True)
    

    
    
