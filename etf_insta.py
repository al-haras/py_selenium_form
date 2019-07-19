import os
import info
import xpaths
import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Define Chrome Driver Path
if platform.system()=='Linux':
    driverPath = os.path.join(os.getcwd(), 'chromedriver')
elif platform.system()=='Windows':
    driverPath = os.path.join(os.getcwd(), 'chromedriver74.exe')
elif platform.system()=='Darwin':
    driverPath = os.path.join(os.getcwd(), 'chromedriver_mac')
else:
    print("You do not appear to be running Linux, Windows, or Mac")
    input("Press any key to Exit")

# URL
etfURL = 'https://geekhack.org/index.php?topic=79513.0'

# Define Chrome as the Webdriver for Selenium
driver = webdriver.Chrome(driverPath)

# Direct Driver Nightcaps Thread
driver.get(etfURL)

# Check for element, refresh after 5 seconds if not there
form = None
while not form:
    try:
        form = driver.find_element_by_xpath(xpaths.formLink).click()
    except NoSuchElementException:
        driver.implicitly_wait(5)
        driver.refresh()

# Form Interaction - This can be modified to add whatever information you want.
driver.find_element_by_xpath(xpaths.userPath).send_keys(info.username)
driver.find_element_by_xpath(xpaths.geekhackButton).click()
driver.find_element_by_xpath(xpaths.emailPath).send_keys(info.email)
driver.find_element_by_xpath(xpaths.shippingUS).click()
driver.find_element_by_xpath(xpaths.nextButtonPath).click()
driver.implicitly_wait (50)
driver.find_element_by_xpath(xpaths.capAndBlank).click()
driver.find_element_by_xpath(xpaths.nextButtonPath).click()
driver.find_element_by_xpath(xpaths.yesPath).click()
driver.find_element_by_xpath(xpaths.nextButtonPath).click()
