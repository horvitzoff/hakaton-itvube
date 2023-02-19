# -*- coding: cp1251 -*-
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton,\
    WebAppInfo
from data.const import Urls

site_button1 = InlineKeyboardButton('�����������', web_app=WebAppInfo(url=Urls.url_bakalavr))
site_button2 = InlineKeyboardButton('������������',web_app=WebAppInfo(url=Urls.url_magistr))
site_button3 = InlineKeyboardButton('����������',web_app=WebAppInfo(url=Urls.url_aspirant))
site_keyboard = InlineKeyboardMarkup().add(site_button1,site_button2,site_button3)

main_button = InlineKeyboardButton('����������� ����', web_app=WebAppInfo(url=Urls.url_main))
main_keyboard = InlineKeyboardMarkup().add(main_button)