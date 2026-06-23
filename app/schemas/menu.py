from pydantic import BaseModel, Field, ConfigDict
from app.enums.menu_type import MenuType


class MenuCreate(BaseModel):
    title : str
    price : int
    description : str | None = None
    image_path : str
    menu_type : MenuType

class MenuUpdate(BaseModel):
    title : str | None = None
    price : int | None = None
    description : str | None = None
    image_path : str | None = None
    menu_type : MenuType | None = None

class MenuResponse(BaseModel):
    id : int
    title : str
    price : int
    description : str | None
    image_path : str
    menu_type : MenuType
    uploaded_by : int
  
    model_config = ConfigDict(
      from_attributes = True
    )