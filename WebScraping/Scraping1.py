from  bs4 import BeautifulSoup
import requests_html
from requests_html import HTMLSession,HTML,HTMLResponse
urls = ['http://books.toscrape.com/']

for no in range(1,51):
    urls.append(f'http://books.toscrape.com/catalogue/page-{no}.html')

     
for url in urls:
    session = HTMLSession()
    source = session.get(url).text 
    soup = BeautifulSoup(source, 'lxml')

    block = source.find('ol')
    products = block.find_all('article')
    for product in products:
        name = product.h3.a.text
        print(name)
    print(len(products)) 

# image = []

# session = HTMLSession()
# response = session.get('http://books.toscrape.com/catalogue/category/books_1/index.html')
# source = response.html
# print(source)


# images = source.find('div.image_container img')

# for i in images:
#     print(i.attrs['src'])

# for image in images:
#     print("books.toscrape.com/"+image.attrs['src'])
#     image.append("books.toscrape.com/"+image.attrs['src'])

# for image in images:
#     print(image)

