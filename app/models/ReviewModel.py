from sqlalchemy import Column,String,DateTime,Boolean,UUID

from models.Base import base

class Review(base):
    __tablename__ ="Review"
    id=Column(UUID,primary_key=True,index=True)
    product_review=Column(String,nullable=False)
