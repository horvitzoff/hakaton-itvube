# -*- coding: cp1251 -*-
from loader import dp
from aiogram import types
from inlines.keyboards import main_keyboard

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}.\nЯ бот университета Иннополис.\n Напиши мне любые интересующие тебя вопросы, связаные с поступлением',reply_markup=main_keyboard)