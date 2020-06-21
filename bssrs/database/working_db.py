import sqlite3
import os
import datetime

from PyQt5.QtSql import QSqlDatabase

db_path = os.path.join(os.path.dirname(__file__), "main_db.db")

main_item_garder = """CREATE TABLE IF NOT EXISTS `garder` (
garder_7 TEXT,
garder_8 TEXT,
garder_9 TEXT,
garder_10 TEXT,
garder_11 TEXT,
garder_12 TEXT,
garder_13 TEXT,
garder_14 TEXT,
garder_15 TEXT,
garder_16 TEXT,
garder_17 TEXT,
garder_18 TEXT,
garder_19 TEXT,
garder_20 TEXT
);"""

main_item_fatte = """CREATE TABLE IF NOT EXISTS `fatte` (
fatte_1 TEXT,
fatte_2 TEXT,
`fatte_2.6` TEXT,
`fatte_3` TEXT,
`fatte_3.3` TEXT,
`fatte_3.6` TEXT,
fatte_4 TEXT
);"""

bill_db = """CREATE TABLE IF NOT EXISTS `bill_base` (
bills TEXT NOT NULL
);"""

sql_create_customer_table = """ CREATE TABLE IF NOT EXISTS "customer" (
"fname"	text NOT NULL,
"lname"	text NOT NULL,
"father"	text NOT NULL,
"gender"	text NOT NULL,
"street"	text NOT NULL,
"city"	text NOT NULL,
"pincode"	text NOT NULL,
"number"	text NOT NULL,
"email"	text NOT NULL,
"careof"	text NOT NULL,
PRIMARY KEY("number")
);"""

sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS `tasks` (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                priority integer,
                                status_id integer NOT NULL,
                                project_id integer NOT NULL,
                                begin_date text NOT NULL,
                                end_date text NOT NULL,
                                FOREIGN KEY (project_id) REFERENCES `customer` (number));"""


def create():
    global conn
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        print("Database created and Successfully Connected to SQLite")
        try:
            cursor.execute(sql_create_customer_table)
            cursor.execute(sql_create_tasks_table)
            cursor.execute(main_item_garder)
            cursor.execute(bill_db)
            cursor.execute(main_item_fatte)
            conn.commit()
            print("SQLite table created")
            cursor.close()
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)

    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()
        print("The SQLite connection is closed")


def insert_client(edit_fname, edit_lname, edit_father, edit_gender, edit_street, edit_city, edit_pincode, edit_number,
                  edit_email, edit_careof):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO `customer` VALUES(?,?,?,?,?,?,?,?,?,?)",
                   (edit_fname, edit_lname, edit_father, edit_gender, edit_street, edit_city, edit_pincode, edit_number,
                    edit_email, edit_careof))
    conn.commit()
    conn.close()


def read():
    pass


def update():
    pass


def delete():
    pass


if __name__ == '__main__':
    create()
    read()
    update()
    delete()


def create_client_data(edit_fname=None, edit_lname=None, edit_father=None, edit_gender=None, edit_street=None,
                       edit_city=None, edit_pincode=None, edit_number=None, edit_email=None, edit_careof=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    if edit_fname.get() == "" or edit_lname.get() == "" or edit_father.get() == "" or edit_gender.get() == "" or \
            edit_street.get() == "" or edit_city.get() == "" or edit_pincode.get() == "" or edit_number.get() == "" or \
            edit_email.get() == "" or edit_careof.get() == "":
        print('Error Command:', 'Empty box not created')
    else:
        cursor.execute(
            "INSERT INTO `customer` (fname, lname, father, gender, street, city, pincode, number, email, "
            "careof) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (edit_fname, edit_lname, edit_father, edit_gender, edit_street, edit_city, edit_pincode, edit_number,
             edit_email, edit_careof))
    conn.commit()
    # FIRSTNAME.set("")
    # LASTNAME.set("")
    # ADDRESS1.set("")
    # ADDRESS2.set("")
    # ADDRESS3.set("")
    # ADDRESS4.set("")
    # GENDER.set("")
    # PHONE1.set("")
    # PHONE2.set("")
    # EMAIL.set("")
    # REF1.set("")
    # REF2.set("")
    cursor.close()
    conn.close()
    print('Data Inserted:', 'All is Down.')
    return
