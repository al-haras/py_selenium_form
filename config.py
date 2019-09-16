# URL paths
geekhack_url = 'https://geekhack.org/index.php?topic=79513.0'
insta_url = 'https://www.instagram.com/nightcaps.keycaps/'

# Shipping Information
email = 'your@emailaddress.com'
username = 'Username'
shipping_address = 'My Name\n123 Fake Street\nAnytown, USA 12345'

# XPaths (Shouldn't need to modify)
gh_form_link = '//*[contains(text(),"forms.gle")]'
insta_form_link = '//*[contains(@class,"yLUwa")][contains(text(),"forms.gle")]'
user_path = '//*[contains(@aria-label,"Username:")]'
email_path = '//*[contains(@aria-label,"PayPal email")]'
instagram_button = '//*[contains(@aria-label,"Instagram")]'
geekhack_button = '//*[contains(@aria-label,"GH")]'
reddit_button = '//*[contains(@aria-label,"Reddit")]'
slack_button = '//*[contains(@aria-label,"Slack")]'
discord_button = '//*[contains(@aria-label,"Discord")]'
shipping_us = '//*[contains(@aria-label,"US Domestic $8")]'
shipping_ca = '//*[contains(@aria-label,"Canada $11")]'
shipping_int = '//*[contains(@aria-label,"International $15")]'
shipping_info = '//*[contains(@aria-label,"Shipping address")]'
next_button = '//span[contains(text(),"Next")]'
yes_path = '//*[contains(@aria-label,"Yes")]'
cap_only = '//*[contains(@aria-posinset,"1")]'
cap_and_blank = '//*[contains(@aria-posinset,"2")]'
