from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from app.config.db import Base

class Classes(Base):  # Changed class name from 'Class' to 'Classes'
    __tablename__ = 'classes'  # Table name remains 'classes' in the database

    class_id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String(255), nullable=False)
    status = Column(String(20), default='active')
    created_at = Column(TIMESTAMP, server_default=func.now())  
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
