from selenium import webdriver
driver = webdriver.Chrome('/Users/hariskhan/Desktop/webselenium/chromedriver')
search_query='War'
driver.get('https://www.youtube.com/results?search_query='+search_query)

