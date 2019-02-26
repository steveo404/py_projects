# Script Name:  DupProfile
# Author:       Steveo
# 
# Purpose:
# Script analyzes pictures for duplicates using a imagehash
# Captures the details and prints it out to a log file

import os
import sys
import exifread
from Tkinter import *
import Tkinter, tkFileDialog

from PIL import Image
import imagehash

import time

    
def getfolderlocation(foldertitle): 
    root = Tk()
    root.withdraw()
    file_path = tkFileDialog.askdirectory(title = foldertitle)
    return file_path

def logPicOutput(pyear, pmonth, pdirectory, pfile):
    logOutput = open(logFile, 'a')
    logOutput.write(pyear)
    logOutput.write(",")
    logOutput.write(pmonth)
    logOutput.write(",")
    logOutput.write(pdirectory)
    logOutput.write(",")
    logOutput.write(pfile)
    logOutput.write('\n')
    logOutput.close()

#currentDirectory = "/home/dale/Projects/testdirectory/"
#currentDirectory = "/media/dale/6480F4E580F4BE9C/MyPictures/Summer/"
currentDirectory = getfolderlocation("Choose INPUT folder")


# Destination for duplicate pictures
#duppath = getfolderlocation("DUPLICATES folder")


# log file to show picture profiles
#logFileLocation = getfolderlocation("Choose LOG FILE location")
logFile = "/home/dale/Projects/Duplogfile.txt"

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
                logPicOutput(yearTaken, monthTaken, picFileDirectory, picFile)
            elif tags.get('EXIF DateTimeDigitized'):
                dateTakenexif = str(tags['EXIF DateTimeDigitized'])
                yearTaken = dateTakenexif[0:4]
                monthTaken = dateTakenexif[5:7]
                logPicOutput(yearTaken, monthTaken, picFileDirectory, picFile)
            else:
                yearTaken = ""
                monthTaken = ""


