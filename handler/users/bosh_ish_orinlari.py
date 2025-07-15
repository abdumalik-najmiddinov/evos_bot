from aiogram import Router, types, F

from keyboard.default import (glavnye_vakansii_ru, toshkent_menu, andijon_menu,
                              qarshi_menu, qoqon_menu, namangan_menu, toshkent_viloyati_menu, samarqand_viloyati_menu,
                              fergana_viloyati_menu, shahrisabz_menu, navoiy_menu, urgench_menu, main_menu,
                              bosh_ish_orinlari_uz)

router = Router()


@router.message(F.text == "💼 Bo'sh ish o'rinlari")
async def show_filials(message: types.Message):
    await message.answer(text="EVOS jamoasiga qo'shiling!", reply_markup=bosh_ish_orinlari_uz())
    await message.answer(text="📍 Shaharni tanlang.", reply_markup=bosh_ish_orinlari_uz())


@router.message(F.text == "Toshkent")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang", reply_markup=toshkent_menu())


@router.message(F.text == "Andijon")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang", reply_markup=andijon_menu())


@router.message(F.text == "Qarshi")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang", reply_markup=qarshi_menu())


@router.message(F.text == "Qo'qon")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang", reply_markup=qoqon_menu())


@router.message(F.text == "Namangan")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang", reply_markup=namangan_menu())


@router.message(F.text == "Toshkent viloyati")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang", reply_markup=toshkent_viloyati_menu())


@router.message(F.text == "Nukus")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang", reply_markup=toshkent_viloyati_menu())


@router.message(F.text == "Samarqand")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang", reply_markup=samarqand_viloyati_menu())


@router.message(F.text == "Farg'ona")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang", reply_markup=fergana_viloyati_menu())


@router.message(F.text == "Shahrisabz")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang", reply_markup=shahrisabz_menu())


@router.message(F.text == "Navoiy")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang", reply_markup=navoiy_menu())



@router.message(F.text == "Urgench")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang", reply_markup=urgench_menu())



@router.message(F.text == "Ortga ↩️")
async def show_filials(message: types.Message):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-14_10-06-20.jpg?updatedAt=1752469592749"
    await message.answer_photo(photo=photo,
                               reply_markup=bosh_ish_orinlari_uz())

@router.message(F.text == "Ortga ↩️")
async def show_filials(message: types.Message):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-14_10-06-20.jpg?updatedAt=1752469592749"
    await message.answer_photo(photo=photo,
                               reply_markup=bosh_ish_orinlari_uz())


@router.message(F.text == "❌ Bekor qilish ❌")
async def show_filials(message: types.Message):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-14_10-06-20.jpg?updatedAt=1752469592749"
    await message.answer_photo(photo=photo,
                         reply_markup=main_menu())




