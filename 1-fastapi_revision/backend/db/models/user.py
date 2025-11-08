from db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    blogs = relationship("Blog", back_populates="author", cascade="all, delete-orphan")