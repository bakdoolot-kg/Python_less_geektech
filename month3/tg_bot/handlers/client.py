from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from config import bot
from keyboards.client_kb import start_markup


# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hello my boss {message.from_user.full_name}",
                           reply_markup=start_markup)


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_1',
    )
    markup.add(button_call_1)

    question = "Чему равно число p?"
    answers = [
        '3.15', '4.25', '3.14', '2.14'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Я тоже не знаю...",
        explanation_parse_mode=ParseMode.MARKDOWN,
        reply_markup=markup
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
