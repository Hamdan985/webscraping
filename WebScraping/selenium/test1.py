

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('/Users/hariskhan/Desktop/webselenium/chromedriver')
browser.get("http://www.google.com")
try:
    assert "Google" in browser.title
    print('assert success')

except Exception as e:
    print('assertion failed')
browser.close()

