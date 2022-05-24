from aiogram import types
from aiogram.dispatcher import FSMContext
from db.model_listening import Listening, ListeningMain
from buttons.buttons import CREATE_LISTENING_TEXT, back_markup, BACK_TEXT, create_markup, complete, COMPLETE_TEXT
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
    if message.text != BACK_TEXT:
        ListeningMain(name=message.text).insert_listening_main()
        text = "Marxamat listening uchun file tashlang (file,audio or video)"
        await CreateListeningState.file.set()
        await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=complete())
        return
    text = "Bosh menuga qaytdingiz"
    await CreateAdminState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=create_markup())


@dp.message_handler(content_types=types.ContentType.TEXT, state=CreateListeningState.file)
async def create_file_handler(message: types.Message, state: FSMContext):
    if message.text == COMPLETE_TEXT:
        text = "Muvaffaqiyatli qo'shildi"
        await CreateAdminState.begin.set()
        await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=create_markup())
    else:
        await message.delete()


@dp.message_handler(content_types=types.ContentType.AUDIO, state=CreateListeningState.file)
async def create_file_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        file_id = message.audio.file_id
        file_info = await bot.get_file(file_id=file_id)
        data['file'] = file_info.file_id
        data['created_by'] = message.chat.id
        data['content_type'] = "audio"
    last_object = ListeningMain().select_one_listening()
    Listening(listening=data['file'],created_by=data['created_by'],
              content_type=data['content_type'], listening_id=last_object[0]).insert_listening()


@dp.message_handler(content_types=types.ContentType.VIDEO, state=CreateListeningState.file)
async def create_file_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        file_id = message.video.file_id
        file_info = await bot.get_file(file_id=file_id)
        data['file'] = file_info.file_id
        data['created_by'] = message.chat.id
        data['content_type'] = "video"
    last_object = ListeningMain().select_one_listening()
    Listening(listening=data['file'],created_by=data['created_by'],
              content_type=data['content_type'], listening_id=last_object).insert_listening()


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=CreateListeningState.file)
async def create_file_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        file_id = message.document.file_id
        file_info = await bot.get_file(file_id=file_id)
        data['file'] = file_info.file_id
        data['created_by'] = message.chat.id
        data['content_type'] = "docs"
    last_object = ListeningMain().select_one_listening()
    Listening(listening=data['file'],created_by=data['created_by'],
              content_type=data['content_type'], listening_id=last_object).insert_listening()


@dp.message_handler(lambda message: str(message.text).__eq__(BACK_TEXT),
                    state=[CreateListeningState.file, CreateListeningState.begin])
async def back_listening_handler(message: types.Message):

    text = "Bosh menuga xush kelibsiz"
    await CreateAdminState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=create_markup())
