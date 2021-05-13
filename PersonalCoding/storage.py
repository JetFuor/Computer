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
