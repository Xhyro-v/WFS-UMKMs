from sqlalchemy.orm import Session
from app.models.content import Content
from app.enums.content_type import ContentType

#CRUD
def create_content(
  db: Session,
  content: Content
):
      db.add(content)
      db.commit()
      db.refresh(content)

      return content
def update_content(
    db: Session,
    content: Content
):
      db.commit()
      db.refresh(content)

      return content
def delete_content(
    db: Session,
    content: Content
):
      db.delete(content)
      db.commit()

      return content
#End CRUD

#Show data
def get_by_id(
    db: Session,
    content_id : int
):
      return (
          db.query(Content)
          .filter(Content.id == content_id)
          .first()
      )

def get_by_type(
    db: Session ,
    content_type: ContentType
):
      return (
          db.query(Content)
          .filter(Content.content_type == content_type)
          .all()
      )

def get_published(db: Session):
      return (
          db.query(Content)
          .filter(Content.is_published == True)
          .all()
      )

def get_un_published(db: Session):
      return (
          db.query(Content)
          .filter(Content.is_published == False)
          .all()
      )

def get_all(db: Session):
      return (
          db.query(Content)
          .all()
      )
#End Data Show


#Change Status
def publish_content(
    db: Session,
    content_id: int
):
    content = (
        db.query(Content)
        .filter(Content.id == content_id)
        .first()
    )

    if content:
        content.is_published = True
        db.commit()
        db.refresh(content)

    return content

def un_publish_content(
    db: Session,
    content_id: int
):
    content = (
        db.query(Content)
        .filter(Content.id == content_id)
        .first()
    )

    if content:
        content.is_published = False
        db.commit()
        db.refresh(content)

    return content
#End Status Change

#——————————————————————PUBLICSERVICE—————————————————————————

def get_by_id_published(
    db: Session,
    content_id : int
):
      return (
          db.query(Content)
          .filter(
                Content.id == content_id,
                Content.is_published == True
          )
          .first()
      )

def get_all_published(db: Session):
      return (
          db.query(Content)
          .filter(Content.is_published == True)
          .all()
      )

def get_by_published_type(
    db: Session ,
    content_type: ContentType
):
      return (
          db.query(Content)
          .filter(
                  Content.content_type == content_type,
                  Content.is_published == True
          )
          .all()
      )