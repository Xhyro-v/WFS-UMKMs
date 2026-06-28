from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.gallery import Gallery
from app.schemas.gallery import GalleryCreate, GalleryUpdate, GalleryResponse
from app.repositories.gallery_repository import(                 create_gallery,
      update_gallery ,
      delete_gallery ,
      get_by_id, get_all, 
      publish_gallery, 
      un_publish_gallery,
      get_by_published ,
      get_by_un_published, 
      get_gallery_published_id
)

#create_gallery_service
#update_gallery_service
#delete_gallery_servuce
#get_all
#get_by_id_service
#get_published_gallery
#get_un_published_gallery
#get_gallery_published_id
#publish_gallery_service
#un_publish_gallery_service


def create_gallery_service(
      data: GalleryCreate,
      db: Session,
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
      
      new_gallery = Gallery(
            title = data.title,
            description = data.description,
            image_path = data.image_path,
            uploaded_by=current_admin.id
        )
      
      try:
          create_gallery(db,new_gallery)
      except IntegrityError:
          db.rollback()
          raise HTTPException(
              status_code=409,
              detail="Gallery already exist!!"
          )
      return {
            "message":"Gallery successfully created",
            "Content": new_gallery.title,
            "uploaded_by":new_gallery.uploaded_by
      }

def update_gallery_service(
      db: Session,
      gallery_id: int,
      data: GalleryUpdate
):
      gallery = get_by_id(db,gallery_id)
      
      if not gallery:
            raise HTTPException(
                  status_code=404,
                  detail="Gallery not found!")
      
      
      gallery.title = data.title
      gallery.description = data.description
      gallery.image_path = data.image_path
      
      try:
            updated_gallery = update_gallery(db,gallery)
      except IntegrityError:
            db.rollback()
            raise HTTPException(
                  status_code=409,
                  detail="Somthing wrong with update gallery process!!"
            )
      return {
            "message": "Gallery successfully updated",
            "gallery": updated_gallery.title
      }

def delete_gallery_service(
      db: Session,
      gallery_id: int
):
      gallery = get_by_id(db,gallery_id)
      
      if not gallery:
            raise HTTPException(
                  status_code=404,
                  detail="Gallery not found!!"
            )
      delete_gallery(db,gallery)
      
      return {
            "message": "Gallery successfully deleted"
      }


def get_by_id_service(
      db: Session,
      gallery_id: int
):
      gallery = get_by_id(db,gallery_id)
  
      if not gallery:
            raise HTTPException(
                  status_code=404,
                  detail=f"No gallery with id {gallery_id}"
            )
      return gallery

def get_published_gallery(db: Session):
      gallery = get_by_published(db)
      return gallery

def get_un_published_gallery(db: Session):
      gallery = get_by_un_published(db)
      return gallery

def get_gallery_published_id_service(
      db: Session,
      gallery_id: int
):
      gallery = get_gallery_published_id(db, gallery_id)
      
      if not gallery :
            raise HTTPException(
                  status_code=404,
                  detail="Not found"
            )
      return gallery

def publish_gallery_service(
      db: Session,
      gallery_id: int
):
      gallery = get_by_id(db, gallery_id)
      
      if not gallery:
            raise HTTPException(
                  status_code=404,
                  detail="Gallery not found!")
      if gallery.is_published == True:
            raise HTTPException(
                  status_code=404,
                  detail="Gallery already published!")
      
      gallery = publish_gallery(db, gallery_id)
      
      return {
            "message":"Gallery successfully published",
            "Gallery": gallery.title
      }

def un_publish_gallery_service(
      db: Session,
      gallery_id: int
):
      gallery = get_by_id(db, gallery_id)
      
      if not gallery:
            raise HTTPException(
                  status_code=404,
                  detail="Gallery not found!")
      if gallery.is_published == False:
            raise HTTPException(
                  status_code=404,
                  detail="Gallery already unpublished!")
      
      gallery = un_publish_gallery(db, gallery_id)
      
      return {
            "message":"Gallery successfully unpublished",
            "Gallery": gallery.title
      }