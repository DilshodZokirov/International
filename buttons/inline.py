from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from db.model_group import Group

ELEMENTARY_TEXT = "Elementary"
PRE_INTERMEDIATE_TEXT = "Pre Intermediate"
INTERMEDIATE_TEXT = "Intermediate"
UPPER_INTERMEDIATE_TEXT = "Upper Intermediate"
ADVANCED_TEXT = "Advanced"

UZ_LANGUAGE_TEXT = "🇺🇿 O'zbekcha"
RU_LANGUAGE_TEXT = "🇷🇺 Русский"
EN_LANGUAGE_TEXT = "🇬🇧 English"


def language_inline_markup():
    keyboard = InlineKeyboardMarkup()
    row1 = InlineKeyboardButton(text=UZ_LANGUAGE_TEXT, callback_data="uz")
    row2 = InlineKeyboardButton(text=RU_LANGUAGE_TEXT, callback_data="ru")
    row3 = InlineKeyboardButton(text=EN_LANGUAGE_TEXT, callback_data="en")
    keyboard.add(row1, row2, row3)
    return keyboard


def level():
    keyboard = InlineKeyboardMarkup()
    row1 = InlineKeyboardButton(text=ELEMENTARY_TEXT)
    row2 = InlineKeyboardButton(text=PRE_INTERMEDIATE_TEXT)
    row3 = InlineKeyboardButton(text=INTERMEDIATE_TEXT)
    row4 = InlineKeyboardButton(text=UPPER_INTERMEDIATE_TEXT)
    row5 = InlineKeyboardButton(text=ADVANCED_TEXT)
    keyboard.add(row1)
    keyboard.add(row2)
    keyboard.add(row3)
    keyboard.add(row4)
    keyboard.add(row5)
    return keyboard


def all_groups():
    keyboard = InlineKeyboardMarkup()
    users = Group().select_all_groups()
    for user in users:
        keyboard.add(InlineKeyboardButton(text=user.name, callback_data=f'{user.id}+{user.created_by}'))
    keyboard.add(InlineKeyboardButton(text="🔙 Back", callback_data='back'))
    return None if len(users) == 0 else keyboard