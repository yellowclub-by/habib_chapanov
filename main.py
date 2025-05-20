import asyncio

import aiogram.client.session.base
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode





TOKEN= "8042387585:AAHQN_VLraqQD1ZqeCBA82757Tw2COsK-WU"

bot = Bot(token = TOKEN,parse_mode=ParseMode.HTML)
dp = Dispatcher()



from handlers.user_private import user_router
from handlers.user_groupe import group_router

dp.include_router(user_router)
dp.include_router(group_router)




async def main():
    print("бот запущен")
    await dp.start_polling(bot)


asyncio.run(main())