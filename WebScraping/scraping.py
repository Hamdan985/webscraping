from requests_html import HTML, HTMLSession
import csv

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    html.render()

match = html.find('#footer', first=True)
print(match.html)

# print(html.full_text)
# articles = html.find('div.article')
# for article in articles:
#     headline = article.find('h2', first=True).text
#     summary = article.find('p', first=True).text

#     print(headline)
#     print(summary)


# csv_file = open('scraped.csv','w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['HEADLINE', 'SUMMARY', 'VIDEO'])


# session = HTMLSession()
# response = session.get('https://coreyms.com/')
# html = response.html

# articles = html.find('article')

# for article in articles:

#     headline = article.find('.entry-title-link', first=True).text
#     summary = article.find('.entrycsv_file = open('scraped.csv','w')content p', first=True).text

#     vid_scr = article.find('iframecsv_writer = csv.writer(csv_file), first=True).attrs['src']
#     vid_id = vid_scr.split('/')[4]csv_writer.writerow(['HEADLINE', 'SUMMARY', 'VIDEO'])
#     yt_link = vid_id.split('?')[0]

#     yt_link = f'https://youtube.com/watch?v={yt_link}'

#     print("HEADLINE\n",headline)
#     print("\nSUMMARY" ,summary)
#     print("\nYOUTUBE LINK : ",yt_link) 

#     csv_writer.writerow([headline, summary, yt_link])

# csv_file.close()