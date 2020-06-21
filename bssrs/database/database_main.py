import os
import sqlite3

from PyQt5.QtWidgets import QMessageBox

db_main = os.path.join(os.path.dirname(__file__), "timegm.db")


class Database:
    client = """
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        PRIORITY INTEGER,
        project_id INTEGER NOT NULL,
        status_id INTEGER NOT NULL,
        begin_date DATE NOT NULL,
        end_date DATE NOT NULL,
        FOREIGN KEY (`project_id`) REFERENCES project(`id`)"""

    customer = """
    id INTEGER PRIMARY KEY,
    fname	text,
    lname	text,
    father text,
    gender text,
    street text,
    city text,
    pincode text,
    number INTEGER,
    email text,
    careof text,
    creation_date text,
    UNIQUE (number)"""

    book = """id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    year INTEGER,
    isbn INTEGER,
    UNIQUE (title)"""

    def __init__(self):
        super(Database, self).__init__()
        self.connect()

    def garders(self):
        for x in range(7, 21):
            return f"Garder-{x}"

    def error(self):
        message = QMessageBox.information("title", "this is not allows")
        return message

    def connect(self):
        conn = sqlite3.connect(db_main)
        cur = conn.cursor()
        cur.execute(f"CREATE TABLE IF NOT EXISTS `book` ({Database.book})")
        cur.execute(f"CREATE TABLE IF NOT EXISTS `customer` ({Database.customer})")
        conn.commit()
        conn.close()

    def insert_book(self, title, author, year, isbn):
        conn = sqlite3.connect(db_main)
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO `book` VALUES(NULL,?,?,?,?)", (title, author, year, isbn))
        except sqlite3.Error as e:
            print(e)
            self.error()
        print("Insert Book!")
        conn.commit()
        conn.close()

    def insert_customer(self, fname, lname, father, gender, street, city, pincode, number, email, careof,
                        creation_date):
        conn = sqlite3.connect(db_main)
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO `customer` VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?)",
                        (fname, lname, father, gender, street, city, pincode, number, email, careof, creation_date))
        except sqlite3.Error as e:
            print(e)

            self.error()
        print("Insert In customer!")
        conn.commit()
        conn.close()

    def view_all(self):
        conn = sqlite3.connect(db_main)
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        conn = sqlite3.connect(db_main)
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",
                    (title, author, year, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self, id):
        conn = sqlite3.connect(db_main)
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def update(self, id, title, author, year, isbn):
        conn = sqlite3.connect(db_main)
        cur = conn.cursor()
        cur.execute("UPDATE book SET title =?, author =?, year =?, isbn =? WHERE id =?",
                    (title, author, year, isbn, id))
        conn.commit()
        conn.close()


db = Database()
db.connect()

# db.insert("another novel", "James W.", 2017, random.random())
# db.insert("world", "Singh", datetime.datetime.today().date(), random.random())
# db.insert_book("world", "Singh", datetime.datetime.today().date(), random.random())
# db.update(1, title="book", author="pink", year=1992, isbn=5555)
# m = db.search(author="mike")

# db.insert_customer(9872855415, 'mike', 'maninder', datetime.datetime.today(), random.random())
# db.insert_customer(123456789, 'tim', 'tommy', datetime.datetime.today(), random.random())

print("Database Called")
