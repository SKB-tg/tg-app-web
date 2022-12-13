import logging
from os import getenv
import requests


from aiohttp.web import run_app
from aiohttp.web_app import Application
from src.handlers import my_router
from src.gethandler import demo_handler
from src.sendMessage.sendMessage import send_message_handler
from src.checkData.checkData import check_data_handler
# from handlers import my_router
# from routes import check_data_handler, demo_handler, send_message_handler


from aiogram import Bot, Dispatcher
from aiogram.types import MenuButtonWebApp, WebAppInfo
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

TELEGRAM_TOKEN = "1699887557:AAGvYsHg0IjLplNPmWiBRwbWfQrXVIRzZmU"#getenv("1699887557:AAGvYsHg0IjLplNPmWiBRwbWfQrXVIRzZmU")
APP_BASE_URL = "https://classy-pixie-efeff1.netlify.app" #getenv("URL")


async def on_startup(bot: Bot, base_url: str):
    await bot.set_webhook(f"{base_url}/src/webhook")
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(text="Open Menu", web_app=WebAppInfo(url=f"{base_url}/src"))
    )


def main():
    bot = Bot(token=TELEGRAM_TOKEN, parse_mode="HTML")
    dispatcher = Dispatcher()
    dispatcher["base_url"] = APP_BASE_URL
    dispatcher.startup.register(on_startup)

    dispatcher.include_router(my_router)

    app = Application()
    app["bot"] = bot

    app.router.add_get("/src", demo_handler)
    app.router.add_post("/src/checkData", check_data_handler)#/src/checkData
    app.router.add_post("/src/sendMessage", send_message_handler)#/src/sendMessage
    SimpleRequestHandler(
        dispatcher=dispatcher,
        bot=bot,
    ).register(app, path="/src/webhook")
    setup_application(app, dispatcher, bot=bot)

    requests.get('https://api.telegram.org/bot5822305353:AAHexHNC9TLD1HZvZGcMg4C19hGnVGLyr6M/sendmessage?chat_id='+str(5146071572)+'&text=start.')

    run_app(app, host="127.0.0.1", port=8081)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
