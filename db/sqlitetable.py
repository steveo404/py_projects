import sqlite3
from sqlite3 import Error

sqlite_file = '/home/dale/Projects/db/pythonsqlite.db'    # name of the sqlite database file
table_picdata = 'tblpicdata'  # name of the table to be created
new_field = 'picID' # name of the column
field_type = 'INTEGER'  # column data type

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a  table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn=table_picdata, nf=new_field, ft=field_type))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()