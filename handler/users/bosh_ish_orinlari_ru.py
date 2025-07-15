from aiogram import Router, types, F

from keyboard.default import (glavnye_vakansii_ru, tashkent_menu_ru, andijan_menu_ru,
                              karshi_menu_ru, kokand_menu_ru, namangan_menu_ru, tashkent_viloyat_menu_ru,
                              fergana_viloyat_menu_ru,
                              shahrisabz_menu_ru, navoiy_menu_ru, urgench_menu_ru, nukus_menu_ru,
                              samarkand_viloyat_menu_ru, main_menu_ru, main_menu)

router = Router()


@router.message(F.text == "💼 Вакансии")
async def show_filials(message: types.Message):
    await message.answer(text="Присоединяйтесь к команде EVOS!", reply_markup=glavnye_vakansii_ru())
    await message.answer(text="📍 Выберите город.", reply_markup=glavnye_vakansii_ru())


@router.message(F.text == "Ташкент")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=tashkent_menu_ru())


@router.message(F.text == "Андижан")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=andijan_menu_ru())


@router.message(F.text == "Карши")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=karshi_menu_ru())


@router.message(F.text == "Коканд")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=kokand_menu_ru())


@router.message(F.text == "Наманган")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=namangan_menu_ru())


@router.message(F.text == "Ташкентская область")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=tashkent_viloyat_menu_ru())


@router.message(F.text == "Нукус")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=nukus_menu_ru())


@router.message(F.text == "Самарканд")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=samarkand_viloyat_menu_ru())


@router.message(F.text == "Фергана")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=fergana_viloyat_menu_ru())


@router.message(F.text == "Шахрисабз")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=shahrisabz_menu_ru())


@router.message(F.text == "Навои")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=navoiy_menu_ru())


@router.message(F.text == "Ургенч")
async def show_filials(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=urgench_menu_ru())


@router.message(F.text == "Назад ↩️")
async def show_filials(message: types.Message):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-14_10-06-20.jpg?updatedAt=1752469592749"
    await message.answer_photo(photo=photo,
                               reply_markup=glavnye_vakansii_ru())


@router.message(F.text == "❌ Отмена ❌")
async def show_filials(message: types.Message):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-14_10-06-20.jpg?updatedAt=1752469592749"
    await message.answer_photo(photo=photo,
                               reply_markup=main_menu_ru())


@router.message(F.text == "⬅️ Ortga")
async def show_filials(message: types.Message):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-14_10-06-20.jpg?updatedAt=1752469592749"
    await message.answer_photo(photo=photo,
                               reply_markup=main_menu())
