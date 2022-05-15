from db.transactions import Transactions
from utils import generate_unique_id


class Writing(Transactions):
    def __init__(self, unique_id: str = None, name: str = None, writing: str = None, created_by: str = None,
                 content_type: str = None, w_type: str = None):
        super().__init__()
        self.id = unique_id or generate_unique_id()
        self.name = name
        self.writing = writing
        self.created_by = created_by
        self.content_type = content_type
        self.writing_type = w_type

    def select_all_writing(self):
        sql: str = "select * from writing"
        return self.execute(sql, fetchall=True)

    def select_one_writing(self):
        sql: str = "select * from writing where id=%s"
        params = (self.id,)
        return self.execute(sql, params, fetchone=True)

    def insert_writing(self):
        sql: str = "insert into writing(id, name, writing, created_by, type, content_type) VALUES (%s,%s,%s,%s,%s,%s)"
        params = (self.id, self.name, self.writing, self.created_by, self.writing_type, self.content_type)
        self.execute(sql, params, commit=True)
