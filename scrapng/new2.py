import requests
from bs4 import BeautifulSoup
import csv

csv_file = open("imdb.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title','Time','Genre','Rating','Summary','Director/s','Stars'])

source = requests.get("https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs").text
soup = BeautifulSoup(source, 'lxml')

movies = soup.findAll(class_="nm-title-overview-widget-layout")
# print(movies)
for movie in movies:
    title = movie.h4.text
    print(title)
    try:
        time = movie.time.text
        print(time)
    except:
        print("None") 
    genre = []
    for genres in movie.p.findAll("span"):
        # print(genres.text)
        genre.append(genres.text)

    # print(genre)
    try:
        rating = movie.find(class_="rating_txt").span.text
        print(rating)
    except:
        rating = "None"
        print(rating)

    desc = movie.find(class_="outline").text
    print(desc)
    x = []
    cast = movie.findAll("div" ,class_="txt-block")
    for element in cast:
        # print(element.text)
        x.append(element.text)
    dir = x[0]
    stars = x[1]
    # print(x)
    print(dir)
    print(stars)
    csv_writer.writerow([title,time,genre,rating,desc.strip(' '),dir,stars])
csv_file.close()
