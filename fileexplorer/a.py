
from tkinter import *      
import os
from tkinter import filedialog
from tkinter import messagebox as mb

def renaming():
    print(float(entry1.get())*3)

root = Tk()
root.geometry("300x150")

entry1 = Entry(root).pack()
Button(root, text = "Choose folder", command = renaming).pack(pady="10")

root.mainloop()