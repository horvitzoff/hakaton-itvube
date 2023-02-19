from loader import dp
from aiogram import types
from utils.edit_message import clean_message,func_compare
import inlines.keyboards as kb
import json


@dp.message_handler(content_types=['text'])
async def start(message: types.Message):
    with open("D:\Desktop\hakaton-itvube\parsing\json\data_file.json", "r",encoding='utf8') as read_file:
        data = json.load(read_file)


    title_list = list(data.keys())
    for i in range(len(title_list)):
        compare = func_compare(clean_message(message.text.lower()), title_list[i].lower().split())
        if compare == True:
            text = f'{title_list[i]}\n{data[title_list[i]]}'
            await message.answer(text)

    if ('сайт' or 'ссылка') in clean_message(message.text):
        await message.answer('Ссылки для абитуриентов',reply_markup=kb.site_keyboard)
    elif 'поступить' in clean_message(message.text):
        await message.answer('Задайте более конкретный вопрос')
    else:
        await message.answer('Извините, я не могу ответить на этот вопрос, но вы можете обраться за помощью /help')