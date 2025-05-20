from aiogram import types, Router, F


group_router = Router()


restricted_words = ["ненужно","нет","червяк"]
@group_router.message(F.text)
async def canseled_words(message: types.Message):
    words_ist = message.text.lower().split(" ")
    for word in words_ist:
        if word in restricted_words:
            await (message.answer(f"{message.from_user.first_name} запретное слово"))
            await message.delete()