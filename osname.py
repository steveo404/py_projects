import os
from sys import platform
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root = Tk()
root.withdraw()
file_path = tkFileDialog.askdirectory()

print file_path

def platformidentity():
    if platform == "linux2":
        platformtype = "Linux"
    elif platform == "win32":
        platformtype = "Linux"
    elif platform == "win64":
        platformtype = "Linux"
        
    return platformtype

print platformidentity()