from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.buttons import WRITING_TEXT
from dispatch import dp
from states import FinalRegisterState, WritingState


@dp.message_handler(lambda message: str(message.text).__eq__(WRITING_TEXT), state=FinalRegisterState.begin)
async def writing_handlers(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Yozuv bo'limiga xush kelibsiz"
    await WritingState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id)
