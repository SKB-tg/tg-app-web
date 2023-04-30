"""Endpoints module."""
from typing import Dict, List

from fastapi import APIRouter, Depends, Response, status, Request, HTTPException, FastAPI
from sqlalchemy.orm import Session

from app.database import crud, models, schemas
from app.db import SessionLocal, engine
#from app.dispatcher import main_router

#from dependency_injector.wiring import inject, Provide

# from .containers import Container
# from .services import UserService
# from .repositories import NotFoundError

#Запуск server      uvicorn endpoints:app --reload


#Base.metadata.create_all(bind=engine)

router = APIRouter()
#router = APIRouter()


# @router.get("/users")
# @inject
# def get_list(
#         user_service: UserService = Depends(Provide[Container.user_service]),
# ):
#     return user_service.get_users()


# @router.get("/users/{user_id}")
# @inject
# def get_by_id(
#         user_id: int,
#         user_service: UserService = Depends(Provide[Container.user_service]),
# ):
#     try:
#         return user_service.get_user_by_id(user_id)
#     except NotFoundError:
#         return Response(status_code=status.HTTP_404_NOT_FOUND)


# @router.post("/users", status_code=status.HTTP_201_CREATED)
# @inject
# def add(
#         user_service: UserService = Depends(Provide[Container.user_service]),
# ):
#     return user_service.create_user()


# @router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
# @inject
# def remove(
#         user_id: int,
#         user_service: UserService = Depends(Provide[Container.user_service]),
# ):
#     try:
#         user_service.delete_user_by_id(user_id)
#     except NotFoundError:
#         return Response(status_code=status.HTTP_404_NOT_FOUND)
#     else:
#         return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/status/")
def get_status():
    return {"status": "OK"}





def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/product/", response_model=schemas.Product)
def create_Product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.get_Product(db, name=product.name)
    if db_product:
        raise HTTPException(status_code=400, detail="Такой товар существует")
    return crud.create_Product(db=db, product=product)


@router.get("/product/{name}/", response_model=schemas.Product)
def read_product(name: str, db: Session = Depends(get_db)):
    db_product = crud.get_Product(db, name=name)
    if db_product is None:
        raise HTTPException(status_code=404, detail="product not found")
    return db_product

@router.get("/users/", response_model=List[schemas.TgUser])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_TgUsers(db, skip=skip, limit=limit)
    return users

@router.get("/user/{name}/", response_model=schemas.TgUser)
def read_user(name: str, db: Session = Depends(get_db)):
    db_user = crud.get_TgUser_by_email(db, first_name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return db_user

@router.post("/create-user/", response_model=schemas.TgUser)
def _create_TgUser(user: schemas.TgUserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_TgUser_by_email(db, first_name=user.first_name)
    if db_user:
        raise HTTPException(status_code=400, detail="Такой user существует")
    return crud.create_TgUser(db=db, user=user)
# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items