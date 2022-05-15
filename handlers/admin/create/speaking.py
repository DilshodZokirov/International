from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.buttons import CREATE_SPEAKING_PRACTICE_TEXT, back_markup, BACK_TEXT, create_markup
from db.mapper import insert_speaking
from db.model_speaking import Speaking
from dispatch import dp, bot
from states import CreateAdminState


@dp.message_handler(lambda message: str(message.text).__eq__(CREATE_SPEAKING_PRACTICE_TEXT),
                    state=CreateAdminState.begin)
async def create_practice_speaking_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Speaking yaratish bo'limiga xush kelibsiz" \
           "nomini kiriting"
    await CreateAdminState.create_speaking.set()
    await message.bot.send_message(text=text,
                                   chat_id=message.chat.id,
                                   reply_markup=back_markup())


@dp.message_handler(lambda message: not str(message.text).__eq__(BACK_TEXT), state=CreateAdminState.create_speaking)
async def create_name_insert(message: types.Message, state: FSMContext):
    text = "Iltimos speaking file ni tashlang (video or audio)"
    await CreateAdminState.speaking_file.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id)


@dp.message_handler(lambda message: str(message.text).__eq__(BACK_TEXT),
                    state=[CreateAdminState.create_speaking, CreateAdminState.speaking_file])
async def back_menu(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        text = "Asosiy menuga xush kelibsiz"
    await CreateAdminState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=create_markup())


@dp.message_handler(content_types=types.ContentType.AUDIO, state=CreateAdminState.speaking_file)
async def create_file_speaking(message: types.Message, state: FSMContext):
    file_id = message.audio.file_id
    file_info = await bot.get_file(file_id=file_id)
    async with state.proxy() as data:
        data['speaking_file'] = file_info.file_id
        data['content_type'] = 'audio'
    insert = insert_speaking(data)
    insert.insert_speaking()
    text = "Speaking topik muaffaqiyatli yaratildi"
    await CreateAdminState.begin.set()
    await message.bot.send_message(text=text,
                                   chat_id=message.chat.id,
                                   reply_markup=create_markup())


@dp.message_handler(content_types=types.ContentType.VIDEO, state=CreateAdminState.speaking_file)
async def create_file_speaking(message: types.Message, state: FSMContext):
    file_id = message.video.file_id
    file_info = await bot.get_file(file_id=file_id)
    async with state.proxy() as data:
        data['speaking_file'] = file_info.file_id
        data['content_type'] = 'video'
    insert = insert_speaking(data)
    insert.insert_speaking()
    text = "Speaking topik muaffaqiyatli yaratildi"
    await CreateAdminState.begin.set()
    await message.bot.send_message(
        text=text,
        chat_id=message.chat.id,
        reply_markup=create_markup()
    )


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=CreateAdminState.speaking_file)
async def create_file_speaking(message: types.Message, state: FSMContext):
    file_id = message.document.file_id
    file_info = await bot.get_file(file_id=file_id)
    async with state.proxy() as data:
        data['speaking_file'] = file_info.file_id
        data['content_type'] = 'document'
    insert = insert_speaking(data)
    insert.insert_speaking()
    text = "Speaking topik muaffaqiyatli yaratildi"
    await CreateAdminState.begin.set()
    await message.bot.send_message(
        text=text,
        chat_id=message.chat.id,
        reply_markup=create_markup()
    )


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=CreateAdminState.create_speaking)
async def pronunciation_audio_file_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        file_id = message.document.file_id
        file_info = await bot.get_file(file_id=file_id)
        data['file'] = file_info.file_id
