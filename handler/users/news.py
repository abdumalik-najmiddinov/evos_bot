from aiogram import Router, types, F


router = Router()
about_photo = "https://ik.imagekit.io/h4yilyuyg/image2.jpg?updatedAt=1752478076882"


@router.message(F.text == "🗣 Новости")
async def bot_start(message: types.Message):
    await message.answer(text="""Новости компании
Акция
Новые филиалы
Новые торты и т.д.""")
# --------------------------------------
@router.message(F.text == "🗣 Yangiliklar")
async def bot_start(message: types.Message):
    await message.answer(text="""Kompaniya yangiliklari
Aksiya
Yangi filiallar
Yangi tortlar va hk.""")