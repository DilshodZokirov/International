from typing import List

from db.dto import ListeningDto
from db.transactions import Transactions
from utils import generate_unique_id


class ListeningMain(Transactions):
    def __init__(self, unique_id: str = None, name: str = None):
        super().__init__()
        self.id = unique_id
        self.name = name

    def insert_listening_main(self):
        sql: str = "insert into listening_main(name) VALUES (%s)"
        params = (self.name,)
        self.execute(sql, params, commit=True)

    def select_one_listening(self):
        sql: str = "select max(id) from listening_main"
        return self.execute(sql, fetchone=True)

    def select_all_listening_main(self):
        sql: str = "select * from listening_main"
        return self.execute(sql,  fetchall=True)

    def delete_listening_main(self):
        sql: str = "delete from listening_main where id = %s"
        params = (self.id,)
        self.execute(sql, params,commit=True)


class Listening(Transactions):
    def __init__(self, unique_id: str = None, listening_id: int = None, listening: str = None, created_by: str = None,
                 content_type: str = None):
        super().__init__()
        self.id = unique_id or generate_unique_id()
        self.listening = listening
        self.created_by = created_by
        self.content_type = content_type
        self.listening_id = listening_id

    def select_all_listening(self):
        sql: str = "select * from listening where listening_id = %s"
        params = (self.listening_id,)
        return self.execute(sql,params, fetchall=True)

    def select_one_listening(self):
        sql: str = "select * from listening where id=%s"
        params = (self.id,)
        return self.execute(sql, params, fetchone=True)

    def select_by_document(self):
        sql: str = "select * from listening where listening_id = %s and content_type = 'docs'"
        params = (self.listening_id,)
        return self.execute(sql, params, fetchall=True)

    def select_by_video(self):
        sql: str = "select * from listening where listening_id = %s and content_type = 'video'"
        params = (self.listening_id,)
        return self.execute(sql, params, fetchall=True)

    def select_by_audio(self):
        sql: str = "select * from listening where listening_id = %s and content_type = 'audio'"
        params = (self.listening_id,)
        return self.execute(sql, params, fetchall=True)

    def insert_listening(self):
        sql: str = "insert into listening(id, listening, created_by, content_type, listening_id) " \
                   "VALUES (%s,%s,%s,%s,%s)"
        params = (self.id, self.listening, self.created_by, self.content_type,self.listening_id)
        self.execute(sql, params, commit=True)

    def delete_listening(self , _id):
        sql : str = 'delete from listening where id = %s'
        param = (_id , )
        return self.execute(sql , param , commit=True)



