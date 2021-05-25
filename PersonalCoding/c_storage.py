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





from urllib.request import urlopen

url = "https://overwatchleague.com/en-us/schedule?stage=regular_season&week=1"

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)









from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time, datetime
import pandas as pd

browser = webdriver.Chrome(executable_path=r"C:/Users/Stephen/Downloads/chromedriver_win32/chromedriver")
browser.get("https://www.instagram.com/")
'''
with open("password.txt") as file:
    email = file.readline()
    email = email[:len(email)-1]
    password = file.readline()
    password = password[:len(password)-1]
'''
browser.find_element_by_class_name('_2hvTZ pexuQ zyHYP').send_keys('nutwillinfernape@gmail.com')
browser.find_element_by_name("password").send_keys('infernape123')
browser.find_element_by_xpath("//button[contains(@class,'sqdOP  L3NKy   y3zKF     ')]").click()






# WORD STUFF

import pandas as pd
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt
stopwords = set(STOPWORDS)
n = 5  # n in head(n) determine the numbers of rows to read

with open("lizziecomment.txt", "r") as file:
    df = file.read()
print(df)

positive_wordcloud = WordCloud(width = 1600, height = 1600, background_color ='white', stopwords = stopwords, min_font_size = 10).generate(df) 
plt.figure(figsize = (9, 9), facecolor = None) 
plt.imshow(positive_wordcloud)
plt.axis("off") # off the pixel axis
plt.show()