from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from states.user import Conntact
router = Router()


@router.message(F.text == "Universal xodim")
async def start_form(message: types.Message, state: FSMContext):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-15_15-52-45.jpg?updatedAt=1752576905446"
    await message.answer_photo(photo=photo, caption="Iltimos, ismingizni kiriting:")
    await state.set_state(Conntact.name)

@router.message(Conntact.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Telefon raqamingizni kiriting:")
    await state.set_state(Conntact.phone)

@router.message(Conntact.phone)
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Qo‘shimcha ma'lumot kiriting:")
    await state.set_state(Conntact.info)

@router.message(Conntact.info)
async def process_info(message: types.Message, state: FSMContext):
    await state.update_data(info=message.text)

    data = await state.get_data()
    name = data.get("name")
    phone = data.get("phone")
    info = data.get("info")
    await message.answer(
        f"✅ Malumotlar qabul qilindi:\n\n"
        f"👤 Ism: {name}\n"
        f"📞 Telefon: {phone}\n"
        f"📝 Ma'lumot: {info}\n\n"
        f"⏳ Siz bilan administratorlarimiz 24-48 soat davomida bog‘lanishadi! 🤝"
    )

    await state.clear()






@router.message(F.text == "Call-markaz operatori")
async def start_form(message: types.Message, state: FSMContext):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-15_15-52-45.jpg?updatedAt=1752576905446"
    await message.answer_photo(photo=photo, caption="Iltimos, ismingizni kiriting:")
    await state.set_state(Conntact.name)

@router.message(Conntact.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Telefon raqamingizni kiriting:")
    await state.set_state(Conntact.phone)

@router.message(Conntact.phone)
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Qo‘shimcha ma'lumot kiriting:")
    await state.set_state(Conntact.info)

@router.message(Conntact.info)
async def process_info(message: types.Message, state: FSMContext):
    await state.update_data(info=message.text)

    data = await state.get_data()
    name = data.get("name")
    phone = data.get("phone")
    info = data.get("info")
    await message.answer(
        f"✅ Malumotlar qabul qilindi:\n\n"
        f"👤 Ism: {name}\n"
        f"📞 Telefon: {phone}\n"
        f"📝 Ma'lumot: {info}\n\n"
        f"⏳ Siz bilan administratorlarimiz 24-48 soat davomida bog‘lanishadi! 🤝"
    )

    await state.clear()




@router.message(F.text == "Kuryer")
async def start_form(message: types.Message, state: FSMContext):
    photo = "https://ik.imagekit.io/h4yilyuyg/photo_2025-07-15_15-52-45.jpg?updatedAt=1752576905446"
    await message.answer_photo(photo=photo, caption="Iltimos, ismingizni kiriting:")
    await state.set_state(Conntact.name)

@router.message(Conntact.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Telefon raqamingizni kiriting:")
    await state.set_state(Conntact.phone)

@router.message(Conntact.phone)
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Qo‘shimcha ma'lumot kiriting:")
    await state.set_state(Conntact.info)

@router.message(Conntact.info)
async def process_info(message: types.Message, state: FSMContext):
    await state.update_data(info=message.text)

    data = await state.get_data()
    name = data.get("name")
    phone = data.get("phone")
    info = data.get("info")
    await message.answer(
        f"✅ Malumotlar qabul qilindi:\n\n"
        f"👤 Ism: {name}\n"
        f"📞 Telefon: {phone}\n"
        f"📝 Ma'lumot: {info}\n\n"
        f"⏳ Siz bilan administratorlarimiz 24-48 soat davomida bog‘lanishadi! 🤝"
    )

    await state.clear()
