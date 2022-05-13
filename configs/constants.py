from environs import Env
from pathlib import Path
from os.path import join as join_path

BASE_URL = Path(__file__).parent.parent
env = Env()
env.read_env()
BOT_TOKEN = env.str('BOT_TOKEN')
BOT_NAME = env.str('BOT_NAME')
DB_PORT = env.str("DB_PORT")
DB_USERNAME = env.str("DB_USERNAME")
DB_NAME = env.str("DB_NAME")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_HOST = env.str("DB_HOST")
STORAGE_PATH = join_path(BASE_URL, 'configs', 'mystates.json')
PAYMENTS_PROVIDER_TOKEN = env.str("PAYMENTS_PROVIDER_TOKEN")
LOG_PATH = join_path(BASE_URL, 'configs', 'log.log')
