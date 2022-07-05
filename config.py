from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN = [608718247]
URL = "https://baku18-1.herokuapp.com/"
URI = "postgres://ekmzrrbkxdxyum:0d73c0f56e6f6cb811dcc29a27b2d82fccb1932c06559904848732f9cbcc4ae3@ec2-34-248-169-69.eu-west-1.compute.amazonaws.com:5432/dej61pdm5tbe41"
