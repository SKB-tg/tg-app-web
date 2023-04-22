from fastapi import APIRouter, Request, Response, FastAPI, Depends
from fastapi.responses import Response
#from auth.api import router as auth
import json

import logging

from typing import Dict
from transliterate import slugify, translit

from app.database.crud import create_Product, get_Product
from pydantic import BaseModel
from fastapi import Body
from sqlalchemy.orm import Session

from app.database import schemas
from app.db import SessionLocal, engine
from app.database import crud
#from app.handlers.handler import bot


from aiogram import Bot, Dispatcher
from aiohttp.web_request import BaseRequest
from app.u_utils import Methods

# from aiohttp.web_response import json_response
from aiogram.utils.web_app import check_webapp_signature, safe_parse_webapp_init_data, parse_webapp_init_data

router = APIRouter()
TELEGRAM_TOKEN1="1699887557:AAGvYsHg0IjLplNPmWiBRwbWfQrXVIRzZmU"
bot = Bot(token=TELEGRAM_TOKEN1, parse_mode="HTML")

class DataBot(BaseModel):
    data: Dict
    # item_data: Dict 
    # id_m: int = 5
def get_db():
    """
    A dependency for working with PostgreSQL
    """
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        logging.error(e)
    finally:
        db.close()



@router.post("/zakazDataForm/")#, response_model=UserResponse)
async def zakaz_data_form_handler(request: Request, db: Session = Depends(get_db)):
    #bot: Bot = request.app["bot"]
    #data=[]
    data = await request.body()
    # data1=[]
    # data1= [str(i[0]).split(':') for i in data.items()]
    # data2= [l[0]+':'+ l[1][3:] for l in data1]
    # data3=data2[:-4].extend(data2[-2:])
    # for l in data2.items():
    #     product={}
    #     product[]=

    print(data.decode())
    #add_img_product(STATIC_PATH + '/img/3.png')
    #get_img_product(1)
    if data == None:
        return {"ok": False, "err": "Unauthorized", "status": 401}
    # await bot.answer_web_app_query(
    #     web_app_query_id=web_app_init_data.query_id,
    #     result=InlineQueryResultArticle(
    #         id=web_app_init_data.query_id,
    #         title="Demo",
    #         input_message_content=InputTextMessageContent(
    #             message_text='''Уважаемая {id}.\nВаш заказ принят, ожидайте оповещения!\n
                

    #             ''',
    #        ),
    #         reply_markup=reply_markup,
    #     ),
    # ) #             parse_mode=None
    return {"ok": True}
###################################################################


@router.post("/sendDataDB/")    # служебная ф. длясохранения продукции в базе
async def send_data_json_for_db_handler(request1: Dict, db: Session = Depends(get_db)):
    #bot: Bot = request.app["bot"]
    _product = request1

    if _product:
        print(_product)
        if _product.get("quantity"):
            _product.pop("quantity")
            _product.pop("id")
        _product["slug"]="" + str(slugify(_product.get('name'))) + '-' + (slugify(_product["attribute"]) if (_product["attribute"] != '') else 'X')

        db_product=get_Product(db, name=_product["name"])#row_is_db('product', ('slug', data_product.get('slug')))
        if db_product == None:
            crud.create_Product(db=db, product=_product)
            print('этого товара еще нет', _product)
        else:
           print('такой уже есть', f"id-{db_product.id}")

        return {"ok": _product}

    return {"ok": True}
##################################################################################
@router.post("/checkData/")
async def check_data_handler(request: Dict):
    data = request["data"]
    # Bot.set_current(bot)
    #data={"data":{"_auth":"query_id=AAFGAjQZAAAAAEYCNBlDdEo-&user=%7B%22id%22%3A422838854%2C%22first_name%22%3A%22%D0%9A%D0%B8%D1%80%D0%B8%D0%BB%D0%BB%22%2C%22last_name%22%3A%22sl%22%2C%22username%22%3A%22KirSl19%22%2C%22language_code%22%3A%22ru%22%7D&auth_date=1681729483&hash=9ba9571a67d66db9038f4ebca1c7d6ed6a079a5ba0c2ee8219c3240d9794fe82"}}
    #data = await request.body()
    print(data)
    if check_webapp_signature(bot.token, data["_auth"]):
        return {"ok": True}
    return {"ok": False, "err": "Unauthorized"}


@router.post("/sendMessage/")
async def send_message_handler(request: Dict):
    data = request["data"]
    print(data)
    try:
        web_app_init_data = safe_parse_webapp_init_data(token=bot.token, init_data=data["_auth"])
    except ValueError:
        return {"ok": False, "err": "Unauthorized"}
    waid_d ={}
    w_a_i_d0 = data['msg'].split('&')
    waid_d=[(str(i).split(':')[0], str(i).split(':')[1]) for i in w_a_i_d0]
    w_a_i_d=dict(waid_d)
    print('ppp', w_a_i_d)#['Категория'])
    #d= w_a_i_d.get('Аттрибут') if w_a_i_d.get('Аттрибут') else '--' 
    reply_markup = None
    await bot.send_message(chat_id=web_app_init_data.user.id,
            text=f'''Уважаемый {web_app_init_data.user.username}.\nВаш заказ принят, ожидайте,
             наш курьер свяжется с вами!\n        ------------------------------         \nИнформация о вашем заказе:\n                 \nИмя закащика: {w_a_i_d['Имя']}\nИзделие: {w_a_i_d['Изделие']}\nРазмер: midle\nКол-во:  {w_a_i_d['Количество']}\nЦена:  {w_a_i_d['Цена']} руб.\nОбщая сумма: {w_a_i_d['Общая сумма']} руб.\n''',)


    if data["with_webview"] == "1":
        reply_markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Open",
                        web_app=WebAppInfo(url=str(request.url.with_scheme("https"))),
                    )
                ]
            ]
        )
    # await bot.answer_web_app_query(
    #     web_app_query_id=web_app_init_data.query_id,
    #     result=InlineQueryResultArticle(
    #         id=web_app_init_data.query_id,
    #         title="Demo",
    #         input_message_content=InputTextMessageContent(message_text=f'''Уважаемая {web_app_init_data.user.username}.\nВаш заказ принят, ожидайте оповещения!\n
    #             ''',
    #         parse_mode=None,
    #        ),
    #         reply_markup=reply_markup,
    #     ),
    # ) #             parse_mode=None,
    
    return {"ok": True}

async def check_data_handler(request: Request):
    bot: Bot = request.app["bot"]

    data = await request.post()
    _parse_webapp_init_data = parse_webapp_init_data(init_data=data["_auth"])

    print('OOOO', dict(_parse_webapp_init_data.user))
    tg_user_data = dict(_parse_webapp_init_data.user)

    _tg_user_is_base = tg_user_is_db(dict(_parse_webapp_init_data.user))

    #add_img(STATIC_PATH + '/img/3.png')
    #print(_tg_user_is_base)
    if _tg_user_is_base == False:
        try:
            print(tg_user_data)
            add_tg_user(tg_user_data)
        except exceptions.NotCorrectMessage as e:
            print('eeeee')
    print(TgUser.is_bot)
    if check_webapp_signature(bot.token, data["_auth"]):
        return json_response({"ok": True})

    return json_response({"ok": False, "err": "Unauthorized"}, status=401)
