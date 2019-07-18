import os
import info
import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Variables for Form pulled from info.py
username = info.username
email = info.email

# Define Chrome Driver Path
if platform.system()=='Linux':
    driverPath = os.path.join(os.getcwd(), 'chromedriver')
elif platform.system()=='Windows':
    driverPath = os.path.join(os.getcwd(), 'chromedriver74.exe')

# URLs and xpath
etfURL = 'https://geekhack.org/index.php?topic=79513.0'
formLink = "//*[contains(@class,'bbc_link')][contains(text(),'FORM')]"

# Define Chrome as the Webdriver for Selenium
driver = webdriver.Chrome(driverPath)

# Direct Driver Nightcaps Thread
driver.get(etfURL)

# Check for element, refresh after 5 seconds if not there
form = None
while not form:
    try:
        form = driver.find_element_by_xpath(formLink).click()
    except NoSuchElementException:
        driver.implicitly_wait(5)
        driver.refresh()

# Form Interaction
#driver.find_element_by_name('checkout[email]').send_keys(email)
#driver.find_element_by_name('checkout[username]').send_keys(username)