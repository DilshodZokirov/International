from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from configs.constants import BOT_TOKEN, STORAGE_PATH
from aiogram.contrib.fsm_storage.files import JSONStorage

storage = JSONStorage(STORAGE_PATH)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)

if __name__ == '__main__':
    print(STORAGE_PATH)
