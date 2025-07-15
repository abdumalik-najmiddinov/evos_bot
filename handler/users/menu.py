from aiogram import Router, types, F
from aiogram.filters import Command
from filters.users_chat import IsPrivate
from keyboard.default import main_menu

router = Router()
about_photo = "https://ik.imagekit.io/h4yilyuyg/image2.jpg?updatedAt=1752478076882"


@router.message(F.text == "📱 Меню")
async def bot_start(message: types.Message):
    await message.answer_photo(photo=about_photo,
                               caption="""<a href="https://evos.uz/">Перейти на сайт Evos</a>""", parse_mode="html")

    await message.answer(text="""
        <a href="https://www.instagram.com/evosuzbekistan/">Instagram</a> | <a href="https://t.me/evosuzbekistan">Telegram</a> | <a href="https://www.facebook.com/evosuzbekistan">Facebook</a>
        """,
        parse_mode="HTML"
    )
# --------------------------------------
@router.message(F.text == "Menyu")
async def bot_start(message: types.Message):
    await message.answer_photo(photo=about_photo,
                               caption="""<a href="https://evos.uz/">Evos saytiga o'tish</a>""", parse_mode="html")

    await message.answer(text="""
        <a href="https://www.instagram.com/evosuzbekistan/">Instagram</a> | <a href="https://t.me/evosuzbekistan">Telegram</a> | <a href="https://www.facebook.com/evosuzbekistan">Facebook</a>
        """,
        parse_mode="HTML"
    )