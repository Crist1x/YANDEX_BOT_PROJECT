from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types.input_media import InputMedia
from data.config import TOKEN_API, GREETING_STICKER, HELP, DESCR, HEADERS, STUFF
from data.keyboards import kb_main, ikb_tovars, ikb_progul, ikb_sex
from data.classes import Female, Male

import requests
import json
import random