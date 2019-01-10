# Script to pull exif data from image file
# Exif data is then use to create new folder and move file
# to that folder

import os
# Other method forg getting exif data
import exifread

f = open('/home/dale/Projects/testdirectory/2012/07/testpic.jpg', 'rb')

tags = exifread.process_file(f)

print tags['Image DateTime']
print tags['EXIF DateTimeDigitized']
print tags['EXIF DateTimeOriginal']
print tags['Image Model']

dateTaken = str(tags['EXIF DateTimeOriginal'])
print "Date taken = ", dateTaken





print tags

