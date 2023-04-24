from data.imports import *

bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=MemoryStorage())
tovar_pos = 0
male_zodiak = ""
female_zodiak = ""
id_walk = [a for a in range(1, 18)]
index_pos_walk = 0
id_f = 0


# Генерация текста товара
def tovar_generator(position):
    data = requests.get(STUFF[position][0], headers=HEADERS).json()
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


# Генерация текста гороскопа
def goroscop(zodf, zodm):
    try:
        data = requests.get(f"https://my-calend.ru/zodiak-sovmestimost/zhenshchina-{ZODIAKS[zodf]}-muzhchina-"
                            f"{ZODIAKS[zodm]}", headers=HEADERS).content.decode("utf-8")
        soup = bs(data, "html.parser")
        main_info = soup.find_all("h2")
        total = ""
        for obj in main_info:
            if main_info.index(obj) == 0:
                total += f"❤️‍🔥 {obj.text} ❤️‍🔥\n"
            elif main_info.index(obj) == 1:
                total += f"👥 {obj.text} 👥\n"
            else:
                total += f"💵 {obj.text} 💵\n"
        return total

    except Exception as e:
        return "Мы не смогли найти информацию про вашу совместимость. Скорее всего вы указали неправильно один из " \
               "знаков зодиака. Попробуйте еще раз💗 "


# Генерация комплимента девушке
def female_kompliment(komp_index):
    sqlite_connection = sqlite3.connect('db/database.db')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from Compliments"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    return records[komp_index][1]


# Генерация комплимента парню
def male_kompliment(komp_index):
    sqlite_connection = sqlite3.connect('db/database.db')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from Compliments"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    return records[komp_index][2]


# Генерация всего на свете для прогулки
def all_for_walk(walker_id):
    sqlite_connection = sqlite3.connect('db/database.db')
    cursor = sqlite_connection.cursor()
    result = cursor.execute("""SELECT * FROM Sights WHERE id = ?""", (walker_id,)).fetchall()
    return result


def all_for_walk_spb(walker_id):
    sqlite_connection = sqlite3.connect('db/database.db')
    cursor = sqlite_connection.cursor()
    result = cursor.execute("""SELECT * FROM SPB_Sights WHERE id = ?""", (walker_id,)).fetchall()
    return result


def film_generator(film_id):
    data = requests.get("https://www.kp.ru/afisha/msk/obzory/kino/luchshie-filmy-pro-lyubov/", headers=HEADERS).content.decode("utf-8")
    soup = bs(data, "html.parser")
    all_params = []
    names = []
    descript = []
    links = []
    for ul in soup.find('div', class_="event_content-area").find_all("ul"):
        for li in bs(str(ul), "html.parser").find_all("li"):
            all_params.append(li.text)
    for name in soup.find_all("h3", class_="wp-block-heading"):
        names.append(name.text.split(". ")[1].replace("«", "").replace("»", ""))
    for des1 in soup.find("div", class_="event_content-area").find_all("p"):
        descript.append(des1.text)
    for link in soup.find_all("div", class_="wp-block-embed__wrapper"):
        for yt in bs(str(link), "html.parser").find_all("iframe"):
            links.append(str(yt).split("src=\"")[1].split("\"")[0])
    a = []
    for x in links:
        if x not in a:
            a.append(x)

    links = a

    total = f"""<b>Название:</b> {names[film_id]}    
<b>{all_params[film_id + film_id * 2].split(":")[0]}:</b> {all_params[film_id + film_id * 2].split(":")[1]}
<b>{all_params[film_id + film_id * 2 + 1].split(":")[0]}:</b> {all_params[film_id + film_id * 2 + 1].split(":")[1]}
<b>{all_params[film_id + film_id * 2 + 2].split(":")[0]}:</b> {all_params[film_id + film_id * 2 + 2].split(":")[1]}
<b>Описание:</b> {descript[film_id]}
<b>Трейлер:</b> {links[film_id]}
"""
    return total


async def on_startup(_):
    print("Я был запущен")


# Кнопка Совместимость
@dp.message_handler(Text(equals=["♐️ Совместимость ♌️", "совместимость", "Совместимость"]))
async def progul_func(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Выберите ваш пол:",
                           reply_markup=ikb_sex)


