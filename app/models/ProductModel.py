from sqlalchemy import Column,Integer, Float, UUID, String, LargeBinary, Enum
from sqlalchemy.orm import relationship
from models.Base import base
import enum

class Status(enum.Enum):
    inStock ="Available"
    outOfStock ="Not Available"

class Product(base):
    __tablename__ ="Product"
    id=Column(UUID,primary_key=True,index=True)
    name=Column(String(120),nullable=False)
    description=Column(String(500))
    price=Column(Float,nullable=False)
    stock=Column(Integer,nullable=False,default=0)
    status=Column(Enum(Status),nullable=False) 
    image=Column(LargeBinary) 
    category=relationship("Category",back_populates="User")