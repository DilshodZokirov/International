from aiogram import types
from aiogram.dispatcher import FSMContext
from buttons.inline import listening_names
from buttons.buttons import LISTENING_TEXT, listening_markup, BACK_TEXT, home_menu
from db.model_listening import Listening
from dispatch import dp, bot
from states import FinalRegisterState, ListeningState, ListeningGetState


@dp.message_handler(lambda message: str(message.text).__eq__(LISTENING_TEXT), state=FinalRegisterState.begin)
async def listening_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Tinglash bo'limiga xush kelibsiz"
    text2 = "Listeninglar ni nomi bo'yicha tanlang"
    await ListeningState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=types.ReplyKeyboardRemove())
    await message.bot.send_message(text=text2, chat_id=message.chat.id, reply_markup=listening_names())


@dp.callback_query_handler(state=ListeningState.begin)
async def listening_file_handler(query: types.CallbackQuery):
    await query.message.delete()
    if query.data != BACK_TEXT:
        documents = Listening(listening_id=query.data).select_by_document()
        video = Listening(listening_id=query.data).select_by_video()
        audio = Listening(listening_id=query.data).select_by_audio()
        if documents:
            for i in documents:
                file_info = await bot.get_file(file_id=i[1])
                await query.message.bot.send_document(document=file_info.file_id, chat_id=query.message.chat.id)
        if video:
            for i in video:
                file_info = await bot.get_file(file_id=i[1])
                await query.message.bot.send_video(video=file_info.file_id, chat_id=query.message.chat.id)
        if audio:
            for i in audio:
                file_info = await bot.get_file(file_id=i[1])
                await query.message.bot.send_audio(audio=file_info.file_id, chat_id=query.message.chat.id)

        await FinalRegisterState.begin.set()
        await query.message.bot.send_message(text="Muvaffaqiyatli jo'natildi", chat_id=query.message.chat.id,
                                             reply_markup=home_menu())
    else:
        text = "Bosh menu ⬅️"
        await FinalRegisterState.begin.set()
        await query.message.bot.send_message(text=text, chat_id=query.message.chat.id, reply_markup=home_menu())


@dp.message_handler(lambda message: str(message.text).__eq__(BACK_TEXT), state=ListeningState.begin)
async def back_a_home_menu(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Bosh menu"
    await FinalRegisterState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=home_menu())
