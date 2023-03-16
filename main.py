from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from data.config import TOKEN_API, GREETING_STICKER, HELP, DESCR, HEADERS, STUFF
from data.keyboards import kb

import requests
import json
import random

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print("Я был запущен")


@dp.message_handler(Text(equals="🎁Сюрприз🎁"))
async def surp_func(message: types.Message):
    links_list = STUFF[random.choice(list(STUFF.keys()))]
    data = requests.get(links_list[0], headers=HEADERS).json()
    with open('db/stuff_info.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        print(f'Данные сохранены в db/stuff_info.json')

    total_list = []
    with open("db/stuff_info.json", "r", encoding='UTF-8') as file:
        data = json.load(file)["data"]["products"][0]
        total_list.append(data["name"])
        total_list.append(str(int(data["salePriceU"]) // 100))
        total_list.append(data["id"])
        total_list.append(data["rating"])
        total_list.append(data["feedbacks"])

    tovar = f"""<b>Название:</b> {total_list[0]}.
<b>Цена:</b> {total_list[1]} руб.
<b>Ссылка на ВБ:</b> https://www.wildberries.ru/catalog/{total_list[2]}/detail.aspx.
<b>Рейтинг:</b> {total_list[3]}/5
<b>Количество оценок:</b> {total_list[4]} шт"""

    await bot.send_photo(chat_id=message.chat.id,
                         photo=links_list[1],
                         caption=tovar,
                         parse_mode="HTML")


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


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
