from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.buttons import SPEAKING_WITH_A_PARTNER_TEXT, speaking_markup, BACK_TEXT, home_menu, DEBATE_TEXT, \
    debate_markup, JOIN_CHAT_TEXT, CREATE_CHAT_TEXT, begin_markup, BEGIN_TEXT, back_markup, end_markup, END_TEXT
from buttons.inline import all_groups
from db.model_chat import Chat
from db.model_group import Group
from db.model_user import User
from dispatch import dp, bot
from states import FinalRegisterState, SpeakingState


@dp.message_handler(lambda message: str(message.text).__eq__(SPEAKING_WITH_A_PARTNER_TEXT),
                    state=FinalRegisterState.begin)
async def speaking_with_a_partner_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Sherik bilan gaplashish bo'limiga xush kelibsiz!"
    await SpeakingState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=speaking_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(DEBATE_TEXT), state=SpeakingState.begin)
async def debate_user_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Marxamat practica qilaszmi yoki debate"
    await SpeakingState.practice_debate.set()
    await message.bot.send_message(text=text, chat_id=str(message.chat.id), reply_markup=debate_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(BACK_TEXT), state=SpeakingState.practice_debate)
async def back_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Marxamat bosh menu"
    await SpeakingState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=speaking_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(JOIN_CHAT_TEXT), state=SpeakingState.practice_debate)
async def join_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        groups = all_groups()
        if groups:
            text = "Marxamat birini tanlang"
            await SpeakingState.join.set()
            await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=all_groups())
            return
        text = "Ulanish uchun guruh yo'q"
        await message.bot.send_message(text=text, chat_id=message.chat.id)
        return


