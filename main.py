from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types.input_media import InputMedia
from data.config import TOKEN_API, GREETING_STICKER, HELP, DESCR, HEADERS, STUFF
from data.keyboards import kb, ikb

import requests
import json
import random

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
random.shuffle(STUFF)
tovar_pos = 0
async def on_startup(_):
    print("Я был запущен")


def tovar_generator(tovar_pos):
    data = requests.get(STUFF[tovar_pos][0], headers=HEADERS).json()
    with open('db/stuff_info.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    total_list = []
    with open("db/stuff_info.json", "r", encoding='UTF-8') as file:
        data = json.load(file)["data"]["products"][0]
        total_list.append(data["name"])
        total_list.append(str(int(data["salePriceU"]) // 100))
        total_list.append(data["id"])
        total_list.append(data["rating"])
        total_list.append(data["feedbacks"])

    return f"""<b>Название:</b> {total_list[0]}.
<b>Цена:</b> {total_list[1]} руб.
<b>Ссылка на ВБ:</b> https://www.wildberries.ru/catalog/{total_list[2]}/detail.aspx.
<b>Рейтинг:</b> {total_list[3]}/5
<b>Количество оценок:</b> {total_list[4]} шт"""


@dp.message_handler(Text(equals="🎁Сюрприз🎁"))
async def surp_func(message: types.Message):
    global tovar_pos
    tovar = tovar_generator(tovar_pos)
    await bot.send_photo(chat_id=message.chat.id,
                         photo=STUFF[tovar_pos][1],
                         caption=tovar,
                         parse_mode="HTML",
                         reply_markup=ikb)


# Кнопка Описание
@dp.message_handler(Text(equals="Описание"))
async def desc_func(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=DESCR)


# Кнопка Помощь
@dp.message_handler(Text(equals="Помощь"))
async def help_func(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP)


# Запуск Бота
@dp.message_handler(commands=["start"])
async def strat_func(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Приветствую! Если ты попал в нашего бота, значит ты очень\
                                 хочешь порадовать свою половинку. Не переживай, мы поможем тебе в этом😊",
                           reply_markup=kb)
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=GREETING_STICKER)
    await message.delete()


@dp.callback_query_handler()
async def ikb_cb_handler(callback: types.CallbackQuery):
    global tovar_pos
    if callback.data == "back":
        if tovar_pos != 0:
            tovar_pos -= 1
            capt = tovar_generator(tovar_pos)
            file = InputMedia(media=STUFF[tovar_pos][1], caption=capt, parse_mode="HTML")
            await callback.message.edit_media(file, reply_markup=ikb)
        else:
            await callback.answer("Это первый товар в нашей подборке")
    else:
        if tovar_pos != len(STUFF) - 1:
            tovar_pos += 1
            capt = tovar_generator(tovar_pos)
            file = InputMedia(media=STUFF[tovar_pos][1], caption=capt, parse_mode="HTML")
            await callback.message.edit_media(file, reply_markup=ikb)
        else:
            await callback.answer("Это последний товар в нашей подборке")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
