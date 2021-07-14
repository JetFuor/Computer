# -*- coding: utf-8 -*-

from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# Regular expressions re

def init_driver(url):
    global driver
    driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver")
    driver.get(url)

def login_screen():
    driver.implicitly_wait(5)
    login_button = driver.find_element_by_xpath("//a[contains(@class,'global_action_link')]")
    login_button.click()

def main():
    init_driver("https://store.steampowered.com/")
    login_screen()

main()



"""Alright lets think abt this in steps.
1. Open up steam
2. Login
3. Give time to do the authentification
4. Input to continue the program
5. Go to the market
6. Say what type of stuff you want to sell
7. Sell each item individually"""