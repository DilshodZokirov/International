from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.buttons import phone_number_button
from buttons.inline import language_inline_markup
from db.mapper import admin_insert
from db.model_admin import Admin
from dispatch import dp
from states import AdminState


@dp.message_handler(commands="Admin", state="*")
async def admin_menu(message: types.Message, state: FSMContext):
    text = "Noto'g'ri url"
    await AdminState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id)


@dp.message_handler(state=AdminState.begin)
async def admin_check(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    if not message.text.__eq__('private'):
        text = "Noto'g'ri url"
        await message.answer(text=text)
        return
    text = "Tilingizni tanlang"
    await AdminState.language.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=language_inline_markup())


@dp.callback_query_handler(state=AdminState.language)
async def admin_language_handler(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['lang'] = query.data
    text = "Ismingizni kiriting"
    await AdminState.name.set()
    await query.message.bot.send_message(text=text, chat_id=query.message.chat.id)


@dp.message_handler(state=AdminState.name)
async def name_admin(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    text = "Telefon nomeringizni kiriting"
    await AdminState.phone.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=phone_number_button())


@dp.message_handler(content_types=types.ContentType.CONTACT, state=AdminState.phone)
async def admin_phone_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['chat_id'] = message.chat.id
        data['phone'] = message.contact.phone_number
    admin = admin_insert(data)
    admin.insert_admin()
    text = "Admin muoffaqiyatli yaratildi"
    await AdminState.active.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=admin_markup())
