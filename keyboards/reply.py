from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/cotolog"), KeyboardButton(text="/bots")]
        ],
    resize_keyboard=True,
    input_field_placeholder="text"


)
