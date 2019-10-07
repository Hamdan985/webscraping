from requests_html import HTML, HTMLSession,HTMLResponse
import requests_html
import csv
# with open('simple.html') as source_file:
#     file_content = source_file.read()
#     source = HTML(html=file_content)    

# print(type(source))

csv_file = open('flipkartScraped.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['BOOK TITLE', 'PRICE'])
session = HTMLSession()
response = session.get("http://books.toscrape.com")
source = response.html

book_title = []
book_price = []
content = source.find('.row')[2]

name = content.find('h3')
for elements in name:
    book_title.append(elements.text)


price = content.find('.price_color')
print(type(price))

for elements in price:
    price.append(elements.text)


for i in range


# for book in book_title:
#     print(book)

# print(type(content))
# print(content.html)


# print(type(response))
# print(type(source))


