from requests_html import HTMLSession,HTMLResponse
import urllib.request 
import random
# import selenium
# from selenium import webdriver

# import time

# driver = webdriver.Chrome("C:\\Users\\Hamdan\\Desktop\\scrapng\\selenium\\chromedriver_win32\\chromedriver.exe")
# driver.get("https://librestock.com/")

# SCROLL_PAUSE_TIME = 1

# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height
no = 1
session = HTMLSession()
response = session.get("https://librestock.com/photos/")
# print(response)
source = response.html 
block = source.find("ul.photos", first=True)
image_block = block.find("li a")
for image in image_block:
    sub_response = session.get(image.attrs['href'])
    print(image.attrs['href'])
    print(no ,"    ", sub_response)
    img_source = sub_response.html.find("figure img", first=True).attrs['src']
    print(img_source)
    



