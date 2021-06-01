# -*- coding: utf-8 -*-

from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pyautogui
import imageio
# Regular expressions re

# Obtaining the login from the text file
with open("PersonalCoding/password.txt", 'r') as f:
    content = f.read().splitlines()
    email = content[0]
    password = content[1]

# Opening the driver and going to first website
def init_driver(url):
    global driver
    driver = webdriver.Firefox(executable_path="E:/Drivers/geckodriver")
    driver.get(url)

# Asking the user what accounts they want to scrape through
def accounts():
    global users
    users = []
    while True:
        users.append(input("Input the Instagram account you want to use: "))
        if input("Would you like to input another user? Y/N: ") != "Y":
            break

# Inputting the username into the site
def input_username():
    driver.implicitly_wait(5)
    username_bar = driver.find_element_by_xpath("//input[contains(@name,'username')]")
    username_bar.send_keys(email)

# Inputting the password into the site
def input_password():
    driver.implicitly_wait(5)
    password_bar = driver.find_element_by_xpath("//input[contains(@name,'password')]")
    password_bar.send_keys(password)

# Clicking the button to enter the details
def login_click():
    driver.implicitly_wait(5)
    login_bar = driver.find_element_by_xpath("//button[contains(@class,'sqdOP  L3NKy   y3zKF     ')]")
    login_bar.click()

# Going to the home page
def home_page():
    driver.implicitly_wait(5)
    home_button = driver.find_element_by_xpath("//img[contains(@class,'s4Iyt')]")
    home_button.click()

# Turning off notifications
def notification_off():
    driver.implicitly_wait(5)
    off_noti_button = driver.find_element_by_xpath("//button[contains(@class,'aOOlW   HoLwm ')]")
    off_noti_button.click()

# Looping through the users and searching for them
def search_people():
    driver.implicitly_wait(5)
    for i in range(len(users)):
        search_bar = driver.find_element_by_xpath("//input[contains(@placeholder,'Search')]")
        search_bar.send_keys(users[i])
        time.sleep(2)
        search_bar.send_keys("\n")
        search_bar.send_keys("\n")
        time.sleep(3)
        looping_images()
        time.sleep(2)

# Looping through each image on the users account
def looping_images():
    driver.implicitly_wait(5)
    image_count = int(driver.find_element_by_xpath("//span[contains(@class,'g47SY ')]").text)
    first_photo = driver.find_element_by_xpath("//div[contains(@class,'v1Nh3 kIKUG  _bz0w')]")
    first_photo.click() # Looping through each image
    time.sleep(2)
    obtaining_images()
    """ for i in range(image_count):
        obtaining_images()
        time.sleep(1)
        pyautogui.press('right')
        time.sleep(3) """
    pyautogui.click(200, 200)

def obtaining_images():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    images_src = soup.find_all('img', class_='FFVAD')
    single_image = str(images_src[1])
    """ start_position = single_image.find("src=") + 4
    end_position = single_image.find("srcset=") - 1
    image_url = single_image[start_position:end_position] """

    print(single_image)

def main():
    accounts()
    init_driver("https://www.instagram.com/accounts/login/")
    input_username()
    input_password()
    login_click()
    home_page()
    notification_off()
    search_people()
    
main()