@dp.callback_query_handler(state=SpeakingState.join)
async def all_groups_handler(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if not query.data.__eq__('back'):
            await query.message.delete()
            text = "Marxamat begin tugmasini bosing"
            message = query.data.split('+')
            chat_id = message[1]
            data['user_id'] = chat_id
            Chat(user_id=str(query.message.chat.id), chat_id=chat_id, level="ELEMENTARY").create_chat()
            await SpeakingState.final.set()
            await query.message.bot.send_message(text=text, chat_id=str(query.message.chat.id),
                                                 reply_markup=begin_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(CREATE_CHAT_TEXT), state=SpeakingState.practice_debate)
async def group_create(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Marxamat chatga nom qo'ying"
    await SpeakingState.create.set()
    await message.bot.send_message(
        text=text,
        chat_id=message.chat.id,
        reply_markup=back_markup()
    )


@dp.message_handler(state=SpeakingState.create)
async def create_group_finish(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if not message.text.__eq__(BACK_TEXT):
            text = "Marxamat begin tugmasini bosing"
            Group(name=message.text, created_by=str(message.chat.id)).insert_group()
            select_created_user = Group(created_by=str(message.chat.id)).select_created_by()
            user = User(chat_id=str(message.chat.id)).registered_user()
            Chat(chat_id=select_created_user[2], user_id=str(message.chat.id), level=user[5]).create_chat()
            data['user_id'] = user[4]
            await SpeakingState.final.set()
            await message.bot.send_message(text=text, chat_id=str(message.chat.id), reply_markup=begin_markup())
            return
        text = "Marxamat bosh menu"
        await SpeakingState.practice_debate.set()
        await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=debate_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(BEGIN_TEXT), state=SpeakingState.final)
async def chat_all_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    user = User(chat_id=str(message.chat.id)).registered_user()
    text = f"<i>{user[3]} chatga ulandi</i>"
    await SpeakingState.reply.set()
    all_chat_users = Chat(chat_id=data['user_id']).all_chat()
    for user in all_chat_users:
        await message.bot.send_message(text=text, chat_id=str(user[1]),
                                       reply_markup=end_markup(),
                                       parse_mode=types.ParseMode.HTML)


@dp.message_handler(content_types=types.ContentType.VIDEO, state=SpeakingState.reply)
async def video_message(video: types.Message, state: FSMContext):
    async with state.proxy() as data:
        file_info = await bot.get_file(file_id=video.video.file_id)
        all_chat_users = Chat(chat_id=data['user_id']).all_chat()
        if all_chat_users:
            for user in all_chat_users:
                if not user[1] == str(video.chat.id):
                    users = User(chat_id=str(video.chat.id)).registered_user()
                    await SpeakingState.reply.set()
                    await video.bot.send_video(
                        chat_id=str(user[1]),
                        video=file_info.file_id,
                        caption=f'Author:{users[3]}')
            return


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=SpeakingState.reply)
async def document_handler(video: types.Message, state: FSMContext):
    async with state.proxy() as data:
        file_info = await bot.get_file(file_id=video.document.file_id)
        all_chat_users = Chat(chat_id=data['user_id']).all_chat()
        if all_chat_users:
            for user in all_chat_users:
                if not user[1] == str(video.chat.id):
                    users = User(chat_id=str(video.chat.id)).registered_user()
                    await SpeakingState.reply.set()
                    await video.bot.send_document(
                        chat_id=str(user[1]),
                        document=file_info.file_id,
                        caption=f'Author:{users[3]}')
            return


@dp.message_handler(content_types=types.ContentType.VOICE, state=SpeakingState.reply)
async def voice_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        file_info = await bot.get_file(file_id=message.voice.file_id)
        all_chat_users = Chat(chat_id=data['user_id']).all_chat()
        if all_chat_users:
            for user in all_chat_users:
                if not user[1] == str(message.chat.id):
                    users = User(chat_id=str(message.chat.id)).registered_user()
                    await SpeakingState.reply.set()
                    await message.bot.send_voice(
                        chat_id=str(user[1]),
                        voice=file_info.file_id,
                        caption=f'Author:{users[3]}')
            return


@dp.message_handler(content_types=types.ContentType.PHOTO, state=SpeakingState.reply)
async def voice_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        file_info = await bot.get_file(file_id=message.photo[-1].file_id)
        all_chat_users = Chat(chat_id=data['user_id']).all_chat()
        if all_chat_users:
            for user in all_chat_users:
                if not user[1] == str(message.chat.id):
                    users = User(chat_id=str(message.chat.id)).registered_user()
                    await SpeakingState.reply.set()
                    await message.bot.send_photo(
                        chat_id=str(user[1]),
                        photo=file_info.file_id,
                        caption=f'Author:{users[3]}')
            return


@dp.message_handler(state=SpeakingState.reply)
async def user_reply_chat(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if not message.text.__eq__(END_TEXT):
            all_chat_users = Chat(chat_id=data['user_id']).all_chat()
            if all_chat_users:
                for user in all_chat_users:
                    if not user[1] == str(message.chat.id):
                        users = User(chat_id=str(message.chat.id)).registered_user()
                        await SpeakingState.reply.set()
                        await message.bot.send_message(
                            text=f'{users[3]}:{message.text}',
                            chat_id=str(user[1]), parse_mode=types.ParseMode.MARKDOWN)
                return
            text = "Uzr chat yakunlandi"
            await SpeakingState.practice_debate.set()
            await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=debate_markup())
            return
        user = Group(created_by=str(message.chat.id)).select_created_by()
        if not user:
            Chat().delete_chat(user_id=str(message.chat.id))
        else:
            Group().delete_group(created_by=str(message.chat.id))
            Chat().delete_created_by_chat(chat_id=str(message.chat.id))
        text = "Bosh menu"
        await SpeakingState.practice_debate.set()
        await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=debate_markup())
        return


@dp.message_handler(lambda message: str(message.text).__eq__(BACK_TEXT), state=SpeakingState.begin)
async def back_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Marxamat bosh menu"
    await FinalRegisterState.begin.set()
    await message.bot.send_message(text=text, chat_id=str(message.chat.id), reply_markup=home_menu())
