from db.transactions import Transactions
from utils import generate_unique_id


class Writing(Transactions):
    def __init__(self, unique_id: str = None, name: str = None, writing: str = None, created_by: str = None,
                 content_type: str = None):
        super().__init__()
        self.id = unique_id or generate_unique_id()
        self.name = name
        self.writing = writing
        self.created_by = created_by
        self.content_type = content_type

    def select_all_writing(self):
        sql: str = "select * from writing"
        return self.execute(sql, fetchall=True)

    def select_one_writing(self):
        sql: str = "select * from writing where id=%s"
        params = (self.id,)
        return self.execute(sql, params, fetchone=True)

    def insert_writing(self):
        sql: str = "insert into writing(id, name, writing_file, created_by, topic_type) VALUES (%s,%s,%s,%s,%s)"
        params = (self.id, self.name, self.writing, self.created_by,  self.content_type)
        self.execute(sql, params, commit=True)

    def get_writing_by_topic(self):
        sql: str = "select * from writing where topic_type= %s"
        params = (self.content_type,)
        return self.execute(sql, params, fetchall=True)

    def delete_writing_by_id(self):
        sql: str = "delete from writing where id = %s"
        params = (self.id,)
        return self.execute(sql,params,commit=True)


class WritingTopic(Transactions):
    def __init__(self, unique_id: str = None, name: str = None):
        super().__init__()
        self.id = unique_id or generate_unique_id()
        self.name = name

    def select_all_writing(self):
        sql: str = "select * from writing_topic"
        return self.execute(sql, fetchall=True)

    def select_one_writing(self):
        sql: str = "select * from writing_topic where id=%s"
        params = (self.id,)
        return self.execute(sql, params, fetchone=True)

    def insert_writing(self):
        sql: str = "insert into writing_topic(id, name) VALUES (%s,%s)"
        params = (self.id, self.name)
        self.execute(sql, params, commit=True)

