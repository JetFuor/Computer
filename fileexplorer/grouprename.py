# Set up the screen
# Button to click on
# Obtain location of the files
# Get names
# Figure out way to convert to the correct pathing
# to the correct chosen file
# Choose a starter for all the files
# Increment and append the name for each file
# Seems simple, DO IT YOU FUCK

from tkinter import *
import shutil         
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb

# MY VERSION
def renaming():
    # OBTAINING FILE NAMES
    folderlocation = filedialog.askdirectory()
    renamingfiles=sorted(os.listdir(folderlocation))

    # ASKING FOR WHAT TO RENAME IT TO
    prefix = input("Enter starting prefix for all images: ") + "_"

    # CHANGING THE PATHING AND RENAMING EACH FILE
    renamingfolder = folderlocation
    i = 0
    while True:
        if i == len(renamingfolder):
            break
        if renamingfolder[i] == "/":
            renamingfolder = renamingfolder[:i] + "\\\\" + renamingfolder[i + 1:] 
        i += 1
    
    number = 1
    for image in renamingfiles:
        templen = len(image) - 1
        while True:
            if image[templen] == ".":
                break
            else:
                templen = templen - 1
        extension = image[templen:]
        newfilepath = renamingfolder + "\\\\" + prefix + str(number) + extension
        oldfilepath = renamingfolder + "\\\\" + image
        os.rename(oldfilepath,newfilepath)
        number += 1
    mb.showinfo('confirmation', "Done!")
root = Tk()

Label(root, text="Group File Renamer", font=("Helvetica", 16), fg="blue").grid(row = 5, column = 2)
Button(root, text = "Renaming", command = renaming).grid(row=15, column =2)

root.mainloop()