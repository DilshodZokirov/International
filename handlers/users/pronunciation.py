from aiogram import types
from aiogram.dispatcher import FSMContext
from buttons.inline import document_materials_markup, video_materials_markup, audio_materials_markup
from buttons.buttons import MATERIALS, pronunciation_markup, BACK_TEXT, home_menu, materials_markup
# from db.model_pronunciation import Pronunciation
from db.model_pronunciation import Materials
from db.model_speaking import Speaking
from dispatch import dp, bot
from states import FinalRegisterState, PronunciationState


@dp.message_handler(lambda message: str(message.text).__eq__(MATERIALS), state=FinalRegisterState.begin)
async def pronunciation_handler(message: types.Message, state: FSMContext):
    text = "Materiallar bo'limiga xush kelibsiz"
    await PronunciationState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=materials_markup())


@dp.message_handler(lambda message: str(message.text).__eq__("Document"), state=PronunciationState.begin)
async def back_a_home_menu(message: types.Message, state: FSMContext):

    await PronunciationState.next()
    text = "Documentlar"
    await message.bot.send_message(text=text, chat_id=message.chat.id,reply_markup=types.ReplyKeyboardRemove())
    await message.bot.send_message(text="Documentlarni nomi bo'yicha tanlang", chat_id=message.chat.id, reply_markup=document_materials_markup())


@dp.message_handler(lambda message: str(message.text).__eq__("Video"), state=PronunciationState.begin)
async def video_a_home_menu(message: types.Message, state: FSMContext):

    await PronunciationState.next()
    text = "Videolar"
    await message.bot.send_message(text=text, chat_id=message.chat.id,reply_markup=types.ReplyKeyboardRemove())
    await message.bot.send_message(text="Videolarni nomi bo'yicha tanlang", chat_id=message.chat.id, reply_markup=video_materials_markup())


@dp.message_handler(lambda message: str(message.text).__eq__("Audio"), state=PronunciationState.begin)
async def audio_a_home_menu(message: types.Message, state: FSMContext):
    await PronunciationState.next()
    text = "Audiolar"
    await message.bot.send_message(text=text, chat_id=message.chat.id,reply_markup=types.ReplyKeyboardRemove())
    await message.bot.send_message(text="Audiolarni nomi bo'yicha tanlang", chat_id=message.chat.id, reply_markup=audio_materials_markup())


@dp.callback_query_handler(lambda content: str(content.data).__eq__(BACK_TEXT),state=PronunciationState.name)
async def document_get_handler(query: types.CallbackQuery):
    text = "Materiallar bo'limi"
    await PronunciationState.begin.set()
    await query.message.bot.send_message(text=text, chat_id=query.message.chat.id, reply_markup=materials_markup())


@dp.callback_query_handler(lambda content: Materials(id=content.data).select_one_material()[-1] == 'document',state=PronunciationState.name)
async def document_get_handler(query: types.CallbackQuery):
    await query.message.delete()
    material = Materials(id=query.data).select_one_material()
    file_info = await bot.get_file(file_id=material[2])
    await query.message.bot.send_document(document=file_info.file_id, chat_id=query.message.chat.id)
    text = "Materiallar bo'limiga xush kelibsiz"
    await PronunciationState.begin.set()
    await query.message.bot.send_message(text=text, chat_id=query.message.chat.id, reply_markup=materials_markup())


@dp.callback_query_handler(lambda content: Materials(id=content.data).select_one_material()[-1] == 'video',state=PronunciationState.name)
async def document_get_handler(query: types.CallbackQuery):
    await query.message.delete()
    material = Materials(id=query.data).select_one_material()
    file_info = await bot.get_file(file_id=material[2])
    await query.message.bot.send_video(video=file_info.file_id, chat_id=query.message.chat.id)
    text = "Materiallar bo'limi"
    await PronunciationState.begin.set()
    await query.message.bot.send_message(text=text, chat_id=query.message.chat.id, reply_markup=materials_markup())


@dp.callback_query_handler(lambda content: Materials(id=content.data).select_one_material()[-1] == 'audio',state=PronunciationState.name)
async def document_get_handler(query: types.CallbackQuery):
    await query.message.delete()
    material = Materials(id=query.data).select_one_material()
    file_info = await bot.get_file(file_id=material[2])
    await query.message.bot.send_audio(audio=file_info.file_id, chat_id=query.message.chat.id)
    text = "Materiallar bo'limi"
    await PronunciationState.begin.set()
    await query.message.bot.send_message(text=text, chat_id=query.message.chat.id, reply_markup=materials_markup())




@dp.message_handler(lambda message: str(message.text).__eq__(BACK_TEXT), state=PronunciationState.begin)
async def back_a_home_menu(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Bosh menu"
    await FinalRegisterState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=home_menu())
