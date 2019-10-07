import requests_html
from requests_html import HTMLSession,HTML,HTMLResponse
import time 


session = HTMLSession()
response = session.get("https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=6974e394-29b2-4edc-824f-b3a0fa708b2d")

source = response.html

block = source.find('._1HmYoV,._35HD7C', first=True)


sets = block.find('._1UoZlX')

output_set = []
for x in sets:
    if x not in output_set:
        output_set.append(x)

frp = sets.find('._1vC4OE, ._2rQ-NK')


for set in output_set:
    name = set.find('div._3wU53n', first=True)
    print(name.text)

print(len(frp))
print(len(output_set))