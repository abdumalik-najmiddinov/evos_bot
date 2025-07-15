from aiogram import Router, types
from aiogram.filters import Command
from filters.users_chat import IsPrivate
from keyboard.default import main_menu

router = Router()



@router.message(IsPrivate(), Command("start"))
async def bot_start(message: types.Message):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-14_10-06-20.jpg?updatedAt=1752469592749"
    await message.answer_photo(photo=photo,
                         reply_markup=main_menu())




