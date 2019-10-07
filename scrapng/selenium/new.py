from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver_win32\\chromedriver.exe')

browser = driver.get('https://twitter.com/login')
#react-root > div > div > div.css-1dbjc4n.r-1pi2tsx.r-13qz1uu.r-417010 > main > div > div > form > div > div:nth-child(6) > label > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input
username = browser.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-1pi2tsx.r-13qz1uu.r-417010 > main > div > div > form > div > div:nth-child(6) > label > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input")
# username = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
# password = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
password = browser.find_element_by_css_selector("#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input")
# login = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
login = browser.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input')

username.send_keys("hamdan")
password.send_keys("hamdan")
login.click()


