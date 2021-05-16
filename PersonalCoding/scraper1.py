from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pdb
import time, datetime


email = "nutwillinfernape@gmail.com"
password = "infernape123"

browser = webdriver.Chrome("C:/Users/Stephen/Downloads/chromedriver_win32/chromedriver")
dom = browser.find_element_by_xpath('//*')
browser.get("https://www.instagram.com")


pdb.set_trace()
username = dom.find_element_by_name("username")
passwordinput = dom.find_element_by_name("password")
login_button = dom.find_element_by_xpath("//*[contains(@class,'sqdOP  L3NKy   y3zKF     ')]")
username.clear()
passwordinput.clear()
username.send_keys(email)
passwordinput.send_keys(password)
login_button.click()


