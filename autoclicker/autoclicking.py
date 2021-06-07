import keyboard
import pyautogui

# 'x' to right spam
# 'c' to left spam
# 'v' to left hold
# 'z' to turn off
# 'm' to turn close the program

def spam(mouse):
    on = True
    while on:
        pyautogui.click(button = mouse)
        if keyboard.is_pressed("Z"):
            on = False

def lefthold():
    on = True
    while on:
        pyautogui.mouseDown(button='left')
        if keyboard.is_pressed("Z"):
            on = False

while True:
    if keyboard.is_pressed("X"):
        spam("right")
    if keyboard.is_pressed("C"):
        spam("left")
    if keyboard.is_pressed("V"):
        lefthold()
    if keyboard.is_pressed("M"):
        break