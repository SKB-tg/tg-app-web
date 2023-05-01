#from app.dispatcher import routes, views
#from app.handlers.handler import my_router
#from app.handlers.routes import check_data_handler, demo_handler, send_message_handler
#from app.settings import config, BASE_DIR
from app.settings import settings
from aiogram import Bot, Dispatcher
from aiogram.types import MenuButtonWebApp, WebAppInfo, Message, Update
from aiogram.webhook.aiohttp_server import setup_application, SimpleRequestHandler

from aiogram.filters import Command

from pathlib import Path



STATIC_PATH = str(Path('main.py').parent.resolve()) + '/public'
#TELEGRAM_TOKEN = ""#getenv("")
#APP_BASE_URL = "https://7bf2-46-56-191-9.ngrok-free.app" #getenv("URL")
WEBHOOK_PATH=f"/bot/{settings.TELEGRAM_TOKEN}"

def setup_config(application):
    application["config"] = config


def setup_app(application):
   # настройка всего приложения состоит из:
   #setup_external_libraries(application)  # настройки внешних библиотек, например шаблонизатора

   setup_routes(application)  # настройки роутера приложения
   for resource in application.router.resources():
      print(resource)

async def on_startup(bot: Bot, base_url: str):
    await bot.set_webhook(f"{base_url}/webhook", drop_pending_updates=True)
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(text="Open Menu", web_app=WebAppInfo(url=f"{base_url}"))
    )

#def main():


    # _dispatcher.include_router(my_router)
    # setup_admin(app, admin_class=CustomAdmin,  # put here your new template view to register it
    # views=[FirstCustomView,])


#     app = Application() # создаем наш веб-сервер
#     setup_app(app)  # настраиваем приложение

#     run_app(app, host="127.0.0.1", port=7800)

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     main()

#---------------------------------------------

import logging

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.dispatcher import main_router, views
from app.dispatcher.routes import bot
from app.handlers.handler import m_router, _dispatcher
from app.database import models
from app.db import metadata, engine
WEBHOOK_URL=settings.APP_BASE_URL + WEBHOOK_PATH

#bot = Bot(token=TELEGRAM_TOKEN, parse_mode="HTML")
#print(71, bot.__dict__)

SimpleRequestHandler(
    dispatcher=_dispatcher, bot=bot,)

_dispatcher["base_url"] = settings.APP_BASE_URL
app = FastAPI(title=settings.APP_TITLE)

app.include_router(main_router)# router_views])

app.mount("/static", StaticFiles(directory="public/static"), name="static")

#---------------------------------------------
#from aiohttp.web_app import Application

#print(87, settings.ALLOWED_HOST)

#_dispatcher.startup.register(on_startup)
#setup_application(app, _dispatcher, bot=bot)
# _dispatcher.include_router(m_router)
# appp = Application() # создаем наш веб-сервер
# appp["bot"] = bot
# app.mount("/subapi", appp)
#SimpleRequestHandler(
#    dispatcher=_dispatcher, bot=bot,)#.register(app, path="/webhook")
#------------------------------------------

# @m_router.message(Command(commands=["start"]))
# async def start(message: Message):
#     await message.answer(f"Salom, {message.from_user.full_name}")



@app.on_event("startup")
async def startup():
    models.Base.metadata.create_all(bind=engine)
#    await db.connect()
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )

@app.post(WEBHOOK_PATH)#
async def bot_webhook(update: dict):
  tg_update=Update(**update)
  Bot.set_current(bot)
  rec=await _dispatcher.feed_update(bot, tg_update)


@app.on_event("shutdown")
async def shutdown():
#    await db.disconnect()
    await bot.session.close()


if __name__ == "__main__":
    """
    Server configurations
    """
    uvicorn.run(
        app="main:app",
        host=settings.ALLOWED_HOST,
        debug=settings.DEBUG,
        port=settings.ALLOWED_PORT,
        reload=True,
        log_level=logging.INFO,
        use_colors=True,
    )
