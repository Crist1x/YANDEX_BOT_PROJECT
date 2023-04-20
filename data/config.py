TOKEN_API = "6167121391:AAG9JRuVZPmktCtr7pJqcZoP1r-WDt2u7OI"
GREETING_STICKER = "CAACAgIAAxkBAAEIIAlkD2_NHRnP3aDhHC4o5FmF8XghKgACQBUAAsvQKEhYAvM4TJrDvy8E"

HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
}

STUFF = [["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,110,"
          "22,71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,"
          "21&dest=-1257786&nm=10996977",
          "https://basket-01.wb.ru/vol109/part10996/10996977/images/c246x328/1.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,110,"
          "22,71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,"
          "21&dest=-1257786&nm=81957766;77691889;148987287;86927378;64368552;142786769",
          "https://basket-05.wb.ru/vol776/part77691/77691889/images/c246x328/1.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,110,"
          "22,71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,"
          "21&dest=-1257786&nm=40912361",
          "https://basket-03.wb.ru/vol409/part40912/40912361/images/c246x328/4.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,110,"
          "22,71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,"
          "21&dest=-1257786&nm=137026978;140854563;145207583",
          "https://basket-10.wb.ru/vol1408/part140854/140854563/images/big/5.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,110,"
          "22,71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,"
          "21&dest=-1257786&nm=43007173",
          "https://basket-03.wb.ru/vol430/part43007/43007173/images/big/1.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,110,22,"
          "71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,21&dest="
          "-1257786&nm=59181453",
          "https://basket-04.wb.ru/vol591/part59181/59181453/images/big/1.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,"
          "30,86,75,40,1,66,31,48,110,22,71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale"
          "=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,21&dest=-1257786&nm=57853281;16265301;55498604;"
          "62249244;75444189;75231615;45098494;61250504;46864268",
          "https://basket-05.wb.ru/vol752/part75231/75231615/images/big/1.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,110,"
          "22,71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,21&"
          "dest=-1257786&nm=19008821",
          "https://basket-02.wb.ru/vol190/part19008/19008821/images/big/1.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,110,"
          "22,71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,21"
          "&dest=-1257786&nm=9360279;9360277;12921952;9360278",
          "https://basket-01.wb.ru/vol93/part9360/9360277/images/big/1.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,"
          "110,22,71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,"
          "15,21&dest=-1257786&nm=136544885",
          "https://basket-10.wb.ru/vol1365/part136544/136544885/images/big/1.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,110"
          ",22,71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,21"
          "&dest=-1257786&nm=140237111;140724975;143560047;143561588;143562782;148379583",
          "https://basket-10.wb.ru/vol1402/part140237/140237111/images/big/1.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,110,"
          "22,71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,21"
          "&dest=-1257786&nm=124421341;124421340;124421343;124421333;124421335;124421334;124421336;124421342;124421338;"
          "124421332;124421337;124421339",
          "https://basket-09.wb.ru/vol1244/part124421/124421333/images/big/1.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,110,"
          "22,71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,21&"
          "dest=-1257786&nm=143142003;143209421;143209420;143142005;143144240;143144231",
          "https://basket-10.wb.ru/vol1432/part143209/143209420/images/big/1.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,110,22,"
          "71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,21&"
          "dest=-1257786&nm=45165923;50938089;50938090;45225012;57528631;57528580;57528661",
          "https://basket-04.wb.ru/vol452/part45225/45225012/images/big/1.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,110,"
          "22,71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,21"
          "&dest=-1257786&nm=141830534;141830533;141830535",
          "https://basket-10.wb.ru/vol1418/part141830/141830533/images/big/1.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,110,"
          "22,71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,21"
          "&dest=-1257786&nm=12505392;12505393;12505396;140186296;140186295;140185269;11497897;43966661;140185268;"
          "12505397;12505398;43966655;140186468;43966659;11497898;140186469;12505395;140184991;140184992;12505394;"
          "43966660;140185625;140185626;43966652",
          "https://basket-01.wb.ru/vol114/part11497/11497897/images/big/1.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,110,"
          "22,71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,21"
          "&dest=-1257786&nm=82456561;110398998;59389166;118879409;102523014;118879408;46653395;115313929;46653396;"
          "82456560;46653397;147141460;59384506;110398997;59389165;110473753;109155863",
          "https://basket-07.wb.ru/vol1103/part110398/110398997/images/big/1.jpg"],
         ["https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,31,48,"
          "110,22,71,111&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,"
          "15,21&dest=-1257786&nm=127496919;36831422;80865930;80865931;80865932;80865933;80865934;96423865;149387913",
          "https://basket-05.wb.ru/vol964/part96423/96423865/images/big/1.jpg"],
         ]

HELP = """В нашем боте реализованы такие функции как:

1. <b>🎁 Сюрприз 🎁</b> - бот пришлет Вам подборку самых милых подарков для вашей второй половинки.
2. <b>🚗 Прогулка 🚗</b> - бот найдет за Вас самые романтичные места для идеального свидания.
3. <b>♐️ Совместимость ♌️</b> - бот рассчитает уровень гармонии в 
ваших отношениях и покажет астрологическую сочетаемость Ваших знаков зодиака.
4. <b>💌 Комплимент 🎀</b> - бот предложит Вам необычный комплимент для второй половинки.
5. <b>🍿 Фильмы 🎥</b> - бот расскажет Вам о самых красивых и нежных фильмах для двоих. 
"""

DESCR = "<b>L’amour fou</b> - это ваш помощник, который облегчает вам выбор фильма, \
места для свидания или идеальной прогулки, подарка и остальных романтических вещей для своей второй половинки❤️‍🔥"

ZODIAKS = {"стрелец": "strelec",
           "скорпион": "skorpion",
           "близнецы": "bliznecy",
           "телец": "telec",
           "рак": "rak",
           "рыбы": "ryby",
           "водолей": "vodoley",
           "козерог": "kozerog",
           "весы": "vesy",
           "дева": "deva",
           "овен": "oven",
           "лев": "lev"
           }
