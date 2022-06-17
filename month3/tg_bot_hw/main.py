from aiogram import types
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from config import bot, dp
import logging


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, f"Бот 18-1 к вашим услугам {message.from_user.full_name}")


@dp.message_handler(commands=['quiz'])
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


@dp.message_handler(commands=['mem'])
async def command_mem(message: types.Message):
    photo = open("media/images/putin.jpg", 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


@dp.callback_query_handler(lambda call: call.data == "button_next")
async def quiz_2(call: types.CallbackQuery):
    question = "Какой синтаксис вы бы использовали при создании переменной для ввода имени?"
    answers = [
        "input=name",
        "name=input{}",
        "name=INPUT",
        "name=input()",
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


@dp.message_handler()
async def squaring(message: types.Message):
    print(message.text)
    try:
        num = int(message.text) ** 2
        await bot.send_message(message.chat.id, num)
    except:
        await bot.send_message(message.chat.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
