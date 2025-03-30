
from pydantic import BaseModel,Field,EmailStr,field_validator
import re
from datetime import datetime, timezone,timedelta
from util.password import generate_random_password

class UserRequest(BaseModel):

    name: str= Field(min_length=2)
    email: EmailStr
    password: str= Field(min_length=8, default=generate_random_password())

    @field_validator('str')
    @classmethod
    def isStrongPassword(cls, password: str):
        __pattern = r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[^\w\s]).+$'
        if(len(password)<8 or re.match(__pattern, password)):
            raise ValueError("Password is not strong enough")
        return password
        
    remeber_token:bool = Field(default=True)
    email_verified_at:datetime 

    @field_validator("email_verified_at")
    def isValidDateTime(cls,date: datetime):
        start_date=datetime(1990,1,1,tzinfo=timezone.utc)
        if(start_date<=date< start_date+timedelta(days=2)):
            raise ValueError("email need to be verified within 1 day itself")

        if date.tzinfo is None or date.tzinfo.utcoffset(date) is None:
            raise ValueError("Timezon is not correctly registered. ")
        return date