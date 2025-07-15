from aiogram import Router, types, F
from aiogram.filters import Command
from filters.users_chat import IsPrivate
from keyboard.default import main_menu

router = Router()
about_photo = "https://ik.imagekit.io/qve5v7bsa/photo_2024-11-23_12-31-53%20(2).jpg?updatedAt=1752467739055"


@router.message(F.text == "🏢 Kompaniya haqida")
async def bot_start(message: types.Message):
    await message.answer_photo(photo=about_photo,
                               caption="""EVOS ® tez xizmat ko'rsatish restoranlari tarmog'i bir joyda turmaydi, siz uchun va siz bilan doimo o'sib boradi va rivojlanadi! Biz geografiyamizni kengaytiramiz va deyarli har oyda yangi filiallarni ochamiz.
Endi bizning tarmog'imizning O'zbekiston bo'ylab 50 dan ortiq filiali mavjud. Biz doimo jamoamizning bir qismi bo'lishni xohlaydigan va EVOS ® da o'z faoliyatini boshlashga tayyor bo'lgan dinamik va faol odamlarni qidiramiz.
EVOS ® –  bu ishonchli brenddir. EVOS ® da ishlash – barqaror daromad va martaba istiqbollari kafolati.
EVOS ® da o'z karyerangizni boshlang!""")


# --------------------------------------
@router.message(F.text == "🏢 О компании")
async def bot_start(message: types.Message):
    await message.answer_photo(photo=about_photo,
                               caption="""Информация о компании:

Сеть ресторанов быстрого обслуживания EVOS® не стоит на месте, а постоянно растет и развивается вместе с вами и для вас! Мы расширяем свою географию и открываем новые филиалы практически каждый месяц. 
Сейчас в нашей сети насчитывается более 70 филиалов по всему Узбекистану. Поэтому мы всегда в поиске динамичных и активных людей, которые хотят стать частью нашей команды и готовы строить свою карьеру в EVOS®. 
EVOS® – это надежный бренд, которому доверяют. Работа в EVOS® – гарантия стабильного заработка и перспективы карьерного роста. 
Начни свою карьеру в EVOS® уже сейчас!""")




