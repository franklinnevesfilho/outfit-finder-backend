from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base
from .user import user_roles

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)

    users = relationship("User", secondary=user_roles,  back_populates="role")