from typing import List, Union

import json
from typing import Any, Callable, Optional
from urllib.parse import parse_qs, parse_qsl

from aiogram.utils.web_app import WebAppUser
from pydantic import BaseModel
import datetime


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
    #id: int 
    id_chat: int = 0
    is_bot: bool = None
    first_name: str = ""
    last_name: str = ""
    username: str = ""
    language_code: str = 'ru'
    photo_url: bool = None
    is_active: bool = False
    password: str = ""
    created: datetime = None


class TgUserCreate(TgUserBase):
    pass



class TgUser(TgUserBase):
    id: int
    username: str
    first_name: str
    id_chat: int 
    is_bot: bool 
    last_name: str 
    language_code: str
    photo_url: bool
    is_active: bool
    password: str
    created: datetime

    class Config:
        orm_mode = True

