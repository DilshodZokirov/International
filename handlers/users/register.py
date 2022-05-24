from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from buttons.buttons import REGISTER_BUTTON_TEXT, phone_number_button, home_menu
from buttons.inline import language_inline_markup
from db.mapper import user_insert
from dispatch import dp
from states import RegisterState, FinalRegisterState


@dp.message_handler(lambda message: str(message.text).__eq__(REGISTER_BUTTON_TEXT), state=RegisterState.begin)
async def register_handlers(message: types.Message):
    text2 = "Marxamat ro'yxatdan o'ting"
    text = "Tilingizni tanlang"
    await RegisterState.language.set()
    await message.bot.send_message(text=text2, chat_id=message.chat.id, reply_markup=ReplyKeyboardRemove())
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=language_inline_markup())


@dp.message_handler(content_types=types.ContentType.ANY, state=RegisterState.begin)
async def not_message_error(message: types.Message):
    text = f"Iltimos {REGISTER_BUTTON_TEXT} tugmasini  toping!"
    await message.reply(text=text)
    return


@dp.callback_query_handler(state=RegisterState.language)
async def language_handler(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['lang'] = call.data
        data['chat_id'] = call.message.chat.id
    await call.message.delete()
    text = "Iltimos ismingizni kiriting"
    await RegisterState.name.set()
    await call.message.bot.send_message(text=text, chat_id=call.message.chat.id)


@dp.message_handler(state=RegisterState.name)
async def user_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    text = "Iltimos telefon raqamingizni kiriting"
    await RegisterState.phone_number.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=phone_number_button())


@dp.message_handler(content_types=types.ContentType.CONTACT, state=RegisterState.phone_number)
async def phone_number_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.contact.phone_number
        user = user_insert(data)
    user.insert_user()
    text = "Muvaffaqiyatli yakunlandi"
    await FinalRegisterState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=home_menu())
