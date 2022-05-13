from aiogram import types
from aiogram.dispatcher import FSMContext

from buttons.buttons import SETTING_TEXT, settings_markup
from dispatch import dp
from states import FinalRegisterState, SettingState


@dp.message_handler(lambda message: str(message.text).__eq__(SETTING_TEXT), state=FinalRegisterState)
async def settings_handlers(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    text = "Settings bo'limi"
    await SettingState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=settings_markup())
