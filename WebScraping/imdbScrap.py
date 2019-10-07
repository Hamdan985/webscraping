from requests_html import HTMLSession, HTML
import csv
session = HTMLSession()
response = session.get('https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth')
html = response.html


csv_file = open('imdbScraped.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['TITLE', 'RATING', 'RUNTIME','GENRE', 'SUMMARY', 'DIRECTOR','ACTORS'])

names = html.find('.nm-title-overview-widget-layout')
for name in names:
    title = name.find('h4 a', first=True).text

    runTime = name.find('.cert-runtime-genre time', first=True).text
    genre = name.find('.cert-runtime-genre span', first=True).text

    try:
        rating = name.find('.rating_tx', first=True).text
    except Exception as identifier:
        rating = 'None'

    outline = name.find('.outline', first=True).text

    director = name.find('.txt-block span a', first=True).text

    stars = name.find('.txt-block a')

    # print("ACTORS")
    iter_stars = iter(stars)
    next(iter_stars)

    for star_name in iter_stars:
        print(star_name.text)
    print(type(iter_stars))

    csv_writer.writerow([title, rating, runTime,genre,outline,director,star_name.text])

# print(name.html)
# print(html.html)