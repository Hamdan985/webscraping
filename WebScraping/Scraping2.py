import requests
from bs4 import BeautifulSoup

source = requests.get('https://coinmarketcap.com/')

print(source)

# soup = BeautifulSoup(source, 'lxml')


# table = soup.find('table', class_='table floating-header')
# name = table.find('a', class_='currency-name-container link-secondary').text
# market_cap = table.find('td', class_='no-wrap market-cap text-right').text
# price = table.find('a', class_='price').text
# print(name)
# print(market_cap)
# print(price)
