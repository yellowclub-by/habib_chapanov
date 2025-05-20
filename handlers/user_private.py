from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from keyboards import reply, inline

user_router=Router()

@user_router.message(CommandStart())
async def start(message: types.Message):
    await (message.answer("продажа акаунтов",reply_markup=reply.main_kb))



@user_router.message(Command("cotolog"))
async def cotolog(message: types.Message):
    await (message.answer("купить акк"))


@user_router.message(Command("bots"))
async def script(message: types.Message):
    await (message.answer("другие хорошие боты",reply_markup=inline.links_kb))




# @user_router.message(F.text.lower())
# @user_router.message(F.text.lower().contains("цен")|F.text.lower().contains("стоин"))
# async def echo(message: types.Message):
#     await(message.answer("бот в разроботке"))