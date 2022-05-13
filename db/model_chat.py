from db.transactions import Transactions
from utils import generate_unique_id


class Chat(Transactions):
    def __init__(self, unique_id: str = None, user_id: str = None, chat_id: str = None, level: str = None):
        super().__init__()
        self.id = unique_id or generate_unique_id()
        self.user_id = user_id
        self.chat_id = chat_id
        self.level = level

    def all_chat(self):
        sql: str = "select * from chat where chat_id=%s"
        params = (self.chat_id,)
        return self.execute(sql, params, fetchall=True)

    def create_chat(self):
        sql: str = "insert into chat(id, user_id, chat_id, level) VALUES (%s,%s,%s,%s)"
        params = (self.id, self.user_id, self.chat_id, self.level)
        return self.execute(sql, params, commit=True)

    def user_select(self):
        sql: str = "select * from chat where chat_id=%s"
        params = (self.chat_id,)
        return self.execute(sql, params, fetchall=True)

    def user_select_one_id(self):
        sql: str = "Select * from chat where  user_id=%s"
        params = (self.user_id,)
        return self.execute(sql, params, fetchone=True)

    def delete_chat(self, user_id):
        sql: str = "delete from chat where user_id=%s"
        params = (user_id,)
        return self.execute(sql, params, commit=True)

    def delete_created_by_chat(self, chat_id):
        sql: str = "delete from chat where chat_id=%s"
        params: tuple = (chat_id,)
        return self.execute(sql, params, commit=True)
