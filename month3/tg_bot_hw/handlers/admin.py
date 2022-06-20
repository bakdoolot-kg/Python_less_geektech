from aiogram import types, Dispatcher

from config import bot, ADMIN
from database.bot_db import sql_commands_get_all_id


async def dice(message: types.Message):
    user = await bot.send_dice(message.chat.id, emoji="🎲")
    pc = await bot.send_dice(message.chat.id, emoji="🎲")

    if user.dice.value > pc.dice.value:
        await message.answer(f'Победил {message.from_user.full_name}')
    elif user.dice.value == pc.dice.value:
        await message.answer('Ничья!')
    else:
        await message.answer(f'Победил Бот (Точнее Я)')


async def mailing(message: types.Message):
    if message.from_user.id in ADMIN:
        result = await sql_commands_get_all_id()
        print(result)
        for id in result:
            await bot.send_message(id[0], message.text[3:])
    else:
        await message.answer("Ты не мой БОСС!!!")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(dice, commands=["dice"])
    dp.register_message_handler(mailing, commands=["R"])
