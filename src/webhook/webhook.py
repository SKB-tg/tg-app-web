import requests

from aiohttp.web_fileresponse import FileResponse
from aiohttp.web_request import Request
from aiohttp.web_response import json_response

from aiogram import Bot
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    WebAppInfo,
)
from aiogram.utils.web_app import check_webapp_signature, safe_parse_webapp_init_data



async def webhook_data_handler(request: Request):
    requests.get('https://api.telegram.org/bot5822305353:AAHexHNC9TLD1HZvZGcMg4C19hGnVGLyr6M/sendmessage?chat_id='+str(5146071572)+'&text=webhook.')

    bot: Bot = request.app["bot"]

    data = await request.post()
    if check_webapp_signature(bot.token, data):
        return json_response({"ok": True}, status=200)#, AnswerWebAppQuery(web_app_query_id= , extra_data="webhook.py" )
    return json_response({"ok": False, "err": "Unauthorized"}, status=401)

if __name__ == "__main__":
    webhook_data_handler()
