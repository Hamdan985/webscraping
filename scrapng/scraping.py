from requests_html import HTML 

with open('simple.html') as source_file:
    file_content = source_file.read()
    source = HTML(html=file_content)

titles = []
links = []
summarys = []

divs = source.find('.article')
for div in divs:
    title = div.find('a', first=True)
    sum = div.find('p', first=True)

    titles.append(title.text)
    links.append(title.attrs['href'])
    summarys.append(sum.text)

for i in range(len(titles)):
    print(titles[i])
    print(links[i])
    print(summarys[i])
    print()