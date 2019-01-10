# Remove spaces from file names

import os

currentDirectory = "/home/dale/Projects/testspaceremove"
count = 0
for picFile in os.listdir(currentDirectory):
    if picFile.endswith(".jpg") or picFile.endswith(".JPG"):
        print picFile
        
        if picFile.find(" ") > 0:
        
            newPicFile = picFile.replace(" ", "")
            print newPicFile
        
            os.rename(currentDirectory + "/" + picFile, currentDirectory + "/" + newPicFile)
            count = count + 1
            
        #f = open(picFile, 'rb')
        
        
        
print count