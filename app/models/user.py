from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP,func
from sqlalchemy.orm import relationship
from app.config.db import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey('user_roles.role_id'), nullable=False)
    status = Column(String(20), default='pending')
    created_at = Column(TIMESTAMP, server_default=func.now())  
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    role = relationship("UserRole", back_populates="users")

