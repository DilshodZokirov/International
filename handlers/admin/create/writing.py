from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from buttons.buttons import CREATE_WRITING_TEXT, back_markup, BACK_TEXT, create_markup
from buttons.inline import writing_topics_markup
from db.model_admin import Admin
from db.model_writing import WritingTopic, Writing
from dispatch import dp, bot
from states import CreateAdminState, AdminWritingState


@dp.message_handler(lambda message: str(message.text).__eq__(CREATE_WRITING_TEXT), state=CreateAdminState.begin)
async def writing_handlers(message: types.Message, state: FSMContext):
    text = "Writing uchun nom bering"

    await AdminWritingState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=back_markup())


@dp.message_handler(state=AdminWritingState.begin)
async def writing_topics(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['writing_name'] = message.text
    text = "Writing mavzusini tanlang"
    await AdminWritingState.next()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=writing_topics_markup())


@dp.callback_query_handler(state=AdminWritingState.name)
async def writing_handlers(query: types.CallbackQuery, state: FSMContext):
    await query.message.delete()
    if query.data != BACK_TEXT:
        async with state.proxy() as data:
            data['category'] = query.data
        text = "File ni tashlang"
        await AdminWritingState.next()
        await query.message.bot.send_message(text=text, chat_id=query.message.chat.id, reply_markup=ReplyKeyboardRemove())
    else:
        text = "Yaratish bo'limi"
        await CreateAdminState.begin.set()
        await query.message.bot.send_message(text=text, chat_id=query.message.chat.id, reply_markup=create_markup())


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=AdminWritingState.file)
async def get_file(message: types.Message, state: FSMContext):
    user = Admin(chat_id=str(message.chat.id)).select_admin_registered()
    async with state.proxy() as data:
        file_id = message.document.file_id
        file_info = await bot.get_file(file_id=file_id)
        data['admin_file'] = file_id
    Writing(name=data['writing_name'], writing=data['admin_file'], content_type=data['category'], created_by=user[0]).insert_writing()
    await CreateAdminState.begin.set()
    text = "Writing file muvafaqiyatli qo'shildi"
    # await message.bot.send_document(document=file_info.file_id, chat_id=message.chat.id)
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=create_markup())
