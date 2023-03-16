from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Помощь")
b2 = KeyboardButton("Описание")
b3 = KeyboardButton("🎁Сюрприз🎁")
b4 = KeyboardButton("🚗Прогулка🚗")
kb.add(b1, b2).add(b3).add(b4)

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("⏪", callback_data="back"), InlineKeyboardButton("⏩", callback_data="forward")]
])