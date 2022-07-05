from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
location_button = KeyboardButton("Share location", request_location=True)
info_button = KeyboardButton("Share info", request_contact=True)

start_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

start_markup.row(start_button, quiz_button, location_button, info_button)
