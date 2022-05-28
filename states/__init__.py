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
    name = State()
    files = State()


class ListeningState(StatesGroup):
    begin = State()


class ListeningGetState(StatesGroup):
    file = State()


class AdminWritingState(StatesGroup):
    begin = State()
    name = State()
    file = State()


class WritingState(StatesGroup):
    begin = State()
    names = State()
    file = State()


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


class DeleteAdminState(StatesGroup):
    begin = State()


class DeleteWritingState(StatesGroup):
    begin = State()
    deleting = State()


class PronunciationCreateState(StatesGroup):
    begin = State()
    name = State()
    file = State()


class CreateListeningState(StatesGroup):
    file = State()
    begin = State()




class ProductDeleteState(StatesGroup):
    begin = State()

class DeleteListeningState(StatesGroup):
    name = State()
    show_listening = State()
    delete = State()


class PronunciationDeleteState(StatesGroup):
    name = State()
    show_pronunciation = State()
    delete = State()


class WritingDeleteState(StatesGroup):
    name = State()
    show_writing = State()
    delete = State()
