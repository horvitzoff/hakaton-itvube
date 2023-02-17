# -*- coding: cp1251 -*-
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

site_button1 = InlineKeyboardButton('Бакалавриат',url = 'https://apply.innopolis.university/bachelor/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit')
site_button2 = InlineKeyboardButton('Магистратура',url='https://apply.innopolis.university/master/datascience/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit')
site_button3 = InlineKeyboardButton('Аспирантов',url='https://apply.innopolis.university/postgraduate-study/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit')
site_keyboard = InlineKeyboardMarkup().add(site_button1,site_button2,site_button3)