import os
import sqlite3

db_main = os.path.join(os.path.dirname(__file__), "database_main.db")


class Database:
    client = """
        id INT PRIMARY KEY,
        name TEXT NOT NULL,
        PRIORITY INT,
        project_id INT NOT NULL,
        status_id INT NOT NULL,
        begin_date DATE NOT NULL,
        end_date DATE NOT NULL,
        FOREIGN KEY (`project_id`) REFERENCES project(`id`)"""

    customer = """
    fname	TEXT NOT NULL,
    lname	TEXT NOT NULL,
    father TEXT,
    gender TEXT,
    street TEXT,
    city TEXT NOT NULL,
    pincode TEXT,
    number INT PRIMARY KEY NOT NULL UNIQUE,
    email TEXT,
    careof TEXT,
    creation_date DATETIME"""

    item = """
    item_id SMALLINT UNSIGNED NOT NULL,
    title VARCHAR(128) NOT NULL,
    description TEXT DEFAULT NULL,
    rental_duration TINYINT UNSIGNED NOT NULL DEFAULT 3,
    rental_rate DECIMAL(4,2) NOT NULL DEFAULT 4.99,
    replacement_cost DECIMAL(5,2) NOT NULL DEFAULT 19.99,
    last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY  (item_id)"""

    payment = """
    payment_id SMALLINT UNSIGNED NOT NULL,
    customer_id SMALLINT UNSIGNED NOT NULL,
    staff_id TINYINT UNSIGNED NOT NULL,
    rental_id INT DEFAULT NULL,
    amount DECIMAL(5,2) NOT NULL,
    payment_date DATETIME NOT NULL,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY  (payment_id)"""

    staff = """
    staff_id TINYINT UNSIGNED NOT NULL,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    address_id SMALLINT UNSIGNED NOT NULL,
    picture BLOB DEFAULT NULL,
    email VARCHAR(50) DEFAULT NULL,
    store_id TINYINT UNSIGNED NOT NULL,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    username VARCHAR(16) NOT NULL,
    password VARCHAR(40) DEFAULT NULL,
    last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY  (staff_id)"""

    book = """
    title TEXT UNIQUE,
    author TEXT,
    year INT,
    isbn INT PRIMARY KEY UNIQUE"""

    def __init__(self):
        super(Database, self).__init__()
        self.connect()

    def connect(self):
        conn = sqlite3.connect(db_main)
        cur = conn.cursor()
        cur.execute(f"CREATE TABLE IF NOT EXISTS `book` ({Database.book})")
        cur.execute(f"CREATE TABLE IF NOT EXISTS `customer` ({Database.customer})")
        cur.execute(f"CREATE TABLE IF NOT EXISTS `staff` ({Database.staff})")
        cur.execute(f"CREATE TABLE IF NOT EXISTS `payment` ({Database.payment})")
        cur.execute(f"CREATE TABLE IF NOT EXISTS `item` ({Database.item})")
        conn.commit()
        conn.close()

    def insert_customer(self, fname, lname, father, gender, street, city, pincode, number, email, careof,
                        creation_date):
        conn = sqlite3.connect(db_main)
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO `customer` VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                        (fname, lname, father, gender, street, city, pincode, number, email, careof, creation_date))
        except sqlite3.Error as e:
            print(e)
        print("Insert In customer!")
        conn.commit()
        conn.close()

    def view_all_customers(self):
        conn = sqlite3.connect(db_main)
        cur = conn.cursor()
        cur.execute("SELECT * FROM customer")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search_customer(self, title=""):
        conn = sqlite3.connect(db_main)
        cur = conn.cursor()
        cur.execute(f"SELECT {title} FROM customer")
        rows = cur.fetchall()
        conn.close()
        return rows

    # ==================================================================================================================

    def insert_book(self, title, author, year, isbn):
        conn = sqlite3.connect(db_main)
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO `book` VALUES(?,?,?,?)", (title, author, year, isbn))
        except sqlite3.Error as e:
            print(e)
        print("Insert Book!")
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
        print("Value Deleted")
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
