import requests_html
from requests_html import HTML, HTMLSession
import shutil

with open('simple.html') as source_file:
    file_content = source_file.read()
    source = HTML(html= file_content)
# print(source.full_text)
title = source.find('title')
print(type(title))
print(title[0].text)

headings = source.find('h2')
# print(type(heading))
for heading in headings:
    print(heading.text)

links = source.find('a', first=True).attrs['href']
print(links)

para= source.find('div.article p', first=True).text
print(para)

# print(heading[0].text)
# session = HTMLSession()
# response = session.get('http://books.toscrape.com//')

# source = response.html
# # title = source.find('title', first=True).text
# # print(title)
# # div = source.find('div')

# # for element in div:
# #     print(element.text)

# titles = source.find('h3 a')
# prices = source.find('div.product_price p.price_color')

# book_title = []
# book_price = []
image = []
# for title in titles:    
#     book_title.append(title.text)

# for price in prices:
#     book_price.append(price.text)


# # for i in range(len(book_title)):
# #     print(book_title[i])
# #     print(book_price[i])

images = source.find('div.image_container img')
for image in images:
    print("books.toscrape.com/"+image.attrs['src'])
    image.append("books.toscrape.com/"+image.attrs['src'])

for image in images:
    print(image)

# # This is the image url.
# image_url = "http://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"
# # Open the url image, set stream to True, this will return the stream content.
# resp = session.get(image_url, stream=True)
# # Open a local file with wb ( write binary ) permission.
# local_file = open('local_image.jpg', 'wb')
# # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
# resp.raw.decode_content = True
# # Copy the response stream raw data to local image file.
# shutil.copyfileobj(resp.raw, local_file)
# # Remove the


