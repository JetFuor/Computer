
# Aight, what do I want in my calcluator
# Start with choosing 2D or 3D, then moving to choose what type of equation want to calculate
# Then input and show the output
# Can choose go back, choose sth else
# Due date: Friday
# Start with home page, go to 2D or 3D
# Go to options screen with multiple calculators
# Then each individual calculator
# IDK finish by friday, might need alot of late nighters

from tkinter import *
import time
from math import *
# Splash screen commands

class Splash(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        # Designing the splash screen
        self.title("Stephen's Sucky Vector Calculator")
        self.geometry("1380x760")
        self.configure(background="black")
        self.overrideredirect(True)
        
        # Text for the splash screen
        spatxt = Label(self, text = "Yules Coding Company") 
        spatxt.config(font =("Courier", 60), bg="black", fg="white", borderwidth="4", relief="groove", padx="20", pady="4")
        spatxt.place(relx="0.5", rely="0.5")

        present = Label(self, text = "Presents:")
        present.config(font=("Times", 40), bg="black", fg="white")

        # Opening the text
        spatxt.pack(pady="200")
        present.pack()
        ## required to make window show before the program gets to the mainloop
        self.update()

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.withdraw()
        splash = Splash(self)

        ## setup stuff goes here
        self.title("Stephen's Sucky Vector Calculator")
        ## simulate a delay while loading
        time.sleep(3)

        ## finished loading so destroy splash
        splash.destroy()

        ## show window again
        self.deiconify()

        start = StartScreen(self)

class StartScreen(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.configure(background="black")
        
        # Adding text and buttons on the screen
        l = Label(self, text = "Vector Calculator") 
        l.config(font =("Courier", 80), bg="#6e2775", fg="white", borderwidth="4", relief="groove", padx="20", pady="4")
        l.pack(pady="80")

        dimension2 = Button(self, text="2D Vector", font=("Times", 20), command=lambda: self.switch_frame(D2Options))
        dimension2.config(height="2",
                            width="14",
                            bg="black",
                            fg="#97e6ca",
                            relief="groove",
                            borderwidth="4",
                            activebackground="#00ff00")
        dimension2.pack(pady="0")

        dimension3 = Button(self, text="3D Vector", font=("Times", 20), command=lambda: self.switch_frame(D3Options))
        dimension3.config(height="2",
                            width="14",
                            bg="black",
                            fg="#97e6ca",
                            relief="groove",
                            borderwidth="4",
                            activebackground="#00ff00")
        dimension3.pack(pady="80")

        Exit = Button(self, text="Exit", font=("Times", 20), command=lambda: [self.destroy()])
        Exit.config(height="2",
                        width="14",
                        bg="black",
                        fg="#97e6ca",
                        relief="groove",
                        borderwidth="4",
                        activebackground="#00ff00")
        Exit.pack(pady="0")

        # Code for fullscreen and exiting
        self.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.bind("<F11>", self.toggleFullScreen)
        self.bind("<Escape>", self.quitFullScreen)

        self.update()

        # Functions for fullscreen
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)

        # How to move from one screen to another
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        self._frame = new_frame
        self._frame.pack()

# Options for 2D vectors
class D2Options(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.configure(background="black")

        # Text and buttons
        l = Label(self, text = "2D Vector Options") 
        l.config(font =("Courier", 80), bg="#212fad", fg="white", borderwidth="4", relief="groove", padx="20", pady="4")
        l.pack(pady="80")

        magnitude = Button(self, text="Magnitude", font=("Times", 20), command=lambda: self.switch_frame(Mag2D))
        magnitude.config(height="2",
                            width="14",
                            bg="black",
                            fg="#97e6ca",
                            relief="groove",
                            borderwidth="4",
                            activebackground="#00ff00")
        magnitude.pack(pady="0")

        linequ = Button(self, text="Equation of Line", font=("Times", 20), command=lambda: self.switch_frame(Line2D))
        linequ.config(height="2",
                            width="14",
                            bg="black",
                            fg="#97e6ca",
                            relief="groove",
                            borderwidth="4",
                            activebackground="#00ff00")
        linequ.pack(pady="80")

        Exit = Button(self, text="Back", font=("Times", 20), command=lambda: [self.destroy()])
        Exit.config(height="2",
                        width="14",
                        bg="black",
                        fg="#97e6ca",
                        relief="groove",
                        borderwidth="4",
                        activebackground="#00ff00")
        Exit.pack(pady="0")

        # Code for fullscreen
        self.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.bind("<F11>", self.toggleFullScreen)
        self.bind("<Escape>", self.quitFullScreen)

        self.update()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)

        # Ability to change frames
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        self._frame = new_frame
        self._frame.pack()

# 3D options of calculators
class D3Options(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.configure(background="black")

        # Text and buttons for the options
        l = Label(self, text = "3D Vector Options") 
        l.config(font =("Courier", 80), bg="#212fad", fg="white", borderwidth="4", relief="groove", padx="20", pady="4")
        l.pack(pady="80")

        magnitude = Button(self, text="Magnitude", font=("Times", 20), command=lambda: self.switch_frame(Mag3D))
        magnitude.config(height="2",
                            width="14",
                            bg="black",
                            fg="#97e6ca",
                            relief="groove",
                            borderwidth="4",
                            activebackground="#00ff00")
        magnitude.pack(pady="0")

        Exit = Button(self, text="Back", font=("Times", 20), command=lambda: [self.destroy()])
        Exit.config(height="2",
                        width="14",
                        bg="black",
                        fg="#97e6ca",
                        relief="groove",
                        borderwidth="4",
                        activebackground="#00ff00")
        Exit.pack(pady="80")

        # Code to make fullsreen
        self.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.bind("<F11>", self.toggleFullScreen)
        self.bind("<Escape>", self.quitFullScreen)

        self.update()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)

    # Code to make fullscreen
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        self._frame = new_frame
        self._frame.pack()

# 2D Magnitude Calculator Page
class Mag2D(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.configure(background="black")

        l = Label(self, text = "Magnitude of 2D") 
        l.config(font =("Courier", 80), bg="#9c1019", fg="white", borderwidth="4", relief="groove", padx="20", pady="4")
        l.pack(pady="70")

        # Sets up the input boxes and entry stuff, white box of stuff
        canvas1 = Canvas(self, width = 400, height = 250, bg="black")
        canvas1.pack(pady="0")

        entry1 = Entry(self)
        entry2 = Entry(self)
        xval = Label(self, text = "X Value")
        xval.config(font =("Courier",14), fg="white", bg="black")
        yval = Label(self, text = "Y Value")
        yval.config(font =("Courier",14), fg="white", bg="black")
        canvas1.create_window(200, 35, window=xval)
        canvas1.create_window(200, 70, window=entry1)
        canvas1.create_window(200, 105, window=yval)
        canvas1.create_window(200, 140, window=entry2)

        answertext = Label(self, text = "Answer")
        answertext.config(font =("Courier",18), fg="white", bg="black")
        canvas1.create_window(200, 200, window=answertext)

        # Calculating the actual magnitude
        Calculate = Button(self, text="Calculate", font=("Times", 15), command=lambda: answertext.config(text = round(sqrt(float(entry1.get())**2 + float(entry2.get())**2), 2)))
        Calculate.config(height="2",
                        width="14",
                        bg="#94b3ae",
                        fg="purple",
                        activebackground="#00ff00")
        Calculate.pack(pady="10")

        Exit = Button(self, text="Back", font=("Times", 15), command=lambda: [self.destroy()])
        Exit.config(height="2",
                        width="14",
                        bg="black",
                        fg="#97e6ca",
                        relief="groove",
                        borderwidth="4",
                        activebackground="#00ff00")
        Exit.pack(pady="0")

        # Code make it fullscreen
        self.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.bind("<F11>", self.toggleFullScreen)
        self.bind("<Escape>", self.quitFullScreen)

        self.update()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)

        # Code to switch frames
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        self._frame = new_frame
        self._frame.pack()

class Line2D(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.configure(background="black")

        l = Label(self, text = "Line Equation 2D") 
        l.config(font =("Courier", 80), bg="#9c1019", fg="white", borderwidth="4", relief="groove", padx="20", pady="4")
        l.pack(pady="70")

        # Sets up the input boxes and entry stuff, white box of stuff
        canvas1 = Canvas(self, width = 400, height = 250, bg="black")
        canvas1.pack(pady="0")

        entry1 = Entry(self)
        entry2 = Entry(self)

        xval = Label(self, text = "X Value")
        xval.config(font =("Courier",14), fg="white", bg="black")
        yval = Label(self, text = "Y Value")
        yval.config(font =("Courier",14), fg="white", bg="black")

        canvas1.create_window(200, 35, window=xval)
        canvas1.create_window(200, 70, window=entry1)
        canvas1.create_window(200, 105, window=yval)
        canvas1.create_window(200, 140, window=entry2)

        answertext = Label(self, text = "Answer")
        answertext.config(font =("Courier",18), fg="white", bg="black")
        canvas1.create_window(200, 200, window=answertext)

        # Calculating the actual magnitude
        Calculate = Button(self, text="Calculate", font=("Times", 15), command=lambda: answertext.config(text = round(sqrt(float(entry1.get())**2 + float(entry2.get())**2), 2)))
        Calculate.config(height="2",
                        width="14",
                        bg="#94b3ae",
                        fg="purple",
                        activebackground="#00ff00")
        Calculate.pack(pady="10")

        Exit = Button(self, text="Back", font=("Times", 15), command=lambda: [self.destroy()])
        Exit.config(height="2",
                        width="14",
                        bg="black",
                        fg="#97e6ca",
                        relief="groove",
                        borderwidth="4",
                        activebackground="#00ff00")
        Exit.pack(pady="0")

        # Code make it fullscreen
        self.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.bind("<F11>", self.toggleFullScreen)
        self.bind("<Escape>", self.quitFullScreen)

        self.update()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)

        # Code to switch frames
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        self._frame = new_frame
        self._frame.pack()

# 3D Magintude Calc
class Mag3D(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.configure(background="black")

        l = Label(self, text = "Magnitude of 3D") 
        l.config(font =("Courier", 80), bg="#9c1019", fg="white", borderwidth="4", relief="groove", padx="20", pady="4")
        l.pack(pady="70")

        # Sets up the input boxes and entry stuff, white box of stuff
        canvas1 = Canvas(self, width = 400, height = 250, bg="black")
        canvas1.pack(pady="0")

        entry1 = Entry(self)
        entry2 = Entry(self)
        entry3 = Entry(self)

        xval = Label(self, text = "X Value")
        xval.config(font =("Courier",14), fg="white", bg="black")
        yval = Label(self, text = "Y Value")
        yval.config(font =("Courier",14), fg="white", bg="black")
        zval = Label(self, text = "Z Value")
        zval.config(font =("Courier",14), fg="white", bg="black")
        
        canvas1.create_window(200, 20, window=xval)
        canvas1.create_window(200, 45, window=entry1)
        canvas1.create_window(200, 70, window=yval)
        canvas1.create_window(200, 95, window=entry2)
        canvas1.create_window(200, 120, window=zval)
        canvas1.create_window(200, 145, window=entry3)

        answertext = Label(self, text = "Answer")
        answertext.config(font =("Courier",18), fg="white", bg="black")
        canvas1.create_window(200, 200, window=answertext)

        # Calculating the actual magnitude
        Calculate = Button(self, text="Calculate", font=("Times", 15), command=lambda: answertext.config(text = round(sqrt(float(entry1.get())**2 + float(entry2.get())**2 + float(entry3.get())**2), 2)))
        Calculate.config(height="2",
                        width="14",
                        bg="#94b3ae",
                        fg="purple",
                        activebackground="#00ff00")
        Calculate.pack(pady="10")

        Exit = Button(self, text="Back", font=("Times", 15), command=lambda: [self.destroy()])
        Exit.config(height="2",
                        width="14",
                        bg="black",
                        fg="#97e6ca",
                        relief="groove",
                        borderwidth="4",
                        activebackground="#00ff00")
        Exit.pack(pady="0")

        # Code make it fullscreen
        self.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.bind("<F11>", self.toggleFullScreen)
        self.bind("<Escape>", self.quitFullScreen)

        self.update()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)

        # Code to switch frames
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    # Setting up the window
    home = App()

    home.mainloop()