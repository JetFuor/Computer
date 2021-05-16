import requests
page = requests.get("Website")
page
page.status_code
# Repsonse of 200 should be good


# Parsing the page using Beautiful Soup
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'Website')
print(soup.prettify()) # Makes it print out nicely
list(soup.children) # List all the tags
# Can repeatedly select stuff to bare it down to the bone
soup.find_all('p') # Finds all p
soup.find_all('p')[0].get_text() # Takes the text out of it
soup.find_all('p', class_='outer-text') # Get classes and IDs using this method

# PANDAS used to make the data look nice

# REQUESTS just gets it all
# BEAUTIFULSOUP gets the information and presents nicely
# SELENIUM takes specific bits and stores them

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time, datetime
import pandas as pd

driver = webdriver.Chrome(executable_path=r"C:/Users/Stephen/Downloads/chromedriver_win32/chromedriver")
driver.get("https://overwatchleague.com/en-us/schedule?stage=regular_season&week=1")
chengduscore = driver.find_element_by_xpath("//h2[contains(@class,'section-titlestyles__Title-sc-1wlp19u-3 juLYcv')]").text
driver.quit
print(chengduscore)





from urllib.request import urlopen

url = "https://overwatchleague.com/en-us/schedule?stage=regular_season&week=1"

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)