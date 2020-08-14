import sqlite3
from sqlite3 import Error

database = r"sqlite.db"


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_customer(conn, project):
    sql = '''INSERT INTO `customer` (
    fname, 
    lname, 
    father, 
    gender, 
    street, 
    city, 
    pincode, 
    number, 
    email, 
    careof
    ) VALUES(?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid


def create_task(conn, task):
    sql = ''' INSERT INTO `tasks`(name,priority,status_id,project_id,begin_date,end_date) VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid


def update_task(conn, task):
    sql = ''' UPDATE `tasks` SET priority = ? , begin_date = ? , end_date = ? WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


def delete_task(conn, id):
    sql = 'DELETE FROM `tasks` WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_projects(conn, id):
    sql = 'DELETE FROM `customer` WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_all_tasks(conn):
    sql = 'DELETE FROM `tasks`'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def delete_all_projects(conn):
    sql = 'DELETE FROM `customer`'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM `tasks`")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_priority(conn, priority):
    cur = conn.cursor()
    cur.execute("SELECT * FROM `tasks` WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS customer (
                                        id integer PRIMARY KEY,
                                        fname text NOT NUlL,
                                        lname text NOT NUlL,
                                        father text NOT NUlL,
                                        gender text NOT NUlL,
                                        street text NOT NUlL,
                                        city text NOT NUlL,
                                        pincode text NOT NUlL,
                                        number text NOT NUlL,
                                        email text NOT NUlL,
                                        careof text NOT NUlL
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES customer (id)
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create customer table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")

    with conn:
        # create a new project
        project = (
        'maninder', 'singh', 'bantsingh', 'male', 'cunagraroad', 'patran', '147105', 'mike@gmail.com', 'No one')
        project = create_customer(conn, project)

        # tasks
        task_1 = ('Analyze the requirements of the app', 1, 1, project, '2015-01-01', '2015-01-02')
        task_2 = ('Confirm with user about the top requirements', 1, 1, project, '2015-01-03', '2015-01-05')

        # create tasks
        create_task(conn, task_1)
        create_task(conn, task_2)

    with conn:
        update_task(conn, (2, '2020-01-04', '2025-01-06', 2))


def delete_options():
    # create a database connection
    conn = create_connection(database)
    # with conn:
    #     delete_task(conn, 2)
    #     # delete_all_tasks(conn);
    with conn:
        delete_projects(conn, 1)


def delete_all():
    conn = create_connection(database)

    with conn:
        delete_all_tasks(conn)
        delete_all_projects(conn)


def fetch():
    # create a database connection
    conn = create_connection(database)
    with conn:
        # print("1. Query task by priority:")
        # select_task_by_priority(conn, 2)

        print("2. Query all tasks")
        select_all_tasks(conn)


if __name__ == '__main__':
    main()
