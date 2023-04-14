from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types.input_media import InputMedia
from data.config import TOKEN_API, GREETING_STICKER, HELP, DESCR, HEADERS, STUFF, ZODIAKS
from data.keyboards import kb_main, ikb_tovars, ikb_progul, ikb_sex, ikb_komp, ikb_sights
from data.classes import Female, Male
from bs4 import BeautifulSoup as bs

import time
import requests
import json
import random
import sqlite3