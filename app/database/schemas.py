from typing import List, Union

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str  
    attribute: str 
    description: str 
    price: int       #dels.PositiveIntegerField(verbose_name='Стоимость')
    slug: str        #dels.CharField(max_length=80, verbose_name='Алиас')
    category: str        #escription = Column(String, unique=True, index=True)tring, index=Tr
    src: str 


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    name: str
    description: str
    slug: str
    price: int

    class Config:
        orm_mode = True

class ProductPhotoBase(BaseModel):
    name_product: str


class ProductPhotoCreate(ProductBase):
    id_product: int


class ProductPhoto(ProductBase):
    id: int
    id_product: int

    class Config:
        orm_mode = True

class TgUserBase(BaseModel):
    first_name: str


class TgUserCreate(TgUserBase):
    password: str


class TgUser(TgUserBase):
    codename: str
    is_active: bool
    first_name: str

    class Config:
        orm_mode = True