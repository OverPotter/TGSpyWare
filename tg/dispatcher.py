import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from tg_config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

if not BOT_TOKEN:
    exit("No token provided")

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

dp.middleware.setup(LoggingMiddleware())
