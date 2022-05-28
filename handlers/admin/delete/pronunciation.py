from typing import List

from aiogram import types
from aiogram.dispatcher import FSMContext


from buttons.buttons import DELETE_LISTENING_TEXT, back_markup, admin_markup, DELETE_PRONUNCIATION_TEXT
from buttons.inline import listening_delete_file_inline, material_delete_file_inline
from db.dto import ListeningDto, MaterialDto
from db.model_listening import Listening
from db.model_pronunciation import Materials
from dispatch import dp
from states import CreateAdminState, DeleteListeningState, ProductDeleteState, AdminState, PronunciationDeleteState


@dp.message_handler(lambda message: str(message.text).__eq__(DELETE_PRONUNCIATION_TEXT), state=ProductDeleteState.begin)
async def create_listening_handler(message: types.Message, state: FSMContext):
    async with  state.proxy() as data:
        pass
    text = "Marxamat o'chiradigan materialni nomini kiriting"
    await PronunciationDeleteState.name.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=back_markup())


@dp.message_handler(state=PronunciationDeleteState.name)
async def delete_pronunciation_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['file_name'] = message.text
    material = Materials()
    material_dto: List[MaterialDto] = material.select_all_speak_find(data.get('file_name'))
    if not material_dto:
        await AdminState.active.set()
        await message.bot.send_message(chat_id=message.chat.id, text='Hech qanday malumot topilmadi',
                                       reply_markup=admin_markup())
        return
    await PronunciationDeleteState.delete.set()
    await message.bot.send_message(chat_id=message.chat.id , text = 'Topilganlari 👇', reply_markup=material_delete_file_inline(material_dto))


@dp.callback_query_handler(state=PronunciationDeleteState.delete)
async def Listening_Callback_handler(query: types.CallbackQuery, state = FSMContext):
    await query.message.delete()
    if query.data == 'back':
        await AdminState.active.set()
        await query.message.bot.send_message(chat_id=query.message.chat.id, text = 'Menu',
                                             reply_markup=admin_markup())
        return

    Materials().delete_speak(query.data)
    await AdminState.active.set()
    await query.message.bot.send_message(chat_id=query.message.chat.id , text = 'Muofaqiyatli ochirildi !' , reply_markup=admin_markup())