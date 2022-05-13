from db.transactions import Transactions
from utils import generate_unique_id


class User(Transactions):
    def __init__(self,
                 unique_id: str = None,
                 language: str = None,
                 phone: str = None,
                 name: str = None,
                 chat_id: str = None):
        super().__init__()
        self.id = unique_id or generate_unique_id()
        self.language = language
        self.phone = phone
        self.name = name
        self.chat_id = chat_id

    def insert_user(self):
        sql: str = "insert into users(id, language, phone, name, chat_id) VALUES (%s,%s,%s,%s,%s)"
        params = (self.id, self.language, self.phone, self.name, self.chat_id)
        return self.execute(sql, params, commit=True)

    def registered_user(self):
        sql: str = "select * from users where chat_id=%s"
        params = (self.chat_id,)
        return self.execute(sql, params, fetchone=True)
