import sqlite3
import os

class Database:
    def __init__(self, db_name="data/recipes.db"):
        os.makedirs(os.path.dirname(db_name), exist_ok=True)
        
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            ingredients TEXT,
            instructions TEXT,
            category TEXT,
            difficulty TEXT,
            duration INTEGER
        )
        """
        self.connection.execute(query)
        self.connection.commit()

    def execute_query(self, query, params=()):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor

    def close(self):
        self.connection.close()
