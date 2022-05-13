from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.buttons import LISTENING_TEXT, listening_markup, BACK_TEXT, home_menu
from dispatch import dp
from states import FinalRegisterState, ListeningState


@dp.message_handler(lambda message: str(message.text).__eq__(LISTENING_TEXT), state=FinalRegisterState.begin)
async def listening_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Tinglash bo'limiga xush kelibsiz"
    await ListeningState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=listening_markup())


@dp.message_handler(lambda message: str(message.text).__eq__(BACK_TEXT), state=ListeningState.begin)
async def back_a_home_menu(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Bosh menu"
    await FinalRegisterState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=home_menu())
