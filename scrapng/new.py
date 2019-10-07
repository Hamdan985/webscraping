from requests_html import HTMLSession,HTMLResponse
# import urllib.request 

urls = ["http://books.toscrape.com/catalogue/page-1.html"]
for no in range(1,51):
    urls.append(f"http://books.toscrape.com/catalogue/page-{no}.html")

for url in urls:
    session = HTMLSession()
    response = session.get(url)
    # print(response)

    source = response.html 

    # print(type(source))
    # print(source)

    block = source.find('ol.row', first=True)
    # print(block)

    name = []
    cost = []
    images = []

    titles = block.find('li h3 a')
    for title in titles:
        # print(title.attrs['title'])
        name.append(title.attrs['title'])


    prices = block.find('li p.price_color')
    for price in prices:
        # print(price.text[1:])
        cost.append(price.text[1:])

    pics = block.find('li div.image_container img')
    for pic in pics:
        # print("http://books.toscrape.com/"+pic.attrs['src'])
        images.append("http://books.toscrape.com/"+pic.attrs['src'])

    for i in range (len(name)):
        print(i," ::")
        print(name[i])
        print(cost[i])
        print(images[i])
        print()
        # urllib.request.urlretrieve(images[i], name[i])

    


