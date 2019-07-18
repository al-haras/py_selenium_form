## Form Bot
This is a bot that will click on a link and fill out your specified information.

- Python 3
- Chrome Version 75

### This project is still a work in progress
Everything up to entering your information in the form is working.

#### Things still needed:
- Specific form xpaths needed to finish the full project.
- May remove the chromedriver* from directory to allow people to swap to different versions easily based on what they have, but it would require them to manually update the filename for the Webdriver version.

This specific tool is designed to be used to enter a specific raffle that is only open for two-five minutes randomly.

The format of these specific raffles has sort of changed and trivia is sometimes added and/or the maker has been posting raffles to instagram as of late. I have added both Geekhack and Instagram. What this bot will do is get you to the point where you will need to enter trivia but everything else will be automated.

If you need to edit the form for things such as address besides PayPal, it should be easy to add in info.py and find the xpath to send the text to by modifying the etf_(either).py

You must have Selenium installed before running.
```pip3 install selenium```