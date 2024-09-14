from sqlalchemy import Column, Integer, String, TIMESTAMP,func
from app.config.db import Base
from sqlalchemy.orm import relationship

class UserRole(Base):
    __tablename__ = 'user_roles'

    role_id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(255), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())  
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    users = relationship("User", back_populates="role")

