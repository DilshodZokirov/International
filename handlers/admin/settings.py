
from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.inline import language_inline_markup
from db.model_user import User
from db.model_admin import Admin
from buttons.buttons import SETTING_TEXT, settings_markup, EDIT_USERNAME_TEXT, EDIT_LANGUAGE_TEXT, BACK, home_menu, MY_CABINET_TEXT
from dispatch import dp
from states import FinalRegisterState, SettingState
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(lambda message: str(message.text).__eq__(SETTING_TEXT), state=FinalRegisterState.begin)
async def settings_handlers(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Settings bo'limi"
    await SettingState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=settings_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(EDIT_USERNAME_TEXT),state=SettingState.begin)
async def begin_edit_fullname(message: types.Message, state:FSMContext):
    user = Admin(chat_id=str(message.chat.id)).select_admin_registered()
    username = user[2]
    await message.bot.send_message(text=f"Hozirgi ismingiz {username}", chat_id=message.chat.id)
    text = 'Yangi Ismni kiriting'
    await SettingState.fullname.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=SettingState.fullname)
async def edit_fullname(message: types.Message, ):
    Admin(name=message.text, chat_id=str(message.chat.id)).update_name()
    await SettingState.begin.set()
    text = f"Ismingiz {message.text} ga Muvafaqiyatli o'zgartirildi"
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=settings_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(BACK),state=SettingState.begin)
async def back_from_settings(message:types.Message):
    text = "Marxamat bosh menu"
    await FinalRegisterState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=home_menu())


@dp.message_handler(lambda message: str(message.text).__eq__(EDIT_LANGUAGE_TEXT),state=SettingState.begin)
async def begin_lang_edit(message: types.Message):
    await SettingState.lang.set()
    text = "Tilni o'zgartirasizmi ?"
    text2= "Tilni o'zgartirish uchun quyidagilardan birini tanlang"
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=ReplyKeyboardRemove())
    await message.bot.send_message(text=text2, chat_id=message.chat.id, reply_markup=language_inline_markup())


@dp.callback_query_handler(state=SettingState.lang)
async def lang_edit(query: types.CallbackQuery):
    Admin(language=query.data).update_language()
    await FinalRegisterState.begin
    text = "Sizning tilingiz muvafaqiyatli o'zgartirildi"
    await query.bot.send_message(text=text, chat_id=query.message.chat.id, reply_markup=home_menu())


@dp.message_handler(lambda message: str(message.text).__eq__(MY_CABINET_TEXT), state=SettingState.begin)
async def show_profile(message: types.Message):
    user = Admin(chat_id=str(message.chat.id)).select_admin_registered()
    username = user[2]
    user_lang = user[1]
    phone = user[3]
    await message.bot.send_message(text=f"*Ism*: {username}\n*til*: {user_lang}\n*telefon*: {phone}", chat_id=message.chat.id)