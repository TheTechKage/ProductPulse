from pydantic import BaseModel,Field,EmailStr

class UserResponse(BaseModel):
    name: str= Field(description="User name required")
    email: EmailStr = Field(description="User email required")

    # future scope
    #  roles: user/admin/etc
    # token: str