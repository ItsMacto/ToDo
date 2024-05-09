import sqlite3

class DB:
    def __init__(self, db_path='todo.db'):
        self.db_path = db_path

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        return self.cursor  

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
            print(f'Error: {exc_type}')
            if exc_val:
                print(f'Error value: {exc_val}')
            if exc_tb:
                print(f'Trace back: {exc_tb}')
        else:
            self.conn.commit()
        self.cursor.close()
        self.conn.close()

    @staticmethod
    def setup_database(db_path='todo.db'):
        with DB(db_path) as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    due_date DATETIME,
                    completed BOOLEAN NOT NULL DEFAULT 0
                )''')

DB.setup_database()
