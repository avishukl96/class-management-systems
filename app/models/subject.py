from sqlalchemy import Column, Integer, String, TIMESTAMP,func
from app.config.db import Base

class Subject(Base):
    __tablename__ = 'subjects'

    subject_id = Column(Integer, primary_key=True, index=True)
    subject_name = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())  
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

