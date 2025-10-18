from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Игры"), KeyboardButton(text="Помощь")],
        [KeyboardButton(text="Посхалка")]
    ],
    resize_keyboard=True, 
    input_field_placeholder="Зайдите в меню чтобы играть"
)

game = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Football", callback_data="football")],
        [InlineKeyboardButton(text="Basketball", callback_data="basketball")],
        [InlineKeyboardButton(text="Darts", callback_data="darts")],
        [InlineKeyboardButton(text="Bowling", callback_data="bowling")],
        [InlineKeyboardButton(text="Slots", callback_data="slots")],
        [InlineKeyboardButton(text="Dice", callback_data="dice")]
    ]
)