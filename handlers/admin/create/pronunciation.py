from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.buttons import CREATE_PRONUNCIATION_TEXT, back_markup, BACK_TEXT, create_markup
from db.mapper import insert_pronunciation
from dispatch import dp, bot
from states import CreateAdminState, PronunciationCreateState


@dp.message_handler(lambda message: str(message.text).__eq__(CREATE_PRONUNCIATION_TEXT), state=CreateAdminState.begin)
async def create_pronunciation_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Iltimos nom kiriting"
    await PronunciationCreateState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=back_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(BACK_TEXT), state=[PronunciationCreateState.begin])
async def back_pronunciation_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Bosh menuga xush kelibsiz"
    await CreateAdminState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=create_markup())


@dp.message_handler(state=PronunciationCreateState.begin)
async def pronunciation_name_insert(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    text = "Iltimos fayl tashlang (pdf,doc,audio,video)"
    await PronunciationCreateState.file.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id)


@dp.message_handler(content_types=types.ContentType.VIDEO, state=PronunciationCreateState.file)
async def pronunciation_video_file_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        file_id = message.video.file_id
        file_info = await bot.get_file(file_id=file_id)
        data['file'] = file_info.file_id
        data['created_by'] = message.chat.id
        data['content_type'] = "video"
    pron = insert_pronunciation(data=data)
    pron.insert_pronunciation()
    text = "Muaffaqiyatli yaratildi"
    await CreateAdminState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=create_markup())


@dp.message_handler(content_types=types.ContentType.AUDIO, state=PronunciationCreateState.file)
async def pronunciation_audio_file_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        file_id = message.audio.file_id
        file_info = await bot.get_file(file_id=file_id)
        data['file'] = file_info.file_id
        data['created_by'] = message.chat.id
        data['content_type'] = "audio"
    pron = insert_pronunciation(data=data)
    pron.insert_pronunciation()
    text = "Muaffaqiyatli yaratildi"
    await CreateAdminState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=create_markup())


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=PronunciationCreateState.file)
async def pronunciation_audio_file_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        file_id = message.document.file_id
        file_info = await bot.get_file(file_id=file_id)
        data['file'] = file_info.file_id
