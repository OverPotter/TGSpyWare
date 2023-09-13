from aiogram import types


async def reply_handler(message: types.Message, data: str):
    if len(data) > 4096:
        for x in range(0, len(data), 4096):
            await message.answer(data[x:x + 4096])
    else:
        await message.answer(data)
