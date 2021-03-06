from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from db.dto import ListeningDto, MaterialDto
from db.model_listening import ListeningMain
from db.model_pronunciation import Materials
from db.model_speaking import Speaking
from .buttons import BACK_TEXT
from db.model_group import Group
from db.model_writing import WritingTopic, Writing

ELEMENTARY_TEXT = "Elementary"
PRE_INTERMEDIATE_TEXT = "Pre Intermediate"
INTERMEDIATE_TEXT = "Intermediate"
UPPER_INTERMEDIATE_TEXT = "Upper Intermediate"
ADVANCED_TEXT = "Advanced"

UZ_LANGUAGE_TEXT = "๐บ๐ฟ O'zbekcha"
RU_LANGUAGE_TEXT = "๐ท๐บ ะ ัััะบะธะน"
EN_LANGUAGE_TEXT = "๐ฌ๐ง English"


def listening_names():
    markup = InlineKeyboardMarkup()
    names = ListeningMain().select_all_listening_main()
    back = InlineKeyboardButton(text=BACK_TEXT, callback_data=BACK_TEXT)
    for i in names:
        button = InlineKeyboardButton(text=i[1], callback_data=i[0])
        markup.add(button)
    markup.add(back)
    return markup


def writing_topics_markup():
    topics = WritingTopic().select_all_writing()
    keyboard = InlineKeyboardMarkup()
    back = InlineKeyboardButton(text=f"{BACK_TEXT}", callback_data=f'{BACK_TEXT}')
    if topics:
        for i in topics:
            button = InlineKeyboardButton(text=i[1], callback_data=i[0])
            keyboard.add(button)
    keyboard.add(back)
    return keyboard


def get_writings_by_topics(topic_id):
    writings = Writing(content_type=topic_id).get_writing_by_topic()
    keyboard = InlineKeyboardMarkup()
    back = InlineKeyboardButton(text=f"{BACK_TEXT}", callback_data=f"{BACK_TEXT}")
    if writings:
        for i in writings:
            button = InlineKeyboardButton(text=i[1], callback_data=f"{i[0]}")
            keyboard.add(button)
    keyboard.add(back)
    return keyboard


def document_materials_markup():
    markup = InlineKeyboardMarkup()
    documents = Materials().select_by_document()
    back = InlineKeyboardButton(text=BACK_TEXT, callback_data=BACK_TEXT)
    for i in documents:
        button = InlineKeyboardButton(text=i[1],callback_data=i[0])
        markup.add(button)
    markup.add(back)
    return markup


def video_materials_markup():
    markup = InlineKeyboardMarkup()
    documents = Materials().select_by_video()
    back = InlineKeyboardButton(text=BACK_TEXT, callback_data=BACK_TEXT)
    for i in documents:
        button = InlineKeyboardButton(text=i[1],callback_data=i[0])
        markup.add(button)
    markup.add(back)
    return markup


def audio_materials_markup():
    markup = InlineKeyboardMarkup()
    documents = Materials().select_by_audio()
    back = InlineKeyboardButton(text=BACK_TEXT, callback_data=BACK_TEXT)
    for i in documents:
        button = InlineKeyboardButton(text=i[1],callback_data=i[0])
        markup.add(button)
    markup.add(back)
    return markup


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
    keyboard.add(InlineKeyboardButton(text="๐ Back", callback_data='back'))
    return None if len(users) == 0 else keyboard

def listening_delete_file_inline(listening_dto : List[ListeningDto]):

    keyboard = InlineKeyboardMarkup()
    for listening in listening_dto:
        keyboard.add(InlineKeyboardButton(text=listening.name, callback_data=listening.unique_id))
    keyboard.add(InlineKeyboardButton(text="๐ Back" , callback_data='back'))

    return keyboard

def material_delete_file_inline(material_dto : List[MaterialDto]):

    keyboard = InlineKeyboardMarkup()
    for material in material_dto:
        keyboard.add(InlineKeyboardButton(text=material.name, callback_data=material.unique_id))
    keyboard.add(InlineKeyboardButton(text="๐ Back" , callback_data='back'))

    return keyboard



