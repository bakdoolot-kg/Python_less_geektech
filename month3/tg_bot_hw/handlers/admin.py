from aiogram import types, Dispatcher

from config import bot


async def dice(message: types.Message):
    user = await bot.send_dice(message.chat.id, emoji="🎲")
    pc = await bot.send_dice(message.chat.id, emoji="🎲")

    if user.dice.value > pc.dice.value:
        await message.answer(f'Победил {message.from_user.full_name}')
    elif user.dice.value == pc.dice.value:
        await message.answer('Ничья!')
    else:
        await message.answer(f'Победил Бот (Точнее Я)')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(dice, commands=["dice"])
