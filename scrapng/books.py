import requests_html
from requests_html import HTMLSession,HTML,HTMLResponse
import urllib.request 
import time 


session = HTMLSession()
book_title = []
book_cost = []
image = []

urls = ['http://books.toscrape.com/']

file = open("books.csv", "w")
header = "Book Title, Book Price\n"
file.write(header)

for no in range(1,2):
    urls.append(f'http://books.toscrape.com/catalogue/page-{no}.html')

     
for url in urls:
    time.sleep(5)
    response = session.get(url)
    # print(response)
    content = response.html 
    box = content.find('ol.row', first = True)
    # print(box)

    book_name = box.find('li h3 a')
    book_price = box.find('p.price_color')

    for price in book_price:
        # print(float(price.text[1:]))
        book_cost.append(price.text[1:])

    for name in book_name:
        # print(name.text)
        book_title.append(name.attrs['title'])

    images = content.find('div.image_container img')
    for element in images:
        print("http://books.toscrape.com/"+element.attrs['src'])
        image.append("http://books.toscrape.com/"+element.attrs['src'])

    for i in range(len(book_title)):
        print(i+1 ,"  ", book_title[i])
        print("    ", book_cost[i])
        print(image[i])
        file.write(book_title[i].replace(',', '') + ',' + book_cost[i] + '\n')
        urllib.request.urlretrieve(image[i], book_title[i])
file.close()


# from  bs4 import BeautifulSoup
# import requests_html
# from requests_html import HTMLSession,HTML,HTMLResponse
# urls = ['http://books.toscrape.com/']

# for no in range(1,51):
#     urls.append(f'http://books.toscrape.com/catalogue/page-{no}.html')

# title = []
# cost = []

# for url in urls:
#     session = HTMLSession()
#     source = session.get(url).text 
#     soup = BeautifulSoup(source, 'lxml')

#     block = soup.find('ol', class_='row')

#     book_name = block.find_all('article')
#     for product in book_name:
#         name = product.h3.a.text
#         title.append(name)

#         price = block.find('p', class_='price_color')
#         cost.append(price.text[2:])

#     print(len(book_name)) 

#     for i in range(len(title)):
#         print(i+1 ,"    ", title[i])
#         print("     ", cost[i])