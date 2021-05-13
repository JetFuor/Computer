from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time, datetime
import pandas as pd


DRIVER_PATH = "C:/Users/Stephen/Downloads/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')