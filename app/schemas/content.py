from datetime import datetime
from pydantic import Field, ConfigDict ,BaseModel
from app.enums.content_type import ContentType

class ContentCreate(BaseModel):
      title : str 
      content_type : ContentType
      description : str | None = None
      image_path : str | None = None
      location : str | None = None

class ContentUpdate(BaseModel):
      title : str | None = None
      content_type : ContentType | None = None
      description : str | None = None
      image_path : str | None = None
      location : str | None = None


class ContentResponse(BaseModel):
      id : int
      title : str 
      content_type : ContentType
      description : str 
      image_path : str | None = None
      location : str | None = None
      is_published : bool
      created_at : datetime
      uploaded_by : int
  
      model_config = ConfigDict(
      from_attributes = True
    )

