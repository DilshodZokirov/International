from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.buttons import CREATE_LISTENING_TEXT, back_markup, BACK_TEXT, create_markup
from db.mapper import insert_listening
from dispatch import dp, bot
from states import CreateAdminState, CreateListeningState


@dp.message_handler(lambda message: str(message.text).__eq__(CREATE_LISTENING_TEXT), state=CreateAdminState.begin)
async def create_listening_handler(message: types.Message, state: FSMContext):
    async with  state.proxy() as data:
        pass
    text = "Marxamat listening uchun nom kiriting"
    await CreateListeningState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=back_markup())


@dp.message_handler(state=CreateListeningState.begin)
async def create_name_listening(message: types.Message, state: FSMContext):
    if message.text.__eq__(BACK_TEXT):
        async with state.proxy() as data:
            data['name'] = message.text
        text = "Marxamat listening uchun file tashlang (file,audio or video)"
        await CreateListeningState.file.set()
        await message.bot.send_message(text=text, chat_id=message.chat.id)
        return
    text = "Bosh menuga qaytdingiz"
    await CreateAdminState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=create_markup())


@dp.message_handler(content_types=types.ContentType.AUDIO, state=CreateListeningState.file)
async def create_file_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        file_id = message.audio.file_id
        file_info = await bot.get_file(file_id=file_id)
        data['file'] = file_info.file_id
        data['created_by'] = message.chat.id
        data['content_type'] = "audio"
    listening = insert_listening(data)
    listening.insert_listening()
    text = "Muaffaqiyatli yakunlandi"
    await CreateAdminState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=create_markup())


@dp.message_handler(content_types=types.ContentType.VIDEO, state=CreateListeningState.file)
async def create_file_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        file_id = message.video.file_id
        file_info = await bot.get_file(file_id=file_id)
        data['file'] = file_info.file_id
        data['created_by'] = message.chat.id
        data['content_type'] = "video"
    listening = insert_listening(data)
    listening.insert_listening()
    text = "Muaffaqiyatli yakunlandi"
    await CreateAdminState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=create_markup())


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=CreateListeningState.file)
async def create_file_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        file_id = message.document.file_id
        file_info = await bot.get_file(file_id=file_id)
        data['file'] = file_info.file_id
        data['created_by'] = message.chat.id
        data['content_type'] = "docs"
    listening = insert_listening(data)
    listening.insert_listening()
    text = "Muaffaqiyatli yakunlandi"
    await CreateAdminState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=create_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(BACK_TEXT),
                    state=[CreateListeningState.file, CreateListeningState.begin])
async def back_listening_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Bosh menuga xush kelibsiz"
    await CreateAdminState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=create_markup())
