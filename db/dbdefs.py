import sqlite3
from sqlite3 import Error


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
    sql = """INSERT INTO picdata(id, PicName, PicSize, DateTime, ImageLength, ImageModel)
             VALUES(?,?,?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, pic)
    #return cur.lastrowid

def select_pic(conn, pic_id):
    """Query pic database for matching picture"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM picdata WHERE id=?", (pic_id,))

    rows = cur.fetchall()
    return rows

def clear_table(conn, tableName):
    sql = 'DELETE FROM ' + tableName
    cur = conn.cursor()
    cur.execute(sql)

def check_table_exists(conn, tableName):
    sql = "SELECT count(*) FROM sqlite_master WHERE type = 'table' AND name = " + tableName
    cur = conn.cursor()
    cur.execute(sql)
