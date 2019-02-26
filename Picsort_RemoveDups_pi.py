# Script Name:  PicSort_RemoveDups
# Author:       Steveo
# 
# Purpose:
# Script analyzes pictures for duplicates using a imagehash
# Duplicates are placed in the ~/Projects/duplicates folder
# Exif data from images is then use to create folders based on month/year picture taken
# Images are then move to their respective folder

import os
import sys
import exifread
from Tkinter import *
import Tkinter, tkFileDialog

from PIL import Image
import imagehash

import time

# Function creates folders by month and year
def createfolder(yearStamp, monthStamp, pictureFile, fileName):
    yearFilePath = outputDirectory + "/" + yearStamp
    #yearFilePath = "/home/dale/Projects/testoutput/" + yearStamp
    monthFilePath = outputDirectory + "/" + yearStamp + "/" + monthStamp
    #monthFilePath = "/home/dale/Projects/testoutput/" + yearStamp + "/" + monthStamp

    if not os.path.exists(yearFilePath):
        os.makedirs(yearFilePath)

    if not os.path.exists(monthFilePath):
        os.makedirs(monthFilePath)

    os.rename(pictureFile, monthFilePath + "/" + fileName)

# Function deletes empty directories
def removeemptydirectory():
    deletedDirectories = 0
    for dirpath, dirnames, filenames in os.walk(currentDirectory):
        if not os.listdir(dirpath):
            os.rmdir(dirpath)
            deletedDirectories = deletedDirectories + 1
    print deletedDirectories, "Directories removed"
    
def getfolderlocation(foldertitle): 
    root = Tk()
    root.withdraw()
    file_path = tkFileDialog.askdirectory(title = foldertitle)
    return file_path

#currentDirectory = "/home/dale/Projects/testdirectory/"
#currentDirectory = "/media/dale/6480F4E580F4BE9C/MyPictures/Summer/"
currentDirectory = getfolderlocation("Choose INPUT folder")
outputDirectory = getfolderlocation("Choose OUTPUT folder")

# Destination for duplicate pictures
duppath = getfolderlocation("DUPLICATES folder")


# log file to show what was moved/deleted/etc
fileName = "/home/dale/Projects/logfile.txt"
logOutput = open(fileName, 'a')

# Function creates folders based on file stamps
# Then moves the picture to the folder

count = 0
dupCount = 0
removedCount = 0
notRemoved = 0

imglist = []


# traverse directory for files
for root, dirs, files in os.walk(currentDirectory):
    for picFile in files:
        if picFile.endswith(".jpg") or picFile.endswith(".JPG"):
            picFileDirectory = os.path.join(root, picFile)

            pichash = imagehash.average_hash(Image.open(picFileDirectory))
      
            if pichash in imglist:
                print("found match")
                print(picFileDirectory)
                os.rename(picFileDirectory, duppath + "/" + picFile)
                dupCount += 1
            else:  # added to not put duplicate in list
                imglist.append(pichash)
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
                
print(count, "Files moved")
print(removedCount, "Files removed")
print(notRemoved, "Files not moved or removed")
print(dupCount, "Duplicate files placed in %s folder" % duppath)

localtime = time.asctime( time.localtime(time.time()) )

logOutput.write(localtime)
logOutput.write('\n')
logOutput.write(str(count) + ' Files moved\n')
logOutput.write(str(removedCount) + ' Files removed\n')
logOutput.write(str(notRemoved) + ' Files not removed\n')
logOutput.write('\n')
logOutput.close()

removeemptydirectory()