from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.buttons import PRONUNCIATION_TEXT, pronunciation_markup, BACK_TEXT, home_menu
from dispatch import dp
from states import FinalRegisterState, PronunciationState


@dp.message_handler(lambda message: str(message.text).__eq__(PRONUNCIATION_TEXT), state=FinalRegisterState.begin)
async def pronunciation_handler(message: types.Message, state: FSMContext):
    text = "Talaffuz bo'limiga xush kelibsiz"
    await PronunciationState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=pronunciation_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(BACK_TEXT), state=PronunciationState.begin)
async def back_a_home_menu(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Bosh menu"
    await FinalRegisterState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=home_menu())
