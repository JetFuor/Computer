from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pyautogui
import string

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
        time.sleep(3)

# Looping through each image on the users account
def looping_images():
    driver.implicitly_wait(5)
    image_count = int(driver.find_element_by_xpath("//span[contains(@class,'g47SY ')]").text)
    first_photo = driver.find_element_by_xpath("//div[contains(@class,'v1Nh3 kIKUG  _bz0w')]")
    first_photo.click() # Looping through each image
    time.sleep(3)
    for i in range(image_count):
        too_many_comments()
        obtaining_comments()
        time.sleep(1)
        pyautogui.press('right')
        time.sleep(3)
    pyautogui.click(200, 200)

# Clicking the plus button to show all the comments to be scraped
# Sometimes too many comments and needs to have a button to be pressed
def too_many_comments():
    visible = True
    while visible:
        driver.implicitly_wait(2)
        soup = str(BeautifulSoup(driver.page_source, 'html.parser'))
        if soup.find('dCJp8 afkep') != -1:
            driver.find_element_by_xpath("//button[contains(@class,'dCJp8 afkep')]").click()
            time.sleep(1)
        else:
            visible = False

# Gaining a list of all the comments on a post and counting them
def obtaining_comments():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    stage1_comments = soup.find_all('span', class_='')
    for i in range(len(stage1_comments)):
        stage1_comments[i] = str(stage1_comments[i])

    tagging_people(stage1_comments)

    stage2_comments = []
    for i in range(len(stage1_comments)):
        temp = stage1_comments[i].split(">")
        uncomplete_comment = temp[len(temp)-2]
        complete_comment= uncomplete_comment[:len(uncomplete_comment)-6]
        stage2_comments.append(complete_comment)

    stage3_comments = []
    for i in range(len(stage2_comments)):
        if stage2_comments[i] != "":
            stage3_comments.append(stage2_comments[i])

    stage4_comments = []
    for i in range(len(stage3_comments)-4):
        stage4_comments.append(stage3_comments[i+4])

    if len(stage4_comments) < 10:
        pass
    else:
        storing_comments(stage4_comments)

# Fixing the issue of text before tags being deleted and no longer applicable
def tagging_people(comments):
    for i in range(len(comments)):
        tempstring = comments[i]
        start_position = tempstring.find('<a') # First character position
        if start_position != -1:
            end_position = tempstring.find('</a>')
            comments[i] = tempstring[:start_position] + tempstring[end_position+5:]

# ISSUES EMOJIS CAN'T BE STORED
# Seperating the comments and counting specific words
def storing_comments(comments):
    emojis = []
    punc = string.punctuation
    with open("a_comments.txt","a") as f:
        for i in range(len(comments)):
            word = comments[i]
            deleted = 0
            for n in range(len(word)):
                letter = word[n-deleted]
                if letter.isalnum() or letter.isspace():
                    pass
                else:
                    word = word[:n-deleted] + word[n+1-deleted:]
                    deleted += 1
                    if punc.find(letter) == -1:
                       emojis.append(letter)
            f.write(word)
    print(emojis)
           
            

# STUPID BS WAY IDEA
# GO THROUGH THING
# TAKE EMOJIS OUT
# STORE INTO ANOTHER LIST

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