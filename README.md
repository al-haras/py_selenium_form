## ETF Form Bot

This is a bot that will click on a link and fill out your specified information. This will allow you to automate the form up until the point you get to trivia, which will give you more time to look up your answer.

#### Tested Using
- Python 3.7
- Chrome Version 76, 77 (Both Linux (Arch btw), and Windows 10)

## Using the bot

Selenium must first be installed via Python before running these scripts.

To function properly, this bot requires you to edit the configuration file `config.py` with your correct information. You will need to provide things such as shipping information, email address, and username on the platform of your choice.

By Default, you can choose which platform you want (Instagram or Geekhack). It will refresh the page every 5 seconds looking for the form URL to be posted.

An example of a scenario where you would want international shipping and specify an address that is not used by PayPal you would do the following:

##### Remove:

`driver.find_element_by_xpath(config.shipping_us).click()`

##### Replace with:

`driver.find_element_by_xpath(config.shipping_int).click()`
`driver.find_element_by_xpath(config.shipping_info).send_keys(config.shipping_address)`

The same applies for Username Selection. The you can specify using the corresponding button listed in the `config.py` file.

## Other Versions of Chrome

If you are running a different version of Chrome, you should be able to easily swap the driver for the version you need. You can get the version needed from: https://sites.google.com/a/chromium.org/chromedriver/downloads. Download the webdriver you need to the working directory. You may or may not need to update the name of the new driver depending on which version you get. If it is not the same name as listed in the script, you will change it here:

`os.path.join(os.getcwd(), 'new_driver_you_downloaded')`