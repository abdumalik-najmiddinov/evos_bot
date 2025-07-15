from aiogram import Router
from .users import (start, about_company, menu, news, contact_evos,
                    languange, branch, bosh_ish_orinlari, ariza_qoldirish, ariza_qoldirish_ru, bosh_ish_orinlari_ru)


def setup_message_routers():
    router = Router()
    router.include_router(start.router)
    router.include_router(about_company.router)
    router.include_router(menu.router)
    router.include_router(news.router)
    router.include_router(contact_evos.router)
    router.include_router(languange.router)
    router.include_router(branch.router)
    router.include_router(bosh_ish_orinlari.router)
    router.include_router(ariza_qoldirish.router)
    router.include_router(ariza_qoldirish_ru.router)
    router.include_router(bosh_ish_orinlari_ru.router)

    return router
