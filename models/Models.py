from models.base import Base
from sqlalchemy import Column,String,Date,Text

class User(Base):
    __tablename__='user_table'
    name = Column(String(20),nullable=False)
    email_id = Column(String(40),unique=True,nullable=False,primary_key=True)
    dob = Column(Date,nullable=False)

