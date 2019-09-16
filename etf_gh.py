import os
import config
import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# Determine which version of Chromedriver to use based on OS
def determine_os():
    if platform.system() == 'Linux':
        return os.path.join(os.getcwd(), 'chromedriver')
    elif platform.system() == 'Windows':
        return os.path.join(os.getcwd(), 'chromedriver76.exe')
    elif platform.system() == 'Darwin':
        return os.path.join(os.getcwd(), 'chromedriver_mac')
    else:
        print("You do not appear to be running Linux, Windows, or Mac")
        input("Press any key to Exit")
        exit()


# Check link for corresponding URL to see if element exists
def check_link(path, url):
    driver.get(url)
    form = None
    while not form:
        try:
            form = driver.find_element_by_xpath(path).click()
            break
        except NoSuchElementException:
            driver.implicitly_wait(5)
            driver.refresh()


def test_entry():
    try:
        driver.find_element_by_xpath(config.user_path).send_keys(config.username)
    except NoSuchElementException:
        print('The Form Link is valid, but the raffle is closed.')
        input('Press any key to Exit')
        driver.quit()
        exit()


# User manually decides which platform they want to search on.
def user_choice():
    user_input = input('Which ETF URL do you want to Monitor? (Geekhack, or Instagram)\n').lower()
    if user_input == 'geekhack':
        return config.geekhack_url
    elif user_input == 'instagram':
        return config.insta_url
    else:
        print('That is not a valid option.')
        return user_choice()


def x_path(selected):
    if selected == config.geekhack_url:
        return config.gh_form_link
    elif selected == config.insta_url:
        return config.insta_form_link


# Set variables based on user input and functions
user_option = user_choice()
correct_path = x_path(user_option)
driver = webdriver.Chrome(determine_os())

# Call function check_link to check for the xpath element
check_link(correct_path, user_option)

# Test text entry when element is found
test_entry()

# Finish sending the rest of the information
driver.find_element_by_xpath(config.user_path).send_keys(config.username)
driver.find_element_by_xpath(config.geekhack_button).click()
driver.find_element_by_xpath(config.email_path).send_keys(config.email)
driver.find_element_by_xpath(config.shipping_us).click()
driver.find_element_by_xpath(config.next_button).click()
driver.implicitly_wait(50)
driver.find_element_by_xpath(config.cap_and_blank).click()
driver.find_element_by_xpath(config.next_button).click()
driver.find_element_by_xpath(config.yes_path).click()
driver.find_element_by_xpath(config.next_button).click()
