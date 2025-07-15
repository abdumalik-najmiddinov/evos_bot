from aiogram import Router, types, F
from aiogram.filters import Text, StateFilter
from aiogram.fsm.context import FSMContext
from states.user import ConntactRu
from keyboard.default import glavnye_vakansii_ru, main_menu_ru

router = Router()



@router.message(F.text == "Универсальный сотрудник")
async def start_universal(message: types.Message, state: FSMContext):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-15_15-52-45.jpg?updatedAt=1752576905446"
    await message.answer_photo(photo=photo, caption="Пожалуйста, введите ваше имя:")
    await state.set_state(ConntactRu.name)
    # Agar kerak bo'lsa reply_markup ni shu yerda berish mumkin, hozir FSM bosqichi uchun oddiy

@router.message(F.text == "Оператор колл-центра")
async def start_call_center(message: types.Message, state: FSMContext):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-15_15-52-45.jpg?updatedAt=1752576905446"
    await message.answer_photo(photo=photo, caption="Пожалуйста, введите ваше имя:")
    await state.set_state(ConntactRu.name)

@router.message(F.text == "Курьер")
async def start_courier(message: types.Message, state: FSMContext):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-15_15-52-45.jpg?updatedAt=1752576905446"
    await message.answer_photo(photo=photo, caption="Пожалуйста, введите ваше имя:")
    await state.set_state(ConntactRu.name)


@router.message(ConntactRu.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите номер телефона:")
    await state.set_state(ConntactRu.phone)

@router.message(ConntactRu.phone)
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Введите дополнительную информацию:")
    await state.set_state(ConntactRu.info)

@router.message(ConntactRu.info)
async def process_info(message: types.Message, state: FSMContext):
    await state.update_data(info=message.text)

    data = await state.get_data()
    name = data.get("name")
    phone = data.get("phone")
    info = data.get("info")
    await message.answer(
        f"✅ Информация принята:\n\n"
        f"👤 Имя: {name}\n"
        f"📞 Телефон: {phone}\n"
        f"📝 Доп. информация: {info}\n\n"
        f"⏳ Наши администраторы свяжутся с вами в течение 24-48 часов! 🤝"
    )
    await state.clear()




@router.message(F.text == "Универсальный сотрудник")
async def start_universal(message: types.Message, state: FSMContext):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-15_15-52-45.jpg?updatedAt=1752576905446"
    await message.answer_photo(photo=photo, caption="Пожалуйста, введите ваше имя:")
    await state.set_state(ConntactRu.name)

@router.message(F.text == "Оператор колл-центра")
async def start_call_center(message: types.Message, state: FSMContext):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-15_15-52-45.jpg?updatedAt=1752576905446"
    await message.answer_photo(photo=photo, caption="Пожалуйста, введите ваше имя:")
    await state.set_state(ConntactRu.name)

@router.message(F.text == "Курьер")
async def start_courier(message: types.Message, state: FSMContext):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-15_15-52-45.jpg?updatedAt=1752576905446"
    await message.answer_photo(photo=photo, caption="Пожалуйста, введите ваше имя:")
    await state.set_state(ConntactRu.name)


@router.message(ConntactRu.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите номер телефона:")
    await state.set_state(ConntactRu.phone)

@router.message(ConntactRu.phone)
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Введите дополнительную информацию:")
    await state.set_state(ConntactRu.info)

@router.message(ConntactRu.info)
async def process_info(message: types.Message, state: FSMContext):
    await state.update_data(info=message.text)

    data = await state.get_data()
    name = data.get("name")
    phone = data.get("phone")
    info = data.get("info")
    await message.answer(
        f"✅ Информация принята:\n\n"
        f"👤 Имя: {name}\n"
        f"📞 Телефон: {phone}\n"
        f"📝 Доп. информация: {info}\n\n"
        f"⏳ Наши администраторы свяжутся с вами в течение 24-48 часов! 🤝"
    )
    await state.clear()




