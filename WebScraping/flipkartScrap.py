from requests_html import HTMLSession, HTML
import csv
session = HTMLSession()

for no in range(1,10):
    response = session.get(f'https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_6_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_0_6_na_na_pr&as-pos=0&as-type=RECENT&suggestionId=mobiles&requestId=d0404e7f-0b71-47c6-8077-89a0a4e30015&as-backfill=on&page={no}')
    html = response.html
    
    # csv_file = open('flipkartScraped.csv','w')
    # csv_writer = csv.writer(csv_file)
    # csv_writer.writerow(['NAME', 'MRP', 'FRP'])


    blocks = html.find('.bhgxx2')
    for block in blocks:
        name = block.find('._3wU53n', first=True).text
        try:
            before_price = block.find('._2GcJzG', first=True).text
        except Exception as e:
            before_price = 'NOT FOUND'
        try:
            final_price = block.find('._2rQ-NK',first=True).text
        except Exception as e:
            final_price = 'NOT FOUND'
        # print(block.text)
        print("\n\n NAME : ",name)
        print("\n\n MRP : ",before_price[1:])
        print("\n\n FRP : ",final_price[1:])
    #     # csv_writer.writerow([])

  