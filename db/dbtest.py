import dbdefs
import os
import exifread

from dbdefs import create_connection

sqlite_file = '/home/dale/Projects/db/dbtest.db' 

sql_create_pics_table = """CREATE TABLE IF NOT EXISTS picdata (
                            id integer PRIMARY KEY,
                            DateTime text NOT NULL,
                            DateTimeDigitized text,
                            DateTimeOriginal text,
                            ImageLength text,
                            ImageModel text
                            );"""

conn = create_connection(sqlite_file)
if conn is not None:
    dbdefs.create_table(conn, sql_create_pics_table)
    print("Success!")
else:
    print("Error")
    



f = open('/home/dale/Projects/testdirectory/2012/07/testpic.jpg', 'rb')

tags = exifread.process_file(f)

iDT = str(tags['Image DateTime'])
iDDT = str(tags['EXIF DateTimeDigitized'])
iDTO = str(tags['EXIF DateTimeOriginal'])
iIL = str(tags['EXIF ExifImageLength'])
iIM = str(tags['Image Model'])


counter = 3

print counter
print iIM

with conn:
        pic = (counter, iDT, iDDT, iDTO, iIL, iIM)
        dbdefs.create_pic_entry(conn, pic)
