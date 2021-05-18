from collections import UserString
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

with open("PersonalCoding/password.txt", 'r') as f:
    content = f.read().splitlines()
    email = content[0]
    password = content[1]

def __init__driver():
    global driver
    driver = webdriver.Firefox(executable_path="E:/Drivers/geckodriver")
    driver.get("https://www.instagram.com/accounts/login/")

def accounts():
    global users
    users = []
    while True:
        users.append(input("Input the Instagram account you want to use: "))
        if input("Would you like to input another user? Y/N: ") != "Y":
            break

def input_username():
    driver.implicitly_wait(2)
    username_bar = driver.find_element_by_xpath("//input[contains(@name,'username')]")
    username_bar.send_keys(email)

def input_password():
    driver.implicitly_wait(2)
    password_bar = driver.find_element_by_xpath("//input[contains(@name,'password')]")
    password_bar.send_keys(password)

def login_click():
    driver.implicitly_wait(2)
    login_bar = driver.find_element_by_xpath("//button[contains(@class,'sqdOP  L3NKy   y3zKF     ')]")
    login_bar.click()

def home_page():
    time.sleep(5)
    home_button = driver.find_element_by_xpath("//img[contains(@class,'s4Iyt')]")
    home_button.click()

def notification_off():
    time.sleep(3)
    home_button = driver.find_element_by_xpath("//button[contains(@class,'aOOlW   HoLwm ')]")
    home_button.click()

def search_people():
    time.sleep(2)
    for i in range(len(users)):
        search_bar = driver.find_element_by_xpath("//input[contains(@placeholder,'Search')]")
        search_bar.send_keys(users[i])
        time.sleep(1)
        search_bar.send_keys("\n")
        search_bar.send_keys("\n")
        time.sleep(10)
        obtain_comments()
        time.sleep(2)

def obtain_comments():
    first_photo = driver.find_element_by_xpath("//div[contains(@class,'v1Nh3 kIKUG  _bz0w')]")
    first_photo.click()
    time.sleep(2)
    exit_button = driver.find_element_by_xpath("//button[contains(@class,'wpO6b  ')]")
    exit_button.click()
    # Comments are span with class ""
    # Figure out:
    # Go though entire page code
    # Check if more than 10 comments
    # If so, 

def main():
    accounts()
    __init__driver()
    input_username()
    input_password()
    login_click()
    home_page()
    notification_off()
    search_people()
    
main()