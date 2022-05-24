from db.model_admin import Admin
from db.model_listening import Listening
from db.model_pronunciation import Materials
from db.model_speaking import Speaking
from db.model_user import User


def user_insert(data: dict):
    return User(
        language=data.get('lang'),
        phone=data.get('phone'),
        name=data.get('name'),
        chat_id=data.get('chat_id')
    )


def admin_insert(data: dict):
    return Admin(
        name=data.get('name'),
        phone=data.get('phone'),
        language=data.get('lang'),
        pending="ACTIVE",
        chat_id=data.get('chat_id')
    )


def insert_speaking(data: dict):
    return Speaking(
        name=data.get("name"),
        speaking=data.get('speaking_file'),
        created_by=data.get('created_by'),
        content_type=data.get('content_type')
    )


def insert_pronunciation(data: dict):
    return Materials(
        name=data.get('name'),
        material=data.get('file'),
        created_by=data.get('created_by'),
        content_type=data.get('content_type')
    )


def insert_listening(data: dict):
    return Listening(
        # name=data.get('name'),
        listening=data.get('file'),
        content_type=data.get("content_type"),
        created_by=data.get("created_by"),
    )
