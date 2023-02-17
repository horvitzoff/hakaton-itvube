# -*- coding: cp1251 -*-
from loader import dp
from aiogram import types
from bs4 import BeautifulSoup
from requests import get
from utils.clean_message import clean_message
import utils.keyboards as kb

@dp.message_handler(content_types=['text'])
async def start(message: types.Message):
    if ('сайт' or 'ссылка') in clean_message(message.text):
        await message.answer('Ссылки для абитуриентов',reply_markup=kb.site_keyboard)