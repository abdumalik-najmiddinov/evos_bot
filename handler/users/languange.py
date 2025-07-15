from aiogram import Router, types, F
from keyboard.default import languange_ru, languange_uz, main_menu_ru, main_menu

router = Router()
about_photo = "https://ik.imagekit.io/h4yilyuyg/image3.jpg?updatedAt=1752478965734"


@router.message(F.text == "🇺🇿/🇷🇺 Til")
async def bot_start(message: types.Message):
    await message.answer(text="Tilni o'zgartirish", reply_markup=languange_uz())


# --------------------------------------
@router.message(F.text == "🇺🇿/🇷🇺 Язык")
async def bot_start(message: types.Message):
    await message.answer(text="Смена языка", reply_markup=languange_ru())


# -------------------- ru
@router.message(F.text == "🇷🇺 Русский")
async def bot_start(message: types.Message):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-14_10-06-20.jpg?updatedAt=1752469592749"
    await message.answer_photo(photo=photo,
                         reply_markup=main_menu_ru())

# -------------------- uz
@router.message(F.text == "🇺🇿 O'zbekcha")
async def bot_start(message: types.Message):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-14_10-06-20.jpg?updatedAt=1752469592749"
    await message.answer_photo(photo=photo,
                         reply_markup=main_menu())

# ------------------------------- uz back
@router.message(F.text == "⬅️ Ortga")
async def bot_start(message: types.Message):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-14_10-06-20.jpg?updatedAt=1752469592749"
    await message.answer_photo(photo=photo,
                         reply_markup=main_menu())


# -------------------------------- ru back
@router.message(F.text == "🔙 Назад")
async def bot_start(message: types.Message):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-14_10-06-20.jpg?updatedAt=1752469592749"
    await message.answer_photo(photo=photo,
                         reply_markup=main_menu_ru())