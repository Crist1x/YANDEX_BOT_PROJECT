from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("Помощь")
b2 = KeyboardButton("Описание")
b3 = KeyboardButton("🎁 Сюрприз 🎁")
b4 = KeyboardButton("🚗 Прогулка 🚗")
b5 = KeyboardButton("♐️ Совместимость ♌️")
b6 = KeyboardButton("💌 Комплимент 🎀")
b7 = KeyboardButton("🍿 Фильмы 🎥")
kb_main.add(b1, b2).add(b3, b4).add(b5, b6).add(b7)


ikb_tovars = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("⏪", callback_data="back"), InlineKeyboardButton("⏩", callback_data="forward")]
])

ikb_sights = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("🗺Показать на карте🗺", callback_data="geo")],
    [InlineKeyboardButton("⏪", callback_data="back_sight"), InlineKeyboardButton("⏩", callback_data="forward_sight")]
])

ikb_sights_SPB = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("🗺Показать на карте🗺", callback_data="geo_SPB")],
    [InlineKeyboardButton("⏪", callback_data="back_sight_SPB"), InlineKeyboardButton("⏩", callback_data="forward_sight_SPB")]
])

ikb_progul = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Москва", callback_data="moscow"), InlineKeyboardButton("СПБ", callback_data="saint")]
])

ikb_sex = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("🚹", callback_data="male"), InlineKeyboardButton("🚺", callback_data="female")]
])


ikb_komp = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("🚹", callback_data="komp_male"), InlineKeyboardButton("🚺", callback_data="komp_female")]
])

ikb_rem = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("❌Удалить Сообщение❌", callback_data="rem")]
])

ikb_films = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("⏪", callback_data="prev"), InlineKeyboardButton("⏩", callback_data="next")]
])