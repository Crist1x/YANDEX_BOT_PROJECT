from aiogram.dispatcher.filters.state import StatesGroup, State


class Female(StatesGroup):
    fem = State()
    male = State()


class Male(StatesGroup):
    male = State()
    fem = State()