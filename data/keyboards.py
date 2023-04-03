from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Помощь")
b2 = KeyboardButton("Описание")
b3 = KeyboardButton("🎁Сюрприз🎁")
b4 = KeyboardButton("🚗Прогулка🚗")
b5 = KeyboardButton("♐️Совместимость♌️")
b6 = KeyboardButton("🍿Фильмы🎥")
kb_main.add(b1, b2).add(b3, b4).add(b5, b6)


ikb_tovars = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("⏪", callback_data="back"), InlineKeyboardButton("⏩", callback_data="forward")]
])

ikb_progul = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Москва", callback_data="moscow"), InlineKeyboardButton("СПБ", callback_data="saint")]
])

ikb_sex = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("🚹", callback_data="male"), InlineKeyboardButton("🚺", callback_data="female")]
])
