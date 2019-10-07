import requests
from bs4 import BeautifulSoup
import csv

with open('simple.html') as source_file:
    # content = source_file.read()

    soup = BeautifulSoup(source_file, 'lxml')

# print(content)
# print(soup.prettify())

# ttl = soup.title
# print(ttl.text)

# heading = soup.h1
# print(heading.text)

# ar = soup.div.h2.a
# print(ar.text)

# for ar in soup.find_all('div', class_='article'):
#     print(ar.text)


for ar in soup.find_all('div', class_='article'):
    print(ar.p.text)


# a = soup.find(id='site_title')
# print(a.text)




