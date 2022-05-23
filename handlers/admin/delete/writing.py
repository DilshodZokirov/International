from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from buttons.buttons import CREATE_WRITING_TEXT, back_markup, BACK_TEXT, create_markup, admin_markup
from buttons.inline import writing_topics_markup, get_writings_by_topics
from db.model_admin import Admin
from db.model_writing import WritingTopic, Writing
from dispatch import dp, bot
from states import CreateAdminState, DeleteAdminState, DeleteWritingState, AdminState


@dp.message_handler(lambda message: str(message.text).__eq__(CREATE_WRITING_TEXT),state=DeleteAdminState.begin)
async def writing_topics(message: types.Message, state: FSMContext):
    text = "Writing mavzusini tanlang"
    await DeleteWritingState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=writing_topics_markup())


@dp.callback_query_handler(state=DeleteWritingState.begin)
async def writing_names(query: types.CallbackQuery):
    await query.message.delete()
    if query.data != BACK_TEXT:
        await DeleteWritingState.next()
        text = "O'chirish kerak bo'lgan writingni tanlang"
        await query.message.bot.send_message(text=text, chat_id=query.message.chat.id,
                                             reply_markup=get_writings_by_topics(query.data))
    else:
        text = 'Admin menu'
        await AdminState.active.set()
        await query.message.bot.send_message(text=text, chat_id=query.message.chat.id, reply_markup=admin_markup())


@dp.callback_query_handler(state=DeleteWritingState.deleting)
async def deleting_writing(query: types.CallbackQuery):
    await query.message.delete()
    if query.data != BACK_TEXT:
        Writing(unique_id=query.data).delete_writing_by_id()
        text = "Muvafaqiyatli o'chirildi"
        await AdminState.active.set()
        await query.message.bot.send_message(text=text, chat_id=query.message.chat.id, reply_markup=admin_markup())
    else:
        text = 'Admin menu'
        await AdminState.active.set()
        await query.message.bot.send_message(text=text, chat_id=query.message.chat.id, reply_markup=admin_markup())