# Кнопка Комплимент
@dp.message_handler(Text(equals=["💌 Комплимент 🎀", "комплимент", "Комплимент"]))
async def compliment_func(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Выбери пол человека, для которого хотите получить комплимент🌹",
                           reply_markup=ikb_komp)


# Кнопка Прогулка
@dp.message_handler(Text(equals=["🚗 Прогулка 🚗", "прогулка", "Прогулка"]))
async def progul_func(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Выбери город, в котором ты сейчас находишься🏢",
                           reply_markup=ikb_progul)


# Кнопка Сюрприз
@dp.message_handler(Text(equals=["🎁 Сюрприз 🎁", "сюрприз", "Сюрприз"]))
async def surp_func(message: types.Message):
    global tovar_pos
    random.shuffle(STUFF)
    tovar = tovar_generator(tovar_pos)
    await bot.send_photo(chat_id=message.chat.id,
                         photo=STUFF[tovar_pos][1],
                         caption=tovar,
                         parse_mode="HTML",
                         reply_markup=ikb_tovars)


# Кнопка Фильмы
@dp.message_handler(Text(equals=["🍿 Фильмы 🎥", "фильмы", "Фильмы"]))
async def films_func(message: types.Message):
    global id_f
    id_f = 0
    await bot.send_message(chat_id=message.from_user.id,
                           text=film_generator(id_f),
                           parse_mode="HTML",
                           reply_markup=ikb_films)


# Кнопка Описание
@dp.message_handler(Text(equals=["Описание", "описание"]))
async def desc_func(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=DESCR,
                           parse_mode="HTML")


# Кнопка Помощь
@dp.message_handler(Text(equals=["Помощь", "помощь"]))
async def help_func(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP,
                           parse_mode="HTML")


# Запуск Бота
@dp.message_handler(commands=["start"])
async def start_func(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Приветствую! \nЕсли ты попал в нашего бота, значит ты очень хочешь порадовать "
                                f"свою половинку. Не переживай, мы поможем тебе в этом😊",
                           reply_markup=kb_main)
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=GREETING_STICKER)
    await message.delete()


# Колбек кнопки назад (у товара)
@dp.callback_query_handler(text="back")
async def tovar0(callback: types.CallbackQuery):
    global tovar_pos
    if callback.data == "back":
        if tovar_pos != 0:
            tovar_pos -= 1
            capt = tovar_generator(tovar_pos)
            file = InputMedia(media=STUFF[tovar_pos][1], caption=capt, parse_mode="HTML")
            await callback.message.edit_media(file, reply_markup=ikb_tovars)
        else:
            await callback.answer("Это первый товар в нашей подборке")


# Колбек кнопки вперед (у товара)
@dp.callback_query_handler(text="forward")
async def tovar1(callback: types.CallbackQuery):
    global tovar_pos
    if tovar_pos != len(STUFF) - 1:
        tovar_pos += 1
        capt = tovar_generator(tovar_pos)
        file = InputMedia(media=STUFF[tovar_pos][1], caption=capt, parse_mode="HTML")
        await callback.message.edit_media(file, reply_markup=ikb_tovars)
    else:
        await callback.answer("Это последний товар в нашей подборке")


# Колбек москвы (у прогулки)
@dp.callback_query_handler(text="moscow")
async def moscow_city(callback: types.CallbackQuery):
    global id_walk, index_pos_walk
    random.shuffle(id_walk)
    place_from_bd = all_for_walk(id_walk[index_pos_walk])
    capt = f"""<b>{place_from_bd[0][1]}</b>
{place_from_bd[0][2]}
Подробнее: {place_from_bd[0][6]}"""
    await bot.send_photo(chat_id=callback.from_user.id,
                         photo=place_from_bd[0][5],
                         caption=capt,
                         parse_mode="HTML",
                         reply_markup=ikb_sights)
    await callback.message.delete()


# Колбек Москвы на нажатие back_sight
@dp.callback_query_handler(text="back_sight")
async def mos_back_sight(callback: types.CallbackQuery):
    global id_walk, index_pos_walk
    if index_pos_walk - 1 >= 0:
        index_pos_walk -= 1
        place_from_bd = all_for_walk(id_walk[index_pos_walk])
        capt = f"""<b>{place_from_bd[0][1]}</b>
    {place_from_bd[0][2]}
    Подробнее: {place_from_bd[0][6]}"""
        file = InputMedia(media=place_from_bd[0][5], caption=capt, parse_mode="HTML")
        await callback.message.edit_media(file, reply_markup=ikb_sights)
    else:
        await callback.answer("Это первое место в нашей подборке")


