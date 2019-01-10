# Script to pull exif data from image file
# Exif data is then use to create new folder and move file
# to that folder

import os
import exifread

currentDirectory = "/home/dale/Projects/testdirectory"

# Function creates folders based on file stamps
# Then moves the picture to the folder
def createfolder(yearStamp, monthStamp, pictureFile):
    yearFilePath = "/home/dale/Projects/testoutput/" + yearStamp
    monthFilePath = "/home/dale/Projects/testoutput/" + yearStamp + "/" + monthStamp
    
    if not os.path.exists(yearFilePath):
        os.makedirs(yearFilePath)
    
    if not os.path.exists(monthFilePath):
        os.makedirs(monthFilePath)
        
    os.rename(pictureFile, monthFilePath + "/" + picFile)
    

count = 0
# traverse directory for files
#for root, dirs, files in os.walk(currentDirectory):
#    for file in files:
#        if file.endswith(".jpg") or file.endswith(".JPG"):
            
# cycle through each picture (jpg) file in directory
for picFile in os.listdir(currentDirectory):
    if picFile.endswith(".jpg") or picFile.endswith(".JPG"):
        
        picFileDirectory = currentDirectory + "/" + picFile
        
        f = open(picFileDirectory, 'rb')

        tags = exifread.process_file(f)
        
        if tags['EXIF DateTimeDigitized']:
            dateTakenexif = str(tags['EXIF DateTimeDigitized'])
            yearTaken = dateTakenexif[0:4]
            monthTaken = dateTakenexif[5:7]

            createfolder(yearTaken, monthTaken, picFileDirectory)
                        
        count = count + 1

print count, "Files moved"
