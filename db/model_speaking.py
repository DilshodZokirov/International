from db.transactions import Transactions
from utils import generate_unique_id


class Speaking(Transactions):
    def __init__(self, unique_id: str = None, name: str = None,
                 speaking: str = None, created_by: str = None, content_type: str = None):
        super().__init__()
        self.id = unique_id or generate_unique_id()
        self.name = name
        self.speaking = speaking
        self.created_by = created_by
        self.content_type = content_type

    def insert_speaking(self):
        sql: str = "insert into speaking(id, name, speaking,created_by,content_type) VALUES (%s,%s,%s,%s,%s)"
        params = (self.id, self.name, self.speaking, self.created_by, self.content_type)
        self.execute(sql, params, commit=True)

    def select_all_speak(self):
        sql: str = "select * from speaking"
        return self.execute(sql, fetchall=True)

    def select_by_document(self):
        sql: str = "select * from speaking where content_type = 'document'"
        return self.execute(sql, fetchall=True)

    def select_one_speak(self):
        sql: str = "select * from speaking where id=%s"
        params = (self.id,)
        return self.execute(sql, params, fetchone=True)

    def delete_speak(self):
        sql: str = "delete from speaking where id=%s and created_by=%s"
        params = (self.id, self.created_by)
        self.execute(sql, params, commit=True)

