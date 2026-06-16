from pydantic import BaseModel, EmailStr, Field

class AdminRegister(BaseModel):
    username: str
    email :  EmailStr
    password : str = Field(min_length=8)
    confirm_password : str = Field(min_length=8)

class AdminLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class AdminOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = {
        "from_attributes": True
    }