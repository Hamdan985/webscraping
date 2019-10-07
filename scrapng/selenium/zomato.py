
import requests_html
from requests_html import HTMLSession,HTML,HTMLResponse

urls = ["https://www.zomato.com/mumbai/order-food-online?utm_source=google&utm_medium=cpc&utm_term=zomato&utm_campaign=Gsearch_P-MWeb_O-NA_C-Brand_A-NewUser_SC-Generic_L-Mumbai&gclid=Cj0KCQjwoebsBRCHARIsAC3JP0LTvRcTJT2USytMfTfxJ_Om0mFCGwUxrmm-GYRHevB48MTIGbPhnKcaAqoqEALw_wcB&page=1"]
for no in range(1,5):
    urls.append("https://www.zomato.com/mumbai/order-food-online?utm_source=google&utm_medium=cpc&utm_term=zomato&utm_campaign=Gsearch_P-MWeb_O-NA_C-Brand_A-NewUser_SC-Generic_L-Mumbai&gclid=Cj0KCQjwoebsBRCHARIsAC3JP0LTvRcTJT2USytMfTfxJ_Om0mFCGwUxrmm-GYRHevB48MTIGbPhnKcaAqoqEALw_wcB&page={no}")

for url in urls:
    session = HTMLSession()
    response = session.get(url)
    source = response.html 
    box = source.find("div#orig-search-list", first=True)
    # print(box)

    hotels = box.find(" .card search-o2-card, .mr0")
    # print(hotel)
    for hotel in hotels:
        name = hotel.find("a", first=True)
        print("Name : ",name.text)

        type = hotel.find(".grey-text nowrap, .ln24 ", first=True)
        print("Type",type.text)

        image = hotel.find(".feat-img", first=True)
        print("Image :",image.attrs['data-original'].split('?')[0])



# rating = hotel.find(".rating-popup, .rating-for-36403, .res-rating-nf, .right, .level-7, .bold, .visible", first = True)
# print(rating.text)
