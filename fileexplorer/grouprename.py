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

def open_window():
    read=easygui.fileopenbox()
    return read

# rename file function
def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension=os.path.splitext(chosenFile)[1]
    print("Enter new name for the chosen file")
    newName=input()
    path = os.path.join(path1, newName+extension)
    print(path)
    os.rename(chosenFile,path) 
    mb.showinfo('confirmation', "File Renamed !")

# MY VERSION
def renaming():
    # OBTAINING FILE NAMES
    folderList = filedialog.askdirectory()
    sortlist=sorted(os.listdir(folderList))

    # ASKING FOR WHAT TO RENAME IT TO
    prefix = input("Enter starting prefix for all images: ")

    # CHANGING THE PATHING AND RENAMING EACH FILE
    while True:
        i = 0
        if folderList[i] == "/":
            folderList = folderList[:i] + "\\" + folderList[i + 1:]
                



    

root = Tk()

Label(root, text="Group File Renamer", font=("Helvetica", 16), fg="blue").grid(row = 5, column = 2)
Button(root, text = "Renaming", command = renaming).grid(row=15, column =2)

root.mainloop()