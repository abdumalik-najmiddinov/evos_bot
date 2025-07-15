from aiogram import Router, types, F
from keyboard.default import filial_ru, yaqin_filial_ru, tosheknt_filial_ru

router = Router()

# Rasm manzillari
about_photo = "https://ik.imagekit.io/h4yilyuyg/image_havas.jpg?updatedAt=1752482350554"
photo = "https://ik.imagekit.io/h4yilyuyg/image_ofis.jpg?updatedAt=1752482792446"

# 📍 Филиалы
@router.message(F.text.in_(["📍 Филиалы", "📍 Fililallar"]))
async def show_filials(message: types.Message):
    await message.answer_photo(
        photo=about_photo,
        caption=(
            "EVOS - крупнейшая фастфуд-компания в Узбекистане. "
            "На данный момент открыто более 70 торговых точек и современное многопрофильное производство.\n\n"
            "Сотрудники компании — это большая семья, которая развивается вместе и растет изо дня в день. "
            "Компания EVOS расширяется каждый день, сегодня нас более полутора тысяч. "
            "Стань частью нашей команды, добро пожаловать в семью EVOS!"
        ),
        reply_markup=filial_ru()
    )

@router.message(F.text == "📍 Fililallar")
async def show_filials(message: types.Message):
    await message.answer_photo(
        photo=about_photo,
        caption=(
            """EVOS - O'zbekistondagi eng yirik fastfud kompaniyasi. Ayni paytda 49 ta chakana savdo shoxobchasi va zamonaviy diversifikatsiyalangan ishlab chiqarish ochiq.

Kompaniya xodimlari birgalikda rivojlanib, kundan -kunga o'sib borayotgan katta oila. EVOS har kuni kengayib bormoqda, bugungi kunda bizda bir yarim mingdan ortiq odam bor. Bizning jamoamizga a'zo bo'ling, EVOS oilasiga xush kelibsiz!"""
        ),
        reply_markup=filial_uz()
    )

# 🏢 Головной офис
@router.message(F.text.in_(["🏢 Головной офис", "🏢 Bosh ofis"]))
async def show_main_office(message: types.Message):
    await message.answer_photo(
        photo=photo,
        caption="Адрес:  ул. Фурката 175, 1 подъезд, 4 этаж.\nОриентир: MAKRO THE TOWER"
    )
    await message.answer_location(latitude=41.302196, longitude=69.248867)

# ☕️ Показать ближайший филиал
@router.message(F.text.in_(["☕️ Показать ближайший филиал", "☕️ Yaqin filiallarni ko'rsatish"]))
async def request_user_location(message: types.Message):
    await message.answer(
        text="Отправьте свое местоположение для определения ближайшего филиала",
        reply_markup=yaqin_filial_ru()
    )

# г. Ташкент
@router.message(F.text.in_(["г. Ташкент", "Toshkent sh."]))
async def show_tashkent_filials(message: types.Message):
    await message.answer(
        text=message.text,
        reply_markup=tosheknt_filial_ru()
    )

# 📍 Алайский базар
@router.message(F.text.in_(["📍 Алайский базар", "📍 Oloy bozori"]))
async def show_oloy_branch(message: types.Message):
    photo_oloy = "https://ik.imagekit.io/h4yilyuyg/photo_oloy.jpg?updatedAt=1752484420852"
    await message.answer_photo(
        photo=photo_oloy,
        caption="Филиал: Алайский базар\n\nАдрес: просп. Амира Темура, 42\n\nКонтакты: +998 71 203 12 12"
    )
    await message.answer_location(latitude=41.32, longitude=69.282572)

# 📍 Малика
@router.message(F.text.in_(["📍 Малика", "📍 Malika"]))
async def show_malika_branch(message: types.Message):
    photo_malika = "https://ik.imagekit.io/h4yilyuyg/photo_malika.jpg?updatedAt=1752485030397"
    await message.answer_photo(
        photo=photo_malika,
        caption="Филиал: Малика\n\nАдрес: ул. Богиравон, 29\n\nКонтакты: +998 71 203 12 12"
    )
    await message.answer_location(latitude=41.342807, longitude=69.264684)

# 📍 Яхьё Гулямова, 94
@router.message(F.text.in_(["📍 Яхьё Гулямова, 94", "📍 Yahyo G'ulomov, 94"]))
async def show_gulomov_branch(message: types.Message):
    photo_gulomov = "https://ik.imagekit.io/h4yilyuyg/gulomova.jpg?updatedAt=1752485804512"
    await message.answer_photo(
        photo=photo_gulomov,
        caption="Филиал: улица Яхъё Гулямова, 94\n\nАдрес: улица Яхъё Гулямова, 94\n\nКонтакты: +998 71 203 12 12"
    )
    await message.answer_location(latitude=41.304758, longitude=69.284565)

# 📍 Samarqand Darvoza
@router.message(F.text.in_(["📍 Samarqand Darvoza", "📍 Самарканд Дарвоза"]))
async def show_samarqand_darvoza_branch(message: types.Message):
    photo_samarqand = "https://ik.imagekit.io/h4yilyuyg/gulomova.jpg?updatedAt=1752485804512"  # Agar boshqa rasm bo'lsa, almashtiring
    await message.answer_photo(
        photo=photo_samarqand,
        caption="Филиал: Самарканд Дарвоза\n\nАдрес: ул. Коратош, 5А\n\nКонтакты: +998 71 203 12 12"
    )
    await message.answer_location(latitude=41.304758, longitude=69.284565)
