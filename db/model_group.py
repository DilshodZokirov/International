from typing import List

from db.dto import GroupDTO
from db.transactions import Transactions
from utils import generate_unique_id


class Group(Transactions):
    def __init__(self, unique_id: str = None, name: str = None, created_by: str = None):
        super().__init__()
        self.id = unique_id or generate_unique_id()
        self.name = name
        self.created_by = created_by

    def select_all_groups(self):
        sql: str = "select * from groups"
        groups = self.execute(sql, fetchall=True)
        groups_dto: List[GroupDTO] = []
        for group in groups:
            groups_dto.append(GroupDTO(unique_id=group[0], name=group[1], created_by=group[2]))
        return groups_dto

    def insert_group(self):
        sql: str = "insert into groups(id, name, created_by) VALUES (%s,%s,%s)"
        params = (self.id, self.name, self.created_by)
        return self.execute(sql, params, commit=True)

    def select_created_by(self):
        sql: str = "select * from groups where created_by=%s"
        params = (self.created_by,)
        return self.execute(sql, params, fetchone=True)

    def delete_group(self, created_by):
        sql: str = "delete from groups where created_by=%s"
        params = (created_by,)
        self.execute(sql, params, commit=True)
