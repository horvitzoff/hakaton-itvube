# -*- coding: cp1251 -*-
from loader import dp
from aiogram import types

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'������, {message.from_user.first_name}.\n� ��� ������������ ��������� � ���������� ������ ���� � ��������� ���������� � ������������.')