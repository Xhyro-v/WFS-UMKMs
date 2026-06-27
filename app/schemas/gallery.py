from datetime import datetime
from pydantic import Field, ConfigDict, BaseModel


class GalleryCreate(BaseModel):
      title : str
      description: str | None = None
      image_path: str | None = None

class GalleryUpdate(BaseModel):
      title : str | None = None
      description: str | None = None
      image_path: str | None = None

class GalleryResponse(BaseModel):
      id : int
      title : str
      description : str
      image_path : str
      created_at : datetime
      is_published : bool
      uploaded_by : int

      model_config = ConfigDict(
      from_attributes = True
      )