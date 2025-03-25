import asyncio
from aiogram import Bot, Dispatcher, types
TOKEN= "8042387585:AAHQN_VLraqQD1ZqeCBA82757Tw2COsK-WU"

bot = Bot(token = TOKEN)
dp = Dispatcher()

async def main():
    print("бот запущен")
    await dp.start_poling(bot)

asyncio.run(main())