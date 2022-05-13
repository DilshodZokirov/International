import sqlite3

import psycopg2

from configs.constants import DB_NAME, DB_PASSWORD, DB_USERNAME, DB_HOST, DB_PORT


class Transactions:
    def __init__(self) -> None:
        self.connect = psycopg2.connect(dbname=DB_NAME,
                                        user=DB_USERNAME, password=DB_PASSWORD,
                                        host=DB_HOST, port=DB_PORT)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        connection = self.connect
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters or tuple())
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data
