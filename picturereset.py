# Script used in conjunction with picsort_traverse to reset for testing
# Script will put all the pictures in folders created by picscort_traverse back in one folder

import os
import exifread
from Tkinter import *
import Tkinter, tkFileDialog


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

currentDirectory = getfolderlocation()


# Function creates folders based on file stamps
# Then moves the picture to the folder
originalFilePath = "/home/dale/Projects/originals"
count = 0
removedCount = 0
notRemoved = 0
# traverse directory (root) for subdirectories (dir) and for files (files)
for root, dirs, files in os.walk(currentDirectory):
    for picFile in files:
        if picFile.endswith(".jpg") or picFile.endswith(".JPG"):
            picFileDirectory = os.path.join(root, picFile)
            movedPicFile = originalFilePath + "/" + picFile
            os.rename(picFileDirectory, movedPicFile)
            
            count += 1
                
print (count, "Files moved")

removeemptydirectory()
removeemptydirectory()