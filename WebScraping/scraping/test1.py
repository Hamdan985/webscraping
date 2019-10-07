import requests_html
from requests_html import HTML, HTMLSession

session = HTMLSession()

response = session.get("http://books.toscrape.com/")
source = response.html

# print(response)
# print(type(source))
# print(source)

content = source.find('ol')[0]

# print(type(content))
# print(content)

# name = content.find('h3')

# print(type(name))
# print(name[0].text)

name = content.find('a')[0].attrs['href']

print(type(name))
print(name)