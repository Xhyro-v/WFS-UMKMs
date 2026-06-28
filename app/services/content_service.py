from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.content import Content
from app.enums.content_type import ContentType
from app.schemas.content import ContentCreate, ContentResponse, ContentUpdate
from app.repositories.content_repository import(               create_content,
    update_content, 
    delete_content,
    get_by_id, 
    get_all, 
    get_by_type, 
    get_published,
    get_un_published,  
    publish_content, 
    un_publish_content, 
#
    get_by_id_published,
    get_all_published,
    get_by_published_type
)

def create_content_service(
      db: Session,
      data: ContentCreate,
      current_admin
):
      if data is None :
            raise HTTPException(
                status_code=400,
                detail="Invalid Data"
            )
      
      
      if len(data.title.strip()) == 0 :
            raise HTTPException(
                status_code=400,
                detail="Fill title !"
            )
      if len(data.title) > 100 :
            raise HTTPException(
                status_code=400,
                detail="Title max 100 character"
            )
      
      
      if len(data.description.strip()) == 0 :
            raise HTTPException(
                status_code=400,
                detail="Fill description !"
            )
      if len(data.description) > 150 :
            raise HTTPException(
                status_code=400,
                detail="Description max 150 character !"
            )
      
      
      if len(data.location.strip()) == 0 :
            raise HTTPException(
                status_code=400,
                detail="Fill location !"
            )
      if len(data.location) > 150 :
            raise HTTPException(
                status_code=400,
                detail="Location max 150 character"
            )
      
      
      new_content = Content(
          title = data.title,
          content_type = data.content_type,
          description = data.description,
          image_path = data.image_path,
          location = data.location,
          uploaded_by=current_admin.id
      )

   
      try:
          create_content(db,new_content)
      except IntegrityError:
          db.rollback()
          raise HTTPException(
              status_code=409,
              detail="Content already exist!!"
          )
      return {
            "message":"Content successfully created",
            "Content": new_content.title,
            "uploaded_by":new_content.uploaded_by
      }

def update_content_service(
      db: Session,
      content_id: int,
      data: ContentUpdate
):
      content = get_by_id(db, content_id)
      
      if not content :
            raise HTTPException(
                status_code=404,
                detail="Content not found !"
            )
      
      
      content.title = data.title
      content.content_type = data.content_type
      content.description = data.description
      content.image_path = data.image_path
      content.location = data.location
      
      try:
          updated_content = update_content(db,content)
      except IntegrityError:
          db.rollback()
          raise HTTPException(
              status_code=409,
              detail="Something wrong with update content process!!"
          )
      return {
            "message":"Content successfull updated",
            "Content": updated_content.title
      }

def delete_content_service(
        db: Session,
        content_id: int
):
        content = get_by_id(db, content_id)
        
        if not content:
              raise HTTPException(
                  status_code=404,
                  detail="Content not found"
              )
        delete_content(db, content)
        return {
            "message":"Content successfull deleted"
        }

def get_by_id_service(
      db: Session,
      content_id: int
):
      content = get_by_id(db,content_id)
      
      if not content:
            raise HTTPException(
                status_code=404,
                detail=f"No content with id {content_id}"
            )
      return content

def get_all_content(db: Session):
      return get_all(db)

def get_by_type_service(
      db: Session,
      content_type: ContentType
):
      content = get_by_type(db, content_type)
      if not content:
          raise HTTPException(
              status_code=422,
              detail="Type of content is empty"
          )
      return content

def get_by_published(
      db: Session
):
      content = get_published(db)
      return content

def get_by_un_published(
      db: Session
):
      content = get_un_published(db)
      return content

def publish_content_service(
      db : Session,
      content_id: int
):
      content = get_by_id(db, content_id)
      
      if not content :
            raise HTTPException(
                status_code=404,
                detail="Content not found"
            )
      if content.is_published == True:
            raise HTTPException(
                status_code=404,
                detail="Content is already published"
            )
    
      content = publish_content(db, content_id)
      
      return {
          "message":"Content published successfully",
          "Content": content.title
      }

def un_publish_content_service(
      db : Session,
      content_id: int
):
      content = un_publish_content(db, content_id)
      
      if not content :
            raise HTTPException(
                status_code=404,
                detail="Content not found"
            )
      if content.is_published == False:
            raise HTTPException(
                status_code=404,
                detail="Content is already unpublished"
            )
      return {
          "message":"Content unpublished successfully",
          "Content": content.title
      }



#——————————————————————PUBLICSERVICE—————————————————————————

def get_by_id_published_service(
      db: Session,
      content_id: int
):
      content = get_by_id_published(db,content_id)
      
      if not content:
            raise HTTPException(
                status_code=404,
                detail="Content not found"
            )
      return content

def get_all_published_content(db: Session):
      return get_all_published(db)

def get_by_published_type_content(
      db: Session,
      content_type: ContentType
):
      return get_by_published_type(db,content_type)