# Script to pull exif data from image file
# Exif data is then use to create new folder and move file
# to that folder

import os
import exifread
from Tkinter import *
import Tkinter, tkFileDialog

def createfolder(yearStamp, monthStamp, pictureFile, fileName):
    yearFilePath = "/home/dale/Projects/testoutput/" + yearStamp
    monthFilePath = "/home/dale/Projects/testoutput/" + yearStamp + "/" + monthStamp

    if not os.path.exists(yearFilePath):
        os.makedirs(yearFilePath)

    if not os.path.exists(monthFilePath):
        os.makedirs(monthFilePath)

    os.rename(pictureFile, monthFilePath + "/" + fileName)

def removeemptydirectory():
    deletedDirectories = 0
    for dirpath, dirnames, filenames in os.walk(currentDirectory):
        if not os.listdir(dirpath):
            os.rmdir(dirpath)
            deletedDirectories = deletedDirectories + 1
    print deletedDirectories, "Directories removed"
    
def getfolderlocation(): 
    root = Tk()
    root.withdraw()
    file_path = tkFileDialog.askdirectory()
    return file_path

#currentDirectory = "/home/dale/Projects/testdirectory/"
#currentDirectory = "/media/dale/6480F4E580F4BE9C/MyPictures/Summer/"
currentDirectory = getfolderlocation()

# log file to show what was moved/deleted/etc
fileName = "/home/dale/Projects/logfile.txt"

logOutput = open(fileName, 'w')
logOutput.truncate


# Function creates folders based on file stamps
# Then moves the picture to the folder

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
            # Search for possible tags in file - 'Image DateTime' or 'EXIF DateTimeDigitized'
            # Tags may not be available and file will be skipped
            if tags.get('Image DateTime'):
                dateTakenexif = str(tags['Image DateTime'])
                yearTaken = dateTakenexif[0:4]
                monthTaken = dateTakenexif[5:7]
                createfolder(yearTaken, monthTaken, picFileDirectory, picFile)
                count = count + 1
            elif tags.get('EXIF DateTimeDigitized'):
                dateTakenexif = str(tags['EXIF DateTimeDigitized'])
                yearTaken = dateTakenexif[0:4]
                monthTaken = dateTakenexif[5:7]
                createfolder(yearTaken, monthTaken, picFileDirectory, picFile)
                count = count + 1
            else:
                yearTaken = ""
                monthTaken = ""
        # Remove legacy Windows Thumbs.db files
        elif picFile.endswith(".db"):
            dbFileDirectory = os.path.join(root, picFile)
            print picFile
            try:
                os.remove(dbFileDirectory)
                removedCount = removedCount + 1
            except OSError:
                pass
        else:
            notRemoved = notRemoved + 1
                
print count, "Files moved"
print removedCount, "Files removed"
print notRemoved, "Files not moved or removed"

logOutput.write("Files moved")
logOutput.close()

removeemptydirectory()