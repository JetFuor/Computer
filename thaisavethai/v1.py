from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pyautogui
import string

with open("password.txt", 'r') as f:
    content = f.read().splitlines()
    email = content[0]
    password = content[1]

def init_driver(url):
    global driver
    driver = webdriver.Firefox(executable_path="E:/Drivers/geckodriver")
    driver.get(url)

def english():
    driver.implicitly_wait(5)
    change_english = driver.find_element_by_xpath("//img[contains(@src,'images/en.png')]")
    change_english.click()

def main():
    init_driver("https://savethai.anamai.moph.go.th/main.php")
    english()