from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from config import bot
from keyboards.client_kb import start_markup


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, f"Бот 18-1 к вашим услугам {message.from_user.full_name}",
                           reply_markup=start_markup)


async def command_mem(message: types.Message):
    photo = open("media/images/putin.jpg", 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_next = InlineKeyboardButton(
        "Следующий вопрос",
        callback_data='button_next'
    )
    markup.add(button_next)

    question = "Какая функция используется для вывода сообщений в Python?"
    answers = [
        "print("")",
        "print",
        "input=name",
        "name=input"
    ]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="К сожалению не могу подсказать",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def pin_message(message: types.Message):
    if not message.reply_to_message:
        await message.answer("Команда должна быть ответом на сообщение!")
    else:
        await bot.pin_chat_message(message.chat.id, message.message_id)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(command_mem, commands=['mem'])
    dp.register_message_handler(pin_message, commands=['pin'], commands_prefix="!/")
