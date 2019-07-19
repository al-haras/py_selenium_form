## ETF Form Bot

This is a bot that will click on a link and fill out your specified information. This will allow you to automate the form up until the point you get to trivia, which will give you more time to look up the trivia.

### Tested Using
- Python 3.7
- Chrome Version 75

## Using the bot

To function properly, this bot requires you to edit the info.py with your correct information. You will need to provide the following:
- Username
- PayPal Email Address
- Address (Not Required) - Only needed if the address you are using is different than the default PayPal address you have. ```\n``` acts as the enter key to create a new line in the address field.

By Default, you can choose which platform you want. Instagram link or Geekhack link. It will refresh the page every 5 seconds looking for the form URL to be posted.

In the ```etf_gh.py``` and/or ```etf_insta.py```, you can specify how the form gets filled out using xpaths. I have set to the most common scenario that I can think of, however any element can be entered.

An example of a scenario where you would want international shipping and specify an address that is not used by PayPal you would do the following:

Remove:
```driver.find_element_by_xpath(xpaths.shippingUS).click()```

Replace with:
```driver.find_element_by_xpath(xpaths.shippingINT).click()```
```driver.find_element_by_xpath(xpaths.shippingInfo).send_keys(info.shippingAddress)```

The same applies for Username Selection. The you can specify using the corresponding button listed in the ```xpaths.py``` file.

### Possible Future Plans:
- May add options to use Chrome or Firefox since I primarily use Firefox. This was built with Chrome as most people seem to use Chrome.
- May add Mac Support as it would be a few more lines of code and another driver in the repo
- Containerization (Docker) of script.
