
# %%
from clearterminal import *
from selenium import webdriver
import time
import pytz
import datetime
import re
from os import path
from csv import writer

clear()
attempt = 1
browser  = webdriver.Firefox() # this open a browser

class ClassRoom:
    def __init__(self, SimpleClassName, SimpleTeacherName, GCClass, Link):
        self.SimpleClassName = SimpleClassName
        self.SimpleTeacherName = SimpleTeacherName
        self.GCClass = GCClass
        self.Link = Link

list_of_classroom = []

Computer_Science = ClassRoom("Computer Science", "Mr.Kieran", "(Y13) CS", "https://classroom.google.com/u/0/c/NDEwNjM3NjM5NTha")
HomeRoom = ClassRoom("Homeroom", "Mr.Ash", "Year 13 Homeroom", "https://classroom.google.com/u/0/c/OTc5NDkyNzg3ODha")

list_of_classroom.append(Computer_Science)
list_of_classroom.append(HomeRoom)




# %%
##############################
##############################
# HARD CODE SETTING

# Which time zone you are in, search up "time zone pytz {your time zone name}"
TIMEZONE = 'Asia/Bangkok'


# Mode for getting the email and password to fill into google login page
mode_list = ["hard_code", "file_based"]
MODE = mode_list[1] # 0 for hard_code, 1 for file_based account(email & password)


# Test Mode Yes or No?
TEST_MODE = True # Test will run the code but not PRESS REPLY


# Time unitll the website refreshes to 
WAIT_TIME_FOR_NO_MATCH = 120 # Seconds


# Valid time for the post
time_list = ["08:", "07:", "7 May"]  ###  CHANGE VARIABLE HERE  ###
OPERATOR = "x*" # x* search for any place that contains each string # CASE-SENSITIVE



# 0 is Computer Science
# 1 is Homeroom
CURRENT_CLASSROOM = list_of_classroom[1] # CHANGE #



FILL_LIST = ["Good Morning! Game here", "Present", "First test run with checking the time Afternoon (BOT)", "Second run reply with validation that the post is up to date. [Criteria posted at 17:xx time]"]
REPLY_COMMENT = FILL_LIST[1]

print("The bot is going to type [{0}] into the classroom [{1}]. {2}'s classroom".format(REPLY_COMMENT, CURRENT_CLASSROOM.SimpleClassName, CURRENT_CLASSROOM.SimpleTeacherName))
print("Attempt #{0}".format(attempt))

##############################
##############################





# %%
def __init_account_from_file():
    global EMAIL, PASSWORD
    MODE = 'file_based'
    if MODE == "hard_code":
        EMAIL = "" ### ENTER USERNAME ###
        PASSWORD = "" ### ENTER PASSWORD ###
    elif MODE == "file_based":
        # Go to README.txt for how enter Absolute Path
        with open('C:\\Users\\Game\\Documents\\GitHub\\password for google classroom bot.txt', "r") as account_file:
            CONTENT = account_file.read().splitlines() # .splitlines() for deleting the /n
            EMAIL = CONTENT[0]
            PASSWORD = CONTENT[1]
__init_account_from_file()





# %%
# The goal is to reach the homepage of the Homeroom
def sign_in_function():
    global browser
    browser.get("""https://accounts.google.com/signin/v2/identifier
    ?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=
    GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin""") # Google Sign In Page
    browser.implicitly_wait(2)
    email_fill = browser.find_element_by_xpath("//input[contains(@type,'email')]").send_keys(EMAIL)
    email_click_next = browser.find_element_by_xpath("//div[contains(@class,'VfPpkd-RLmnJb')]").click()
    time.sleep(2.2)
    password_fill = browser.find_element_by_xpath("//input[contains(@class,'whsOnd zHQkBf')]").send_keys(PASSWORD)
    password_click_next = browser.find_element_by_xpath("//div[contains(@class,'VfPpkd-RLmnJb')]").click()
    browser.get(CURRENT_CLASSROOM.Link) ###  CHANGE VARIABLE HERE  ###

