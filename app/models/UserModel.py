from sqlalchemy import Column,String,DateTime,Boolean,UUID

from models.Base import base

class User(base):
    __tablename__ ="User"
    id=Column(UUID,primary_key=True,index=True)
    name=Column(String,nullable=False)
    email=Column(String(120),nullable=False,unique=True)
    password=Column(String(128),nullable=False)
    remeber_token=Column(Boolean,default=True) 
    email_verified_at=Column(DateTime)
