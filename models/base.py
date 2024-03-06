
import uuid
from config import db
from sqlalchemy import func,String,Column,DateTime


def default_uuid():
    return uuid.uuid4().hex

class Base(db.Model):
    __abstract__=True
    id = Column(String(40), primary_key=True, default=lambda: default_uuid())
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    update_at = Column(DateTime(timezone=True), onupdate=func.now(),default=func.now())

