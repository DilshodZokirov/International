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


class AdminState(StatesGroup):
    language = State()
    begin = State()
    name = State()
    phone = State()
    active = State()
