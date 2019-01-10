import os

currentDirectory = "/home/dale/Projects/testdirectory/"


for dirpath, dirnames, filenames in os.walk(currentDirectory):
    print dirpath
    if not os.listdir(dirpath):
        os.rmdir(dirpath)