sign_in_function()






# %%
def check_for_valid_post_time():
    global post_valid_time, attempt
    post_valid_time = False
    time.sleep(4)
    whole_page = browser.page_source
    
    class_header_post = browser.find_element_by_xpath("""//h1[contains(@class,'tNGpbb uTUgB YVvGBb')]""").text
    if class_header_post == CURRENT_CLASSROOM.GCClass:
        valid_class = True
        print("""
CLASS matched
Class: {0}""".format(CURRENT_CLASSROOM.GCClass))
    else:
        valid_class = False
        print("""
CLASS NOT matched
Doesn't match {}
WRONG CLASS PAGE""".format(CURRENT_CLASSROOM.GCClass))
    
    top_most_recent_post = browser.find_element_by_xpath("""//div[contains(@class,'qhnNic LBlAUc Aopndd TIunU')]""").text
    for time_string in time_list:
        re_string = time_string + OPERATOR # joining the search string with the operator
        valid_time = re.findall(re_string, top_most_recent_post)
        print(valid_time)
        if valid_time:
            print("""
TIME matched
They are {0}
""".format(valid_time))

            post_valid_time = True
            break
        else:
            print("""
TIME NOT matched
Doesn't match {0}""".format(time_list))
            
    if not(valid_time and valid_class):
        print("Trying again in {} seconds".format(WAIT_TIME_FOR_NO_MATCH))
        attempt += 1
        time.sleep(WAIT_TIME_FOR_NO_MATCH)
        browser.get(CURRENT_CLASSROOM.Link) # refresh
        time.sleep(2)
        clear()
        print("The bot is going to type [{0}] into the classroom [{1}]. {2}'s classroom".format(REPLY_COMMENT, CURRENT_CLASSROOM.SimpleClassName, CURRENT_CLASSROOM.SimpleTeacherName))
        print("Attempt #{0}".format(attempt))
        check_for_valid_post_time()
        # PANIC!

check_for_valid_post_time()





# %%
def fill_comment():
    if post_valid_time:
        time.sleep(3)
        comment_fill = browser.find_element_by_xpath("//div[contains(@class,'LsqTRb Lzdwhd-AyKMt tgNIJf-Wvd9Cc Yiql6e iTy5c editable')]").send_keys(REPLY_COMMENT)
        time.sleep(2)
        if not(TEST_MODE):
            click_reply_button = browser.find_element_by_xpath("//*[name()='path' and @d='M2 3v18l20-9L2 3zm2 11l9-2-9-2V6.09L17.13 12 4 17.91V14z']").click()
            # for xpath for svg format is different for somereason

fill_comment()





#%% 
# Logging function
def log_to_csv():
    if path.exists('main_log.csv'):
        with open("main_log.csv", "a") as Log_File:
            Log_File_writer = writer(Log_File)
            if TEST_MODE:
                string_list = [CURRENT_CLASSROOM.SimpleClassName, REPLY_COMMENT, str(datetime.datetime.now(pytz.timezone(TIMEZONE))), "{0} attempt".format(attempt), "TESTMODE"]
            else:
                string_list = [CURRENT_CLASSROOM.SimpleClassName, REPLY_COMMENT, str(datetime.datetime.now(pytz.timezone(TIMEZONE))), "{0} attempt".format(attempt)]
            Log_File_writer.writerow(string_list)
            print('Log successful')
            print(string_list)
    else:
        with open("main_log.csv", "w") as Log_File:
            Log_File_writer = writer(Log_File)
            Log_File_writer.writerow(["Class", "String Replied", "Date&Time", "MODE"])
            print('A new CSV is made')
        log_to_csv()

# (datetime.datetime.now(tz)).strftime("%a %d % b %Y %H:%M:%S") 




# %% Quit 
log_to_csv()
time.sleep(2)
browser.quit()