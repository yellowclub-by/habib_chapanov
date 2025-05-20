from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="бот продажи продуктов", url="tg://resolve?domain=colonwelltricollagen_bot")]
    ]
)



links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="ответы на экзамен", url="tg://resolve?domain=super_math_exam_answers_bot"),
            InlineKeyboardButton(text=" серверы майнкрафта", url="tg://resolve?domain=@FTmain2_bot"),
            InlineKeyboardButton(text="<i>бот продажи продуктов</i>", url="tg://resolve?domain=colonwelltricollagen_bot")
        ]
    ]
)

