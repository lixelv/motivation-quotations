import sqlite3

class DB:
    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()
        self.do("""
        CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        quotation TEXT UNIQUE
        );""")
#         self.do("""
# CREATE TABLE IF NOT EXISTS user (
#     id INTEGER PRIMARY KEY UNIQUE NOT NULL,
#     name TEXT,
#     date DATETIME DEFAULT CURRENT_TIMESTAMP
#     );""")

    def do(self, sql, values=()) -> None:
        self.cursor.execute(sql, values)
        self.connect.commit()

    def read(self, sql, values=()) -> tuple:
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()

    def read_quotation(self):
        return self.read('SELECT quotation FROM data ORDER BY RANDOM() LIMIT 1;')[0][0]

    def write_data(self, quotation):
        try:
            self.do('INSERT INTO data(quotation) VALUES (?)', (quotation,))
        except sqlite3.IntegrityError as e:
            print(f'Повтор!!!  {e}')

    def user_exist(self, user_id) -> bool:
        return bool(self.read('SELECT id FROM user WHERE id = ?', (user_id,)))

    def new_user(self, user_id, username) -> None:
        self.do('INSERT INTO user(id, name) VALUES (?, ?)', (user_id, username))
