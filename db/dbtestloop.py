# Script loops through picture files in target directory
# pulling EXIF data from each picture and putting into database


import dbdefs
import os
import exifread

from dbdefs import create_connection

sqlite_file = '/home/dale/Projects/db/dbtest.db' 

sql_create_pics_table = """CREATE TABLE IF NOT EXISTS picdata (
                            id integer,
                            PicName text, 
                            PicSize integer,
                            DateTime text,
                            ImageLength text,
                            ImageModel text
                            );"""

conn = create_connection(sqlite_file)
if conn is not None:
    dbdefs.create_table(conn, sql_create_pics_table)
    print("Success!")
else:
    print("Error")
    
currentDirectory = "/home/dale/Projects/testoutput/2009/07"


# Function creates folders based on file stamps
# Then moves the picture to the folder
counter = 1
count = 0
removedCount = 0
notRemoved = 0
# traverse directory for files
for root, dirs, files in os.walk(currentDirectory):
    for picFile in files:
        if picFile.endswith(".jpg") or picFile.endswith(".JPG"):
            picFileDirectory = os.path.join(root, picFile)

            f = open(picFileDirectory, 'rb')

            tags = exifread.process_file(f)
            
            iDT = str(tags['Image DateTime'])
            iIL = str(tags['EXIF ExifImageLength'])
            iIM = str(tags['Image Model'])

            picSize = os.path.getsize(picFileDirectory)
            print picSize
    
            with conn:
                pic = (counter, picFile, picSize, iDT, iIL, iIM)
                dbdefs.create_pic_entry(conn, pic)
            
            counter = counter + 1