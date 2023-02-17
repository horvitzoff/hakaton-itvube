# -*- coding: cp1251 -*-
from loader import dp
from aiogram import types
from utils.clean_message import clean_message
import inlines.keyboards as kb

@dp.message_handler(content_types=['text'])
async def start(message: types.Message):
    if ('����' or '������') in clean_message(message.text):
        await message.answer('������ ��� ������������',reply_markup=kb.site_keyboard)