from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root = Tk()
root.withdraw()
file_path = tkFileDialog.askdirectory()

print file_path