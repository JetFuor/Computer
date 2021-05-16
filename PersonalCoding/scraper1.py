from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time, datetime
import pandas as pd

browser = webdriver.Chrome(executable_path=r"C:/Users/Stephen/Downloads/chromedriver_win32/chromedriver")
browser.get("https://www.instagram.com/")

with open("password.txt") as file:
    email = file.readline()
    email = email[:len(email)-1]
    password = file.readline()
    password = password[:len(password)-1]

inputemail = browser.find_element_by_xpath("//input[contains(@aria-label,'Phone number, username, or email')]").send_keys(email)
inputpassword = browser.find_element_by_xpath("//input[contains(@aria-label,'Password')]").send_keys(password)
submit = browser.find_element_by_xpath("//button[contains(@class,'sqdOP  L3NKy   y3zKF     ')]").click()