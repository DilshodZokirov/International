from db.model_admin import Admin
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
