
# Group renaming, works with all types of files
# Be sure to put the files you want in a folder beforehand

from tkinter import *     
import os
from tkinter import filedialog
from tkinter import messagebox as mb
import pathlib
import datetime
import time
from operator import itemgetter

def renaming():
    global renamingfiles
    global renamingfolder
    # Obtaining the file names
    renamingfolder = filedialog.askdirectory()
    renamingfiles = sorted(os.listdir(renamingfolder))

    # Changing the path to viable format, see images for reference, we want zrename
    i = 0
    while i != len(renamingfolder):
        if renamingfolder[i] == "/":
            renamingfolder = renamingfolder[:i] + "\\\\" + renamingfolder[i + 1:] 
        i += 1
    
    sorting()

    filenaming()

def sorting():
    global sortingfiles
    sortingfiles = []
    for image in renamingfiles:
        # Check for if it is a folder, cuz issues
        if os.path.isdir(renamingfolder + "\\\\" + image):
            continue
        sortingfiles.append([image])
    
    i = 0
    while i != len(sortingfiles):
        oldfilepath = renamingfolder + "\\\\" + sortingfiles[i][0]
        fname = pathlib.Path(oldfilepath)
        ctime = datetime.datetime.fromtimestamp(fname.stat().st_ctime)
        ctime = time.mktime(ctime.timetuple())
        sortingfiles[i].append(ctime)
        i += 1

    sortingfiles = sorted(sortingfiles, key=itemgetter(1), reverse=True)


def filenaming():
    # Obtaining the prefix
    prefix = entrybox.get() + "_"

    i = 0
    while i != len(sortingfiles):
        templen = len(sortingfiles[i][0]) - 1
        while sortingfiles[i][0][templen] != ".":
            templen = templen - 1
        # .jpg, .png etc
        extension = sortingfiles[i][0][templen:]
        newfilepath = renamingfolder + "\\\\" + prefix + str((i + 1)) + extension
        oldfilepath = renamingfolder + "\\\\" + sortingfiles[i][0]
        os.rename(oldfilepath,newfilepath)
        i += 1
    mb.showinfo('confirmation', "Done!")

# Showing the screen
root = Tk()
root.geometry("300x150")

Label(root, text="Group File Renamer", font=("Helvetica", 20), fg="blue").pack(pady="10")
Label(root, text="Enter the prefix in the box below FIRST", font=("Helvetica", 10), fg="black").pack()
entrybox = Entry(root, width = 30)
entrybox.pack()
Button(root, text = "Choose folder", command = renaming).pack(pady="10")

root.mainloop()