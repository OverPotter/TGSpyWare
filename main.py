from aiogram.utils import executor
from tg.dispatcher import dp

from tg import handlers

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
