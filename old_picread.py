# Script to pull exif data from image file
# Exif data is then use to create new folder and move file
# to that folder

import os
# Other method forg getting exif data
import exifread

f = open('/media/dale/6480F4E580F4BE9C/MyPictures/CRW_6047.jpg', 'rb')

tags = exifread.process_file(f)

print tags['Image DateTime']
print tags['EXIF DateTimeDigitized']
print tags['EXIF DateTimeOriginal']

dateTaken = str(tags['EXIF DateTimeOriginal'])
print "Date taken = ", dateTaken

print len(dateTaken)

yearTaken = dateTaken[0:4]
monthTaken = dateTaken[5:7]

# Create folder for picture files

yearFilePath = "/home/dale/Projects/" + yearTaken
monthFilePath = "/home/dale/Projects/" + yearTaken + "/" + monthTaken
if not os.path.exists(yearFilePath):
    os.makedirs(yearFilePath)
    
if not os.path.exists(monthFilePath):
    os.makedirs(monthFilePath)
    
# Move file to new directory created above
os.rename("20151016_183816.jpg", monthFilePath + "/20151016_183816.jpg")

currentDirectory = "/home/dale/Projects"
count = 0
for picFile in os.listdir(currentDirectory):
    if picFile.endswith("jpg"):
        count = count + 1
        print picFile
        
print count
    
    