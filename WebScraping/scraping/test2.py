from bs4 import BeautifulSoup
import requests

response = requests.get("http://books.toscrape.com/")

print(response)

soup = BeautifulSoup(response.text, 'lxml')
print(soup.prettify())

content = soup.find('ol', class_='row')

# print(type(content))
# print(content)


