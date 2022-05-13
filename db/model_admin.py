from db.transactions import Transactions
from utils import generate_unique_id


class Admin(Transactions):
    def __init__(self, unique_id: str = None, name: str = None, phone: str = None, language: str = None,
                 pending: str = None, chat_id: str = None):
        super().__init__()
        self.id = unique_id or generate_unique_id()
        self.name = name
        self.phone = phone
        self.language = language
        self.pending = pending
        self.chat_id = chat_id

    def select_admin_registered(self):
        sql: str = "select * from admin where chat_id=%s"
        params = (self.chat_id,)
        return self.execute(sql, params, fetchone=True)

    def insert_admin(self):
        sql: str = "insert into admin(id, name, phone, language,chat_id) VALUES (%s,%s,%s,%s,%s)"
        params = (self.id, self.name, self.phone, self.language, self.chat_id)
        return self.execute(sql, params, commit=True)
