from typing import List

from aiogram import types
from aiogram.dispatcher import FSMContext


from buttons.buttons import DELETE_LISTENING_TEXT, back_markup, admin_markup, BACK_TEXT, delete_markup
from buttons.inline import listening_delete_file_inline, listening_names
from db.dto import ListeningDto
from db.model_listening import Listening, ListeningMain
from dispatch import dp
from states import CreateAdminState, DeleteListeningState, ProductDeleteState, AdminState


@dp.message_handler(lambda message: str(message.text).__eq__(DELETE_LISTENING_TEXT), state=ProductDeleteState.begin)
async def create_listening_handler(message: types.Message):

    text = "Listeninglarni o'chirish uchun nomini  tanlang"
    text2 = "Listening o'chirish bo'limi"
    await DeleteListeningState.name.set()
    await message.bot.send_message(text=text2, chat_id=message.chat.id, reply_markup=types.ReplyKeyboardRemove())
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=listening_names())


@dp.callback_query_handler(state=DeleteListeningState.name)
async def delete_listening_handler(query: types.CallbackQuery, state: FSMContext):
    await query.message.delete()
    if query.data != BACK_TEXT:
        ListeningMain(unique_id=query.data).delete_listening_main()
        await ProductDeleteState.begin.set()
        await query.message.bot.send_message(text="Muvaffaqiyatli o'chirildi",chat_id=query.message.chat.id,
                                             reply_markup=delete_markup())
    else:
        await ProductDeleteState.begin.set()
        await query.message.bot.send_message(text="O'chirish bo'limi", chat_id=query.message.chat.id,
                                             reply_markup=delete_markup())


@dp.callback_query_handler(state=DeleteListeningState.delete)
async def Listening_Callback_handler(query: types.CallbackQuery, state = FSMContext):
    await query.message.delete()
    if query.data == 'back':
        await AdminState.active.set()
        await query.message.bot.send_message(chat_id=query.message.chat.id, text = 'Menu',
                                             reply_markup=admin_markup())
        return

    Listening().delete_listening(query.data)
    await AdminState.active.set()
    await query.message.bot.send_message(chat_id=query.message.chat.id , text = 'Muvaffaqiyatli ochirildi !' , reply_markup=admin_markup())