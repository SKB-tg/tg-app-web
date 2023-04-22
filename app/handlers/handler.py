from aiogram import Bot, F, Router, Dispatcher
from aiogram.filters import Command
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MenuButtonWebApp,
    Message,
    WebAppInfo,
)
_dispatcher=Dispatcher()
m_router = Router()
_dispatcher.include_router( m_router)# 

@_dispatcher.message(Command(commands=["start"]))
async def command_start(message: Message, bot: Bot, base_url: str):
    await bot.set_chat_menu_button(
        chat_id=message.chat.id,
        menu_button=MenuButtonWebApp(text="Загрузить магазин", web_app=WebAppInfo(url=f"{base_url}")),
    )
    await message.answer("""Привет!\nОтправьте мне любое сообщение для подтверждения.\nИли наберите /webview""")


@m_router.message(Command(commands=["webview"]))
async def command_webview(message: Message, base_url: str):
    await message.answer(
        "Отлично. Теперь вы можете посетить наш сайт через Webview",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Загрузить магазин", web_app=WebAppInfo(url=f"{base_url}")
                    )
                ]
            ]
        ),
    )


@m_router.message(~F.message.via_bot)  # Echo to all messages except messages via bot
async def echo_all(message: Message, base_url: str):
    await message.answer(
        "Загрузить магазин",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Загрузить магазин", web_app=WebAppInfo(url=f"{base_url}"))]
            ]
        ),
    )

# @my_router.message()  # Echo to all messages except messages via bot
# async def echo_all(message: Message):
#     print('eys')
#     await message.answer(
#         "Тест webview",
#         reply_markup=ReplyKeyboardRemove()
#     )
