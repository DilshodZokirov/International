from typing import List

from db.dto import MaterialDto
from db.transactions import Transactions
from utils import generate_unique_id


class Materials(Transactions):
    def __init__(self,id: str = None, name: str = None,
                 material: str = None, created_by: str = None, content_type: str = None,):
        super().__init__()
        self.id = id or generate_unique_id()
        self.name = name
        self.material = material
        self.created_by = created_by
        self.content_type = content_type

    def insert_material(self):
        sql: str = "insert into material(id, name, material,created_by,content_type) VALUES (%s,%s,%s,%s,%s)"
        params = (self.id, self.name, self.material, self.created_by, self.content_type)
        self.execute(sql, params, commit=True)

    def select_all_speak(self):
        sql: str = "select * from material"
        return self.execute(sql, fetchall=True)

    def select_all_speak_find(self , material_name):
        sql: str = "select * , REGEXP_MATCHES(name , %s) from material"
        param = (f'^{material_name}',)
        materials = self.execute(sql, param, fetchall=True)

        materials_dto: List[MaterialDto] = []
        for material in materials:
            materials_dto.append(MaterialDto(material[0], material[1], material[2], material[3], material[4]))

        return materials_dto

    def select_by_document(self):
        sql: str = "select * from material where content_type = 'document'"
        return self.execute(sql, fetchall=True)

    def select_by_video(self):
        sql: str = "select * from material where content_type = 'video'"
        return self.execute(sql, fetchall=True)

    def select_by_audio(self):
        sql: str = "select * from material where content_type = 'audio'"
        return self.execute(sql, fetchall=True)

    def select_one_material(self):
        sql: str = "select * from material where id=%s"
        params = (self.id,)
        return self.execute(sql, params, fetchone=True)

    def delete_speak(self, _id):
        sql: str = "delete from material where id=%s"
        params = (_id,)
        self.execute(sql, params, commit=True)




