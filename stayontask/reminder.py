import time
from tkinter import messagebox as mb
from tkinter import *
import random

encouragement = ["STAY ON TASK!!! Love you :)", "You'll be fine, you can do it!", "Do that work -_-", "Almost there, get it done!"]

#i = 1

while True:
    time.sleep(480)
    root = Tk()
    #if (i % 5) == 0:
    #    mb.showinfo('Reminder', "Switch to next task.")
    #else:
    mb.showinfo('Reminder', encouragement[random.randint(0, 3)])
    root.destroy()
    #i = i + 1