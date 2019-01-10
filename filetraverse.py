import os

currentDirectory = "/home/dale/Projects/"

for root, dirs, files in os.walk(currentDirectory):
    for file in files:
        if file.endswith(".jpg"):
            picFileDirectory = os.path.join(root, file)
            print picFileDirectory
                  
                  
                  