import keyboard
import pyautogui

while True:
    if keyboard.is_pressed("X"):
        on = True
        while on:
            pyautogui.click(button='right')
            if keyboard.is_pressed("Z"):
                on = False
    if keyboard.is_pressed("C"):
        break