# Script to pull exif data from image file
# Exif data is then use to create new folder and move file
# to that folder

import os
import PIL.Image

# cycle through each picture (jpg) file in directory
currentDirectory = "/home/dale/Projects/filetest"
count = 0
for picFile in os.listdir(currentDirectory):
    if picFile.endswith(".jpg") or picFile.endswith(".JPG"):
        print picFile
        img = PIL.Image.open(picFile)
        exif_data = img._getexif()
        print picFile
        print exif_data
        
        dateTakenexif = exif_data[36867]
        yearTaken = dateTakenexif[0:4]
        monthTaken = dateTakenexif[5:7]
        print "Date taken exif = ", dateTakenexif
        print yearTaken
        print monthTaken
        
        count = count + 1
        print picFile
        
print count

#*************************************
#img = PIL.Image.open('20151016_183816.jpg')
#exif_data = img._getexif()

# print exif_data

#yearTaken = dateTakenexif[0:4]
#monthTaken = dateTakenexif[5:7]

# Create folder for picture files
#yearFilePath = "/home/dale/Projects/" + yearTaken
#monthFilePath = "/home/dale/Projects/" + yearTaken + "/" + monthTaken
#if not os.path.exists(yearFilePath):
#    os.makedirs(yearFilePath)
    
#if not os.path.exists(monthFilePath):
#    os.makedirs(monthFilePath)

#resultsFile = "results.txt"
#
#target = open(resultsFile, 'w')
#target.write(dateTakenexif)
#target.close

#
# Move file to new directory created above
#os.rename("20151016_183816.jpg", monthFilePath + "/20151016_183816.jpg")

#currentDirectory = "/home/dale/Projects"
#count = 0
#for picFile in os.listdir(currentDirectory):
#    if picFile.endswith("jpg"):
#        count = count + 1
#        print picFile
#        
#print count
    
    