# Колбек Москвы на нажатие forward_sight
@dp.callback_query_handler(text="forward_sight")
async def mos_forward_sight(callback: types.CallbackQuery):
    global id_walk, index_pos_walk
    if index_pos_walk + 1 <= 16:
        index_pos_walk += 1
        place_from_bd = all_for_walk(id_walk[index_pos_walk])
        capt = f"""<b>{place_from_bd[0][1]}</b>
    {place_from_bd[0][2]}
    Подробнее: {place_from_bd[0][6]}"""
        file = InputMedia(media=place_from_bd[0][5], caption=capt, parse_mode="HTML")
        await callback.message.edit_media(file, reply_markup=ikb_sights)
    else:
        await callback.answer("Это последнее место в нашей подборке")


# Колбек геопозиции
@dp.callback_query_handler(text="geo")
async def geoposition(callback: types.CallbackQuery):
    place_from_bd = all_for_walk(id_walk[index_pos_walk])
    lat = place_from_bd[0][3]
    long = place_from_bd[0][4]
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=lat,
                            longitude=long,
                            reply_markup=ikb_rem)


# Удаление геолокации
@dp.callback_query_handler(text="rem")
async def saint_city(callback: types.CallbackQuery):
    await callback.message.delete()


# Колбек питера (у прогулки)
@dp.callback_query_handler(text="saint")
async def saint_city(callback: types.CallbackQuery):
    global id_walk, index_pos_walk
    random.shuffle(id_walk)
    place_from_bd = all_for_walk_spb(id_walk[index_pos_walk])
    capt = f"""<b>{place_from_bd[0][1]}</b>
    {place_from_bd[0][2]}
    Подробнее: {place_from_bd[0][6]}"""
    await bot.send_photo(chat_id=callback.from_user.id,
                         photo=place_from_bd[0][5],
                         caption=capt,
                         parse_mode="HTML",
                         reply_markup=ikb_sights_SPB)
    await callback.message.delete()


# Колбек СПБ на нажатие back_sight_SPB
@dp.callback_query_handler(text="back_sight_SPB")
async def mos_back_sight(callback: types.CallbackQuery):
    global id_walk, index_pos_walk
    if index_pos_walk - 1 >= 0:
        index_pos_walk -= 1
        place_from_bd = all_for_walk_spb(id_walk[index_pos_walk])
        capt = f"""<b>{place_from_bd[0][1]}</b>
    {place_from_bd[0][2]}
    Подробнее: {place_from_bd[0][6]}"""
        file = InputMedia(media=place_from_bd[0][5], caption=capt, parse_mode="HTML")
        await callback.message.edit_media(file, reply_markup=ikb_sights_SPB)
    else:
        await callback.answer("Это первое место в нашей подборке")


# Колбек СПБ на нажатие forward_sight_SPB
@dp.callback_query_handler(text="forward_sight_SPB")
async def mos_forward_sight(callback: types.CallbackQuery):
    global id_walk, index_pos_walk
    if index_pos_walk + 1 <= 16:
        index_pos_walk += 1
        place_from_bd = all_for_walk_spb(id_walk[index_pos_walk])
        capt = f"""<b>{place_from_bd[0][1]}</b>
    {place_from_bd[0][2]}
    Подробнее: {place_from_bd[0][6]}"""
        file = InputMedia(media=place_from_bd[0][5], caption=capt, parse_mode="HTML")
        await callback.message.edit_media(file, reply_markup=ikb_sights_SPB)
    else:
        await callback.answer("Это последнее место в нашей подборке")


# Колбек геопозиции SPB
@dp.callback_query_handler(text="geo_SPB")
async def geoposition_spb(callback: types.CallbackQuery):
    place_from_bd = all_for_walk_spb(id_walk[index_pos_walk])
    lat = place_from_bd[0][3]
    long = place_from_bd[0][4]
    await bot.send_location(chat_id=callback.from_user.id,
                            latitude=lat,
                            longitude=long,
                            reply_markup=ikb_rem)


