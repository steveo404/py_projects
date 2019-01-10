import sqlite3
from sqlite3 import Error

sqlite_file = '/home/dale/Projects/db/pythonsqlite2.db'    # name of the sqlite database file

def create_connection(db_file):
    """create a database connection to the SQLite database
       specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        
    return None

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_pic_entry(conn, pic):
    """Create a new pic in the pics_table table 
    :param conn:
    :param pic:
    :return: id
    """
    sql = """INSERT INTO picdata(id, DateTime, DateTimeDigitized, ImageLength, ImageModel)
             VALUES(?,?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, pic)
    return cur.lastrowid


sql_create_pics_table = """CREATE TABLE IF NOT EXISTS picdata (
                            id integer PRIMARY KEY,
                            name text NOT NULL,
                            date_of_pic text,
                            size_of_pic integer
                            );"""
                            
conn = create_connection(sqlite_file)
if conn is not None:
    create_table(conn, sql_create_pics_table)
    with conn:
        pic = (123, "Family", '2015-1-1', 150)
        pic_result = create_pic_entry(conn, pic)

    print("Success!")
    print(pic_result)
else:
    print("Error")


#if __name__ == '__main__':
#    main()
