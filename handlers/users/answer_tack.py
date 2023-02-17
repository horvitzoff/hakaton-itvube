# -*- coding: cp1251 -*-
from loader import dp
from aiogram import types
import utils.dist_answer as uda
from bs4 import BeautifulSoup
from requests import get


@dp.message_handler(content_types=['text'])
async def start(message: types.Message):
    pass