# Колбек комплимента для мужчины
@dp.callback_query_handler(text="komp_male")
async def saint_city(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id,
                           text=male_kompliment(random.randint(1, 30)))
    await callback.message.delete()


# Колбек комплимента для девушки
@dp.callback_query_handler(text="komp_female")
async def saint_city(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id,
                           text=female_kompliment(random.randint(1, 30)))
    await callback.message.delete()


# Колбек мужского пола (совместимость)
@dp.callback_query_handler(text="male")
async def male_func(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id,
                           text="Напишите ваш знак зодиака")
    await Male.male.set()


# Колбек женского пола (совместимость)
@dp.callback_query_handler(text="female")
async def female_func(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id,
                           text="Напишите ваш знак зодиака")
    await Female.fem.set()


# Колбек назад фильмы
@dp.callback_query_handler(text="prev")
async def prev_film_func(callback: types.CallbackQuery):
    global id_f
    if id_f != 0:
        id_f -= 1
        await callback.message.edit_text(text=film_generator(id_f),
                                         parse_mode="HTML",
                                         reply_markup=ikb_films)
    else:
        await callback.answer("Это первый фильм в нашем списке")


# Колбек вперед фильмы
@dp.callback_query_handler(text="next")
async def next_film_func(callback: types.CallbackQuery):
    global id_f
    if id_f != 29:
        id_f += 1
        await callback.message.edit_text(text=film_generator(id_f),
                                         parse_mode="HTML",
                                         reply_markup=ikb_films)
    else:
        await callback.answer("Это послледний фильм в нашем списке")


# Обработчик машины состояний
@dp.message_handler(state=Male.male)
async def fem_zod(message: types.Message, state: FSMContext):
    await state.update_data(male_zod=message.text)
    await message.answer("Отлично! Теперь введите зодиак вашего партнера.")
    await Male.next()


# Обработчик машины состояний
@dp.message_handler(state=Male.fem)
async def get_address(message: types.Message, state: FSMContext):
    global male_zodiak, female_zodiak
    await state.update_data(female_zod=message.text)
    data = await state.get_data()
    male_zodiak, female_zodiak = data["male_zod"].lower(), data["female_zod"].lower()
    await message.answer("Подождите, мы подсчитываем совместимость💋")
    time.sleep(1)
    await bot.send_message(chat_id=message.chat.id,
                           text=goroscop(female_zodiak, male_zodiak))
    await state.finish()


# Обработчик машины состояний
@dp.message_handler(state=Female.fem)
async def fem_zod(message: types.Message, state: FSMContext):
    await state.update_data(female_zod=message.text)
    await message.answer("Отлично! Теперь введите зодиак вашего партнера.")
    await Female.next()


# Обработчик машины состояний
@dp.message_handler(state=Female.male)
async def get_address(message: types.Message, state: FSMContext):
    global male_zodiak, female_zodiak
    await state.update_data(male_zod=message.text)
    data = await state.get_data()
    male_zodiak, female_zodiak = data["male_zod"].lower(), data["female_zod"].lower()
    await message.answer("Подождите, мы подсчитываем совместимость💋")
    time.sleep(1)
    await bot.send_message(chat_id=message.chat.id,
                           text=goroscop(female_zodiak, male_zodiak))
    await state.finish()


