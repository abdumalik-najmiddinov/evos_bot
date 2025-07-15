from aiogram.fsm.state import State, StatesGroup


class Conntact(StatesGroup):
    name = State()
    phone = State()
    info = State()


class ConntactRu(StatesGroup):
    name = State()
    phone = State()
    info = State()
