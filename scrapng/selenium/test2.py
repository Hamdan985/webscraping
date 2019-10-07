from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
  
browser = webdriver.Chrome('chromedriver_win32\\chromedriver.exe')
browser.get("http://www.facebook.com")
  
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
login   = browser.find_element_by_id("u_0_b")
  
username.send_keys("hamdan")
password.send_keys("mypassword")
  

login.click()