from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import os

root = Tk()
root.withdraw()
file_path = tkFileDialog.askdirectory()

print file_path

count = 50

print count

# log file to show what was moved/deleted/etc
fileName = "/home/dale/Projects/dialogtestfile.txt"

logOutput = open(fileName, 'a')
#logOutput.truncate

logOutput.write(str(count) + " ")
logOutput.write("Files moved" + " ")
logOutput.write(file_path)
logOutput.write('\n')
logOutput.close()