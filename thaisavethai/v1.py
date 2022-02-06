from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

with open("password.txt", 'r') as f:
    content = f.read().splitlines()
    email = content[0]
    password = content[1]

def init_driver(url):
    global driver
    driver = webdriver.Firefox(executable_path="E:/Drivers/geckodriver")
    driver.get(url)

def next_form(url):
    driver.get(url)

def english():
    driver.implicitly_wait(5)
    change_english = driver.find_element_by_xpath("//img[contains(@src,'images/en.png')]")
    change_english.click()

def login_page():
    time.sleep(1)
    log_page = driver.find_element_by_xpath("//img[contains(@src,'images/icon_3.png')]")
    log_page.click()

    # Inputting the username into the site
def input_username():
    driver.implicitly_wait(5)
    username_bar = driver.find_element_by_xpath("//input[contains(@id,'C_USERNAME')]")
    username_bar.send_keys(email)

# Inputting the password into the site
def input_password():
    driver.implicitly_wait(5)
    password_bar = driver.find_element_by_xpath("//input[contains(@id,'C_PASSWORD')]")
    password_bar.send_keys(password)

# Clicking the button to enter the details
def login_click():
    driver.implicitly_wait(5)
    login_bar = driver.find_element_by_xpath("//button[contains(@class,'btn btn-lg btn-covid btn-block text-uppercase')]")
    login_bar.click()

def assess_risk():
    driver.implicitly_wait(5)
    assess_page = driver.find_element_by_xpath("//img[contains(@src,'images/01.png')]")
    assess_page.click()
    form_page = driver.find_element_by_xpath("//a[contains(@class,'btn btn-primary btn-sm float-right')]")
    form_page.click()
    q1_answer = driver.find_element_by_xpath("//input[contains(@id,'C_SICK_2')]")
    q1_answer.click()
    q2_answer = driver.find_element_by_xpath("//input[contains(@id,'C_NOT_SMELL_2')]")
    q2_answer.click()
    q3_answer = driver.find_element_by_xpath("//input[contains(@id,'C_NOT_TALK_2')]")
    q3_answer.click()
    q4_answer = driver.find_element_by_xpath("//input[contains(@name,'C_TRAVEL')][contains(@value, '1')]")
    q4_answer.click()
    save_button = driver.find_element_by_xpath("//button[contains(@class,'btn btn-lg btn-covid btn-block text-uppercase')]")
    save_button.click()

def assess_risk_2():
    driver.implicitly_wait(5)
    assess_page = driver.find_element_by_xpath("//img[contains(@src,'images/03.png')]")
    assess_page.click()
    form_page = driver.find_element_by_xpath("//a[contains(@class,'btn btn-primary btn-sm float-right')]")
    form_page.click()
    q1_answer = driver.find_element_by_xpath("//input[contains(@id,'T_TRAVEL_RISK_AREA_3')]")
    q1_answer.click()
    q2_answer = driver.find_element_by_xpath("//input[contains(@id,'T_DISTANCE_ARER_CROWDED_1')]")
    q2_answer.click()
    q3_answer = driver.find_element_by_xpath("//input[contains(@id,'T_TIME_ARER_CROWDED_1')]")
    q3_answer.click()
    q4_answer = driver.find_element_by_xpath("//input[contains(@id,'T_ACTIVITY_ARER_CROWDED_1')]")
    q4_answer.click()
    q5_answer = driver.find_element_by_xpath("//input[contains(@id,'T_TOUCH_PATIENT_1')]")
    q5_answer.click()
    q6_answer = driver.find_element_by_xpath("//input[contains(@id,'T_AREA_MASK_1')]")
    q6_answer.click()
    q7_answer = driver.find_element_by_xpath("//input[contains(@id,'T_RINSE_TOUCH_1')]")
    q7_answer.click()
    save_button = driver.find_element_by_xpath("//button[contains(@class,'btn btn-lg btn-covid btn-block text-uppercase')]")
    save_button.click()

def main():
    init_driver("https://savethai.anamai.moph.go.th/main.php")
    english()
    login_page()
    input_username()
    input_password()
    login_click()
    assess_risk()
    next_form("https://savethai.anamai.moph.go.th/main.php")
    english()
    assess_risk_2()

main()