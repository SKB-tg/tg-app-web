from sqlalchemy.orm import Session

from app.database import models, schemas


def get_TgUser(db: Session, user_id: int):
    return db.query(models.TgUser).filter(models.TgUser.id == user_id).first()


def get_TgUser_by_email(db: Session, first_name: str):
    return db.query(models.TgUser).filter(models.TgUser.first_name == first_name).first()


def get_TgUsers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TgUser).offset(skip).limit(limit).all()


def create_TgUser(db: Session, user: schemas.TgUserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.TgUser(**user.dict(), hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_Product(db: Session, name: str):
    return db.query(models.Product).filter(models.Product.name == name).first()

def get_Products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_Product(db: Session, product: schemas.ProductCreate):
    if not type(product) == dict:
        db_product = models.Product(**product.dict())
    else:
        db_product = models.Product(**product)

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def create_product_photo(db: Session, product_photo: schemas.ProductPhotoCreate, id__product: int):
    db_photo = models.ProductPhoto(**product_photo.dict(), id_product=id__product)
    db.add(db_photo)
    db.commit()
    db.refresh(db_photo)
    return db_photo
