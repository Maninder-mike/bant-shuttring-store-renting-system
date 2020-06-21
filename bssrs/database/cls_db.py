import sqlite3


class Database(object):
    """sqlite3 database class that holds testers jobs"""
    __DB_LOCATION = "/tester_db.db"

    def __init__(self, db_location=None):
        """Initialize db class variables"""
        if db_location is not None:
            self.connection = sqlite3.connect(db_location)
        else:
            self.connection = sqlite3.connect(self.__DB_LOCATION)
        self.cur = self.connection.cursor()

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()

    def execute(self, new_data):
        """execute a row of data to current cursor"""
        self.cur.execute(new_data)

    def executemany(self, many_new_data):
        """add many new data to database in one go"""
        self.create_table()
        self.cur.executemany('REPLACE INTO jobs VALUES(?, ?, ?, ?)', many_new_data)

    def create_table(self):
        """create a database table if it does not exist already"""
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS jobs(title text, job_id integer PRIMARY KEY, company text, age integer)''')

    def commit(self):
        """commit changes to database"""
        self.connection.commit()

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

    def __del__(self):
        self.connection.close()


db = Database
db.__doc__
