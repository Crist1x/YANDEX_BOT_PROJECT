from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Помощь")
b2 = KeyboardButton("Описание")
b3 = KeyboardButton("🎁Сюрприз🎁")
b4 = KeyboardButton("🚗Прогулка🚗")
kb_main.add(b1, b2).add(b3).add(b4)


ikb_tovars = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("⏪", callback_data="back"), InlineKeyboardButton("⏩", callback_data="forward")]
])

ikb_progul = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Москва", callback_data="moscow"), InlineKeyboardButton("СПБ", callback_data="saint")]
])
