from db.transactions import Transactions
from utils import generate_unique_id


class Listening(Transactions):
    def __init__(self, unique_id: str = None, name: str = None, listening: str = None, created_by: str = None,
                 content_type: str = None):
        super().__init__()
        self.id = unique_id or generate_unique_id()
        self.name = name
        self.listening = listening
        self.created_by = created_by
        self.content_type = content_type

    def select_all_listening(self):
        sql: str = "select * from listening"
        return self.execute(sql, fetchall=True)

    def select_one_listening(self):
        sql: str = "select * from listening where id=%s"
        params = (self.id,)
        return self.execute(sql, params, fetchone=True)

    def insert_listening(self):
        sql: str = "insert into listening(id, listening, name, created_by, content_type) VALUES (%s,%s,%s,%s,%s)"
        params = (self.id, self.listening, self.name, self.created_by, self.created_by)
        self.execute(sql, params, commit=True)
