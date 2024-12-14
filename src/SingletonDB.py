import sqlite3
import threading
import logging

class SingletonDB:
    _local = threading.local()

    def __init__(self):
        if not hasattr(self._local, 'conn'):
            self._local.conn = sqlite3.connect('users.db')
            self._local.cursor = self._local.conn.cursor()

    def execute(self, query, params=()):
        try:
            self._local.cursor.execute(query, params)
        except sqlite3.Error as e:
            print(f"Ошибка {e}")
        return self._local.cursor.fetchall()
    
    def commit(self):
        self._local.conn.commit()

    def close(self):
        self._local.conn.close()