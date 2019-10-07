from selenium import webdriver

driver = webdriver.Chrome("chromedriver_win32\\chromedriver.exe")
query = "python.org"
driver.get('https://www.google.com/search?q=' + query)

