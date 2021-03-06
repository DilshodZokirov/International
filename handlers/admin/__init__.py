from db.model_admin import Admin
from .delete import *
from .create import *
from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.buttons import phone_number_button, admin_markup, CREATE_TEXT, create_markup, DELETE_TEXT, delete_markup
from buttons.inline import language_inline_markup
from db.mapper import admin_insert
from dispatch import dp, bot
from states import AdminState, DeleteAdminState


# @dp.message_handler(commands='aaa', state="*")
# async def get_user(message: types.Message):
#     user = bot.()
#     print(user)


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
    admin = Admin(chat_id=str(message.chat.id)).select_admin_registered()
    if admin:
        admin_text = "admin menu"
        await AdminState.active.set()
        await message.bot.send_message(text=admin_text, chat_id=message.chat.id, reply_markup=admin_markup())
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


@dp.message_handler(lambda message: str(message.text).__eq__(CREATE_TEXT), state=AdminState.active)
async def create_handler(message: types.Message):
    text = "Yaratish bo'limi"
    await CreateAdminState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=create_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(DELETE_TEXT), state=AdminState.active)
async def delete_handler(message: types.Message, state: FSMContext):
    text = "Delete bo'limiga xush kelibsiz"
    await ProductDeleteState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=delete_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(BACK_TEXT), state=ProductDeleteState.begin)
async def back_in_delete(message: types.Message):
    text = "Bosh menu"
    await AdminState.active.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=admin_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(BACK_TEXT), state=CreateAdminState.begin)
async def back_in_create(message: types.Message):
    text = "Bosh menu"
    await AdminState.active.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=admin_markup())