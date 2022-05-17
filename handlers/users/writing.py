from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from buttons.buttons import WRITING_TEXT, BACK_TEXT, home_menu
from buttons.inline import writing_topics_markup, get_writings_by_topics
from db.model_writing import WritingTopic, Writing
from dispatch import dp, bot
from states import FinalRegisterState, WritingState


@dp.message_handler(lambda message: str(message.text).__eq__(WRITING_TEXT), state=FinalRegisterState.begin)
async def writing_handlers(message: types.Message, state: FSMContext):
    text1 = "Writing bo'limiga xush kelibsiz"
    text = "Kategoriyani tanlang"
    await WritingState.begin.set()
    await message.bot.send_message(text=text1, chat_id=message.chat.id, reply_markup=ReplyKeyboardRemove())
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=writing_topics_markup())


@dp.callback_query_handler(state=WritingState.begin)
async def writing_topics(query: types.CallbackQuery, state: FSMContext):
    await query.message.delete()
    if query.data != BACK_TEXT:
        writing = WritingTopic(unique_id=query.data).select_one_writing()
        text = "Writingni nomlari orqali tanlang"
        async with state.proxy() as data:
            data['topic_id'] = writing[0]
        await WritingState.next()
        await query.message.bot.send_message(text=text, chat_id=query.message.chat.id,
                                             reply_markup=get_writings_by_topics(writing[0]))

    else:
        text = 'Bosh menu'
        await FinalRegisterState.begin.set()
        await query.message.bot.send_message(text=text, chat_id=query.message.chat.id, reply_markup=home_menu())


@dp.callback_query_handler(state=WritingState.names)
async def get_file(query: types.CallbackQuery, state: FSMContext):
    await query.message.delete()
    if query.data != BACK_TEXT:
        writing = Writing(unique_id=query.data).select_one_writing()
        file_info = await bot.get_file(file_id=writing[4])
        await query.message.bot.send_document(document=file_info.file_id, chat_id=query.message.chat.id)
    else:
        await FinalRegisterState.begin.set()
        await query.message.bot.send_message(text="Bosh menu", chat_id=query.message.chat.id, reply_markup=home_menu())


