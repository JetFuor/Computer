import keyboard
import pyautogui

# 'x' to right spam
# 'c' to left spam
# 'v' to left hold
# 'k' to right hold
# 'z' to turn off
# 'm' to turn close the program

def spam(mouse):
    on = True
    while on:
        pyautogui.click(button = mouse)
        if keyboard.is_pressed("Z"):
            on = False

def hold(mouse):
    on = True
    while on:
        pyautogui.mouseDown(button = mouse)
        if keyboard.is_pressed("Z"):
            on = False

while True:
    if keyboard.is_pressed("X"):
        spam("right")
    if keyboard.is_pressed("C"):
        spam("left")
    if keyboard.is_pressed("V"):
        hold("left")
    if keyboard.is_pressed("K"):
        hold("right")
    if keyboard.is_pressed("M"):
        break