import dbdefs
import os
import exifread

from dbdefs import create_connection

sqlite_file = '/home/dale/Projects/db/dbtest.db' 

conn = create_connection(sqlite_file)
    
currentDirectory = "/home/dale/Projects/testoutput/2009/07"

with conn: 
    pic_id = 225
    stuff = dbdefs.select_pic(conn, pic_id)
    print stuff
    tableName = 'picdata'
    dbdefs.clear_table(conn, tableName)