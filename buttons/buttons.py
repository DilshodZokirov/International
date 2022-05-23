from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

MOVIES_TEXT = "📺 Movies"
CARTOONS_TEXT = "🎥 Cartoons"
DOCUMENTARIES_TEXT = "📄 Documentaries"
REGISTER_BUTTON_TEXT = "®️Register"
REGISTER_BUTTON = KeyboardButton(text=REGISTER_BUTTON_TEXT)
PHONE_NUMBER_TEXT = "📱 Telefon"
PHONE_NUMBER = KeyboardButton(text=PHONE_NUMBER_TEXT, request_contact=True)
MATERIALS = "📚 Materials"
EDIT_LANGUAGE_TEXT = "🇺🇿 Edit Language"
EDIT_USERNAME_TEXT = "👤 Edit Fullname"
EDIT_PHONE_TEXT = "📱 Edit Phone"
EDIT_LEVEL_TEXT = "🎚 Edit Level"
MY_CABINET_TEXT = "👨‍💻 My Cabinet"
CREATE_MATERIALS = "📚 Materials"

EDIT_LANGUAGE = KeyboardButton(text=EDIT_LANGUAGE_TEXT)
EDIT_USERNAME = KeyboardButton(text=EDIT_USERNAME_TEXT)
EDIT_PHONE = KeyboardButton(text=EDIT_PHONE_TEXT)
EDIT_LEVEL = KeyboardButton(text=EDIT_LEVEL_TEXT)
MY_CABINET = KeyboardButton(text=MY_CABINET_TEXT)

JOIN_CHAT_TEXT = "⏬ Join"
CREATE_CHAT_TEXT = "📌 Create Speaking"

JOIN_CHAT = KeyboardButton(text=JOIN_CHAT_TEXT)
CREATE_CHAT = KeyboardButton(text=CREATE_CHAT_TEXT)

SPEAKING_WITH_A_PARTNER_TEXT = "🗣 Speaking with partner"
PRONUNCIATION_TEXT = "🔉 Pronunciation"
WRITING_TEXT = "✍️Writing"
LISTENING_TEXT = "🎧 Listening"
SETTING_TEXT = "⚙️Settings"
BACK_TEXT = "🔙 Orqaga"
PRACTICE_TEXT = "📖 Practice"
DEBATE_TEXT = "👥 Debate"
BRITISH_TEXT = "🇬🇧 British"
AMERICAN_TEXT = "🇺🇸 American"
DOCUMENTARIES = KeyboardButton(text=DOCUMENTARIES_TEXT)
MOVIES = KeyboardButton(text=MOVIES_TEXT)
CARTOONS = KeyboardButton(text=CARTOONS_TEXT)
SPEAKING_WITH_A_PARTNER = KeyboardButton(text=SPEAKING_WITH_A_PARTNER_TEXT)
PRONUNCIATION = KeyboardButton(text=PRONUNCIATION_TEXT)
WRITING = KeyboardButton(text=WRITING_TEXT)
LISTENING = KeyboardButton(text=LISTENING_TEXT)
SETTINGS = KeyboardButton(text=SETTING_TEXT)
# ELEMENTARY = KeyboardButton(text=ELEMENTARY_TEXT)
# PRE_INTERMEDIATE = KeyboardButton(text=PRE_INTERMEDIATE_TEXT)
# INTERMEDIATE = KeyboardButton(text=INTERMEDIATE_TEXT)
# UPPER_INTERMEDIATE = KeyboardButton(text=UPPER_INTERMEDIATE_TEXT)
# ADVANCED = KeyboardButton(text=ADVANCED_TEXT)
BACK = KeyboardButton(text=BACK_TEXT)
PRACTICE = KeyboardButton(text=PRACTICE_TEXT)
DEBATE = KeyboardButton(text=DEBATE_TEXT)
BRITISH = KeyboardButton(text=BRITISH_TEXT)
AMERICAN = KeyboardButton(text=AMERICAN_TEXT)