# Общий обработчик сообщений
@dp.message_handler()
async def start_func(message: types.Message):
    if 'день' in message.text.lower() or 'число' in message.text.lower() \
            or 'сегодня' in message.text.lower() or 'недел' in message.text.lower():
        date_today = dt.datetime.now().strftime('%A %d-%B-%Y')
        now_time = dt.datetime.now().time()
        # зима выходной день разное время
        if ('Sunday' in date_today or 'Saturday' in date_today) and \
                ('December' in date_today or 'January' in date_today or 'February' in date_today) and \
                (dt.time(6) >= now_time >= dt.time(0)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Зимняя выходная ночь \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' in date_today or 'Saturday' in date_today) and \
                ('December' in date_today or 'January' in date_today or 'February' in date_today) and \
                (dt.time(6) <= now_time <= dt.time(12)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Зимнее выходное утро \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' in date_today or 'Saturday' in date_today) and \
                ('December' in date_today or 'January' in date_today or 'February' in date_today) and \
                (dt.time(12) <= now_time <= dt.time(18)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Зимний выходной день \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' in date_today or 'Saturday' in date_today) and \
                ('December' in date_today or 'January' in date_today or 'February' in date_today) and \
                (dt.time(18) <= now_time <= dt.time(23, 59)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Зимний выходной вечер  \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        # лето выходной день разное время
        elif ('Sunday' in date_today or 'Saturday' in date_today) and \
                ('July' in date_today or 'June' in date_today or 'August' in date_today) and \
                (dt.time(6) >= now_time >= dt.time(0)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Летняя выходная ночь \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' in date_today or 'Saturday' in date_today) and \
                ('July' in date_today or 'June' in date_today or 'August' in date_today) and \
                (dt.time(6) <= now_time <= dt.time(12)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Летнее выходное утро \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' in date_today or 'Saturday' in date_today) and \
                ('July' in date_today or 'June' in date_today or 'August' in date_today) and \
                (dt.time(12) <= now_time <= dt.time(18)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Летний выходной день \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' in date_today or 'Saturday' in date_today) and \
                ('July' in date_today or 'June' in date_today or 'August' in date_today) and \
                (dt.time(18) <= now_time <= dt.time(23, 59)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Летний выходной вечер  \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        # весна выходной день разное время
        elif ('Sunday' in date_today or 'Saturday' in date_today) and \
             ('May' in date_today or 'March' in date_today or 'April' in date_today) and \
             (dt.time(6) >= now_time >= dt.time(0)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Весенняя выходная ночь \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' in date_today or 'Saturday' in date_today) and \
                ('May' in date_today or 'March' in date_today or 'April' in date_today) and \
                (dt.time(6) <= now_time <= dt.time(12)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Весеннее выходное утро \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' in date_today or 'Saturday' in date_today) and \
                ('May' in date_today or 'March' in date_today or 'April' in date_today) and \
                (dt.time(12) <= now_time <= dt.time(18)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Весенний выходной день \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' in date_today or 'Saturday' in date_today) and \
                ('May' in date_today or 'March' in date_today or 'April' in date_today) and \
                (dt.time(18) <= now_time <= dt.time(23, 59)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Весенний выходной вечер  \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        # осень выходной день разное время
        elif ('Sunday' in date_today or 'Saturday' in date_today) and \
             ('September' in date_today or 'October' in date_today or 'November' in date_today) and \
             (dt.time(6) >= now_time >= dt.time(0)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Осенняя выходная ночь \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' in date_today or 'Saturday' in date_today) and \
                ('September' in date_today or 'October' in date_today or 'November' in date_today) and \
                (dt.time(6) <= now_time <= dt.time(12)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Осеннее выходное утро \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' in date_today or 'Saturday' in date_today) and \
                ('September' in date_today or 'October' in date_today or 'November' in date_today) and \
                (dt.time(12) <= now_time <= dt.time(18)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Осенний выходной день \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' in date_today or 'Saturday' in date_today) and \
                ('September' in date_today or 'October' in date_today or 'November' in date_today) and \
                (dt.time(18) <= now_time <= dt.time(23, 59)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Осенний выходной вечер  \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        # зима будний день разное время
        elif ('Sunday' not in date_today or 'Saturday' not in date_today) and \
                ('December' in date_today or 'January' in date_today or 'February' in date_today) and \
                (dt.time(6) >= now_time >= dt.time(0)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Зимняя будняя ночь  \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' not in date_today or 'Saturday' not in date_today) and \
                ('December' in date_today or 'January' in date_today or 'February' in date_today) and \
                (dt.time(6) <= now_time <= dt.time(12)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Зимнее буднее утро \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' not in date_today or 'Saturday' not in date_today) and \
                ('December' in date_today or 'January' in date_today or 'February' in date_today) and \
                (dt.time(12) <= now_time <= dt.time(18)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Зимний будний день  \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' not in date_today or 'Saturday' not in date_today) and \
                ('December' in date_today or 'January' in date_today or 'February' in date_today) and \
                (dt.time(18) <= now_time <= dt.time(23, 59)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Зимний будний вечер  \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        # лето будний день разное время
        elif ('Sunday' not in date_today or 'Saturday' not in date_today) and \
                ('July' in date_today or 'June' in date_today or 'August' in date_today) and \
                (dt.time(6) >= now_time >= dt.time(0)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Летняя будняя ночь  \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' not in date_today or 'Saturday' not in date_today) and \
                ('July' in date_today or 'June' in date_today or 'August' in date_today) and \
                (dt.time(6) <= now_time <= dt.time(12)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Летнее буднее утро  \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' not in date_today or 'Saturday' not in date_today) and \
                ('July' in date_today or 'June' in date_today or 'August' in date_today) and \
                (dt.time(12) <= now_time <= dt.time(18)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Летний будний день  \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' not in date_today or 'Saturday' not in date_today) and \
                ('July' in date_today or 'June' in date_today or 'August' in date_today) and \
                (dt.time(18) <= now_time <= dt.time(23, 59)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Летний будний вечер  \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        # весна будний день разное время
        elif ('Sunday' not in date_today or 'Saturday' not in date_today) and \
                ('May' in date_today or 'March' in date_today or 'April' in date_today) and \
                (dt.time(6) >= now_time >= dt.time(0)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Весенняя будняя ночь  \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' not in date_today or 'Saturday' not in date_today) and \
                ('May' in date_today or 'March' in date_today or 'April' in date_today) and \
                (dt.time(6) <= now_time <= dt.time(12)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Весеннее буднее утро  \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' not in date_today or 'Saturday' not in date_today) and \
                ('May' in date_today or 'March' in date_today or 'April' in date_today) and \
                (dt.time(12) <= now_time <= dt.time(18)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Весенний будний день \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' not in date_today or 'Saturday' not in date_today) and \
                ('May' in date_today or 'March' in date_today or 'April' in date_today) and \
                (dt.time(18) <= now_time <= dt.time(23, 59)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Весенний будний вечер  \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        # осень будний день разное время
        elif ('Sunday' not in date_today or 'Saturday' not in date_today) and \
                ('September' in date_today or 'October' in date_today or 'November' in date_today) and \
                (dt.time(6) >= now_time >= dt.time(0)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Осенняя будняя ночь \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' not in date_today or 'Saturday' not in date_today) and \
                ('September' in date_today or 'October' in date_today or 'November' in date_today) and \
                (dt.time(6) <= now_time <= dt.time(12)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Осеннее буднее утро \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' not in date_today or 'Saturday' not in date_today) and \
                ('September' in date_today or 'October' in date_today or 'November' in date_today) and \
                (dt.time(12) <= now_time <= dt.time(18)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Осенний будний день \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )
        elif ('Sunday' not in date_today or 'Saturday' not in date_today) and \
                ('September' in date_today or 'October' in date_today or 'November' in date_today) and \
                (dt.time(18) <= now_time <= dt.time(23, 59)):
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Осенний будний вечер  \n {dt.datetime.now().strftime('%A %d-%B-%Y')}",
                                   )

    elif 'не' in message.text.lower():
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Мы ничего не поняли, попробуйте еще раз.",
                               )
    elif 'хорош' in message.text.lower():
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Мы рады за Вас! Всё что хорошо, никогда не бывает плохо.",
                               )
    elif 'крут' in message.text.lower():
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Мы рады за Вас! Всё что хорошо, никогда не бывает плохо.",
                               )
    elif 'отличн' in message.text.lower():
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Мы рады за Вас! Всё что хорошо, никогда не бывает плохо.",
                               )
    elif 'прекрасн' in message.text.lower():
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Мы рады за Вас! Всё что хорошо, никогда не бывает плохо.",
                               )
    elif 'ужас' in message.text.lower():
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Всё что может быть плохо, еще может привести к чему-то хорошему."
                                    f" Не опускайте руки и всё будет отлично!",
                               )
    elif 'кошмар' in message.text.lower():
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Всё что может быть плохо, еще может привести к чему-то хорошему."
                                    f" Не опускайте руки и всё будет отлично!",
                               )
    elif 'отврат' in message.text.lower():
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Всё что может быть плохо, еще может привести к чему-то хорошему."
                                    f" Не опускайте руки и всё будет отлично!",
                               )
    elif 'плох' in message.text.lower():
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Всё что может быть плохо, еще может привести к чему-то хорошему."
                                    f" Не опускайте руки и всё будет отлично!",
                               )

    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Мы ничего не поняли, попробуйте еще раз.",
                               reply_markup=kb_main)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
