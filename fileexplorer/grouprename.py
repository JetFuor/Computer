
from tkinter import *     
import os
from tkinter import filedialog
from tkinter import messagebox as mb

def renaming():
    # Obtaining the file names
    folderlocation = filedialog.askdirectory()
    renamingfiles=sorted(os.listdir(folderlocation))

    # Obtaining the prefix
    prefix = entrybox.get()

    # Changing the path to viable format, see images for reference, we want zrename
    renamingfolder = folderlocation
    i = 0
    while True:
        if i == len(renamingfolder):
            break
        if renamingfolder[i] == "/":
            renamingfolder = renamingfolder[:i] + "\\\\" + renamingfolder[i + 1:] 
        i += 1
    
    # Giving each file proper name and renaming it
    number = 1
    for image in renamingfiles:
        templen = len(image) - 1
        while True:
            if image[templen] == ".":
                break
            else:
                templen = templen - 1
        # .jpg, .png etc
        extension = image[templen:]
        newfilepath = renamingfolder + "\\\\" + prefix + str(number) + extension
        oldfilepath = renamingfolder + "\\\\" + image
        os.rename(oldfilepath,newfilepath)
        number += 1
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