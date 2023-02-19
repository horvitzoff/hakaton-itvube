from loader import dp
from aiogram import types
from inlines.keyboards import main_keyboard

@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    await message.answer('Вы можете обратиться:\n1. По номеру телефона: +78432039253\n2. Написав на эл.почту: university@innopolis.ru')