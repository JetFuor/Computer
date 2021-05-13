from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Firefox()

driver.get('https://hoopshype.com/salaries/players/')