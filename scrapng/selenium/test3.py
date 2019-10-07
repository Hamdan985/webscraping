from selenium import webdriver
driver = webdriver.Chrome('chromedriver_win32\\chromedriver.exe')
search_query='War'
driver.get('https://www.youtube.com/results?search_query='+search_query)

