from sqlalchemy import Column,String,Integer,DateTime,func
from config import db
import uuid




class Base(db.Model):
    
    __abstract__ = True
    
    id = Column(Integer, primary_key = True, autoincrement=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True),server_onupdate=func.now(),default=func.now())
    
    