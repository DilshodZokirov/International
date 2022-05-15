from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    begin = State()
    language = State()
    name = State()
    phone_number = State()


class FinalRegisterState(StatesGroup):
    begin = State()


class SpeakingState(StatesGroup):
    final = State()
    begin = State()
    practice_debate = State()
    join = State()
    create = State()
    reply = State()


class PronunciationState(StatesGroup):
    begin = State()


class ListeningState(StatesGroup):
    begin = State()


class WritingState(StatesGroup):
    begin = State()


class SettingState(StatesGroup):
    begin = State()
    fullname = State()
    lang = State()
    level = State()


class AdminState(StatesGroup):
    language = State()
    begin = State()
    name = State()
    phone = State()
    active = State()


class CreateAdminState(StatesGroup):
    speaking_file = State()
    create_speaking = State()
    begin = State()


class PronunciationCreateState(StatesGroup):
    begin = State()
    name = State()
    file = State()


class CreateListeningState(StatesGroup):
    file = State()
    begin = State()
