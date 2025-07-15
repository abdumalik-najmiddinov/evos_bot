from aiogram import Router, types, F

router = Router()
about_photo = "https://ik.imagekit.io/h4yilyuyg/image3.jpg?updatedAt=1752478965734"


@router.message(F.text == "📞 Kontaktlar/Manzil")
async def bot_start(message: types.Message):
    await message.answer(text="""Manzil: Furqat ko'chasi 175, kirish 1, 
2-qavat.
Mo'ljal: MAKRO THE TOWER

Kontakt: +998 71 203 12 12""")
    await message.answer_location(latitude=41.302196, longitude=69.248867)


# --------------------------------------
@router.message(F.text == "📞 Контакты/Адрес")
async def bot_start(message: types.Message):
    await message.answer(text="""📍Адрес:  ул. Фурката 175, 1 подъезд, 2 этаж.
📌Ориентир: MAKRO THE TOWER

📲 Контакты: +998 71 203 12 12""")
    await message.answer_location(latitude=41.302196, longitude=69.248867)
