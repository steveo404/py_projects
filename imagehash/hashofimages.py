# Script analyzes pictures for duplicates using a imagehash
# Duplicates are placed in the ~/Projects/duplicates folder

from Tkinter import *

import os
import exifread
import Tkinter, tkFileDialog

from PIL import Image
import imagehash

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

# Request folder location of pictures to be analyzed
currentDirectory = getfolderlocation()


# Function creates folders based on file stamps
# Then moves the picture to the folder
originalFilePath = "/home/dale/Projects/originals"
duppath = "/home/dale/Projects/duplicates"
count = 0
removedCount = 0
notRemoved = 0

imglist = []

# traverse directory for files
for root, dirs, files in os.walk(currentDirectory):
    for picFile in files:
        if picFile.endswith(".jpg") or picFile.endswith(".JPG"):
            picFileDirectory = str(os.path.join(root, picFile))

            pichash = imagehash.average_hash(Image.open(picFileDirectory))
            #print(pichash)
            if pichash in imglist:
                print("found match")
                print(picFileDirectory)
                os.rename(picFileDirectory, duppath + "/" + picFile)
            else:  # added to not put duplicate in list
                imglist.append(pichash)

            
            count += 1
                
print (count)

