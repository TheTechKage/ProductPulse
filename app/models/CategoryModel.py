from sqlalchemy import Column,Integer, Float, UUID, String, LargeBinary
from sqlalchemy.orm import relationship
from models.Base import base

class Category(base):
    __tablename__ ="Category"
    id=Column(UUID,primary_key=True,index=True)
    name=Column(String(120),nullable=False)
    description=Column(String(500))
    products=relationship("Product",back_populates="Category",cascade="all, delete-orphan")