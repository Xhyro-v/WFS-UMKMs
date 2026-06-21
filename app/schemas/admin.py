from pydantic import BaseModel, EmailStr, Field, ConfigDict

class AdminRegister(BaseModel):
    username: str
    email :  EmailStr
    password : str
    confirm_password : str

class AdminLogin(BaseModel):
    email: EmailStr
    password : str 

class AdminOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(
        "from_attributes": True
    )

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    email : str | None = None