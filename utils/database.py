import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('p3.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user(
                id integer primary key,
                name varchar not null,
                age integer not null,
                address varchar,
                photo varchar)
        """)

    def add_user(self, name, age, address, photo):
        self.cursor.execute("""
            INSERT INTO user (name, age, address, photo)
            VALUES (?, ?, ?, ?)""",
        (name, age, address, photo))
        self.connection.commit()

    def all_user(self):
        users = self.cursor.execute("""
            SELECT * FROM user""").fetchall()
        return users

db = Database()
