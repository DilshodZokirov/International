from db.model_user import User
from .users import *
from .admin import *
from buttons.buttons import register_button
from dispatch import dp
from configs.constants import BOT_NAME
from states import RegisterState, FinalRegisterState


@dp.message_handler(commands=['start'], state='*')
async def cmd_start(message: types.Message):
    user = User(chat_id=str(message.chat.id)).registered_user()
    if not user:
        await RegisterState.begin.set()
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=f"Assalomu alaykum {message.from_user.first_name} bizning {BOT_NAME} ga xush kelibsiz iltimos register tugmasini bosing",
                                       reply_markup=register_button())
        return
    text = "Marxamat bosh menu"
    await FinalRegisterState.begin.set()
    await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=home_menu())