def settings_markup():
    row1 = [EDIT_LANGUAGE, EDIT_USERNAME]
    row2 = [EDIT_LEVEL]
    row3 = [MY_CABINET, BACK]
    keyboard = [row1, row2, row3]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


def listening_markup():
    row1 = [MOVIES, CARTOONS]
    row2 = [DOCUMENTARIES, BACK]
    keyboard = [row1, row2]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


def pronunciation_markup():
    row1 = [BRITISH, AMERICAN]
    row2 = [BACK]
    keyboard = [row1, row2]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


def speaking_markup():
    row1 = [PRACTICE, DEBATE]
    row2 = [BACK]
    keyboard = [row1, row2]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


def back_markup():
    row1 = [BACK]
    keyboard = [row1]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


BEGIN_TEXT = "🏟 Begin"
BEGIN = KeyboardButton(text=BEGIN_TEXT)
END_TEXT = "🔚 End"
END = KeyboardButton(text=END_TEXT)


def end_markup():
    row1 = [END]
    keyboard = [row1]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


def begin_markup():
    row1 = [BEGIN]
    row2 = [BACK]
    keyboard = [row1, row2]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


# def type_internship():
#     row1 = [ELEMENTARY]
#     row2 = [PRE_INTERMEDIATE, INTERMEDIATE, UPPER_INTERMEDIATE]
#     row3 = [ADVANCED]
#     row4 = [BACK]
#     return ReplyKeyboardMarkup(resize_keyboard=True)


def materials_markup():
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    audio = KeyboardButton(text="Audio")
    video = KeyboardButton(text="Video")
    docs = KeyboardButton(text="Document")
    back = KeyboardButton(text=BACK_TEXT)
    buttons.add(audio,video, docs)
    buttons.add(back)
    return buttons


def home_menu():
    row1 = [SPEAKING_WITH_A_PARTNER, MATERIALS]
    row2 = [WRITING, LISTENING]
    row3 = [SETTINGS]
    keyboard = [row1, row2, row3]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


def phone_number_button():
    row1 = [PHONE_NUMBER]
    keyboard = [row1]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


def register_button():
    row1 = [REGISTER_BUTTON]
    keyboard = [row1]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


def debate_markup():
    row1 = [JOIN_CHAT, CREATE_CHAT]
    row2 = [BACK]
    keyboard = [row1, row2]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


# ADMIN_PROPERTIES_TEXT = "👨‍💻 Admin Properties"
# ADMIN_CREATE = "️ Create Admin"
CREATE_TEXT = "☑ Created"
DELETE_TEXT = "❌ Delete"
# ADMIN_PROPERTIES = KeyboardButton(text=ADMIN_PROPERTIES_TEXT)
CREATE = KeyboardButton(text=CREATE_TEXT)
DELETE = KeyboardButton(text=DELETE_TEXT)
CREATE_SPEAKING_PRACTICE_TEXT = "🔉 Speaking Practice"
CREATE_LISTENING_TEXT = "🎧 Listening"
CREATE_PRONUNCIATION_TEXT = "👂 Pronunciation"
CREATE_WRITING_TEXT = "📝 Writing"
CREATE_SPEAKING_PRACTICE = KeyboardButton(text=CREATE_SPEAKING_PRACTICE_TEXT)
CREATE_LISTENING = KeyboardButton(text=CREATE_LISTENING_TEXT)
CREATE_PRONUNCIATION = KeyboardButton(text=CREATE_PRONUNCIATION_TEXT)
CREATE_WRITING = KeyboardButton(text=CREATE_WRITING_TEXT)


def admin_markup():
    row1 = [CREATE, DELETE]
    row2 = [SETTINGS]
    keyboard = [row1, row2]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


def create_markup():
    row1 = [CREATE_SPEAKING_PRACTICE, CREATE_LISTENING]
    row2 = [CREATE_MATERIALS, CREATE_WRITING]
    row3 = [BACK]
    keyboard = [row1, row2, row3]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)

