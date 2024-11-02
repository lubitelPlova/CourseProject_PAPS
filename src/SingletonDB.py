import sqlite3

class SingletonDB:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonDB, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect('users.db')
            cls._instance.cursor = cls._instance.conn.cursor()
        return cls._instance
    
    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()