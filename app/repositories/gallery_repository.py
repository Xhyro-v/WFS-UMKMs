from sqlalchemy.orm import Session
from app.models.gallery import Gallery

def create_gallery(
      db: Session,
      gallery: Gallery
):
      db.add(gallery)
      db.commit()
      db.refresh(gallery)
      
      return gallery

def update_gallery(
      db: Session,
      gallery : Gallery
):
      db.commit()
      db.refresh(gallery)

def delete_gallery(
      db: Session,
      gallery: Gallery
):
      db.delete(gallery)
      db.commit()


def get_by_id(
      db: Session,
      gallery_id: int
):
      return (
            db.query(Gallery)
            .filter(Gallery.id == gallery_id)
            .first()
      )

def get_all(db: Session):
      return (
          db.query(Gallery)
          .all()
      )


def get_by_published(db: Session):
      return (
            db.query(Gallery)
            .filter(Gallery.is_published == True)
            .all()
      )

def get_by_un_published(db: Session):
      return (
            db.query(Gallery)
            .filter(Gallery.is_published == False)
            .all()
      )

def publish_gallery(
      db : Session,
      gallery_id: int
):
      gallery = (db.query(Gallery)
                .filter(Gallery.id == gallery_id)
                .first()
      )
      if gallery:
            gallery.is_published = True
            db.commit(gallery)
            db.refresh()
      
      return gallery

def un_publish_gallery(
      db : Session,
      gallery_id: int
):
      gallery = (db.query(Gallery)
                .filter(Gallery.id == gallery_id)
                .first()
      )
      if gallery:
            gallery.is_published = False
            db.commit(gallery)
            db.refresh()
      
      return gallery