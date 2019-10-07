import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.wsj.com/market-data').text

soup = BeautifulSoup(source, 'lxml')

# Find all the HTML tables on the page
tables = soup.find_all('table')

# Loop through all of the tables
for table in tables:
	# Access the table's body
	table_body = table.find('tbody')
	# Grab the rows from the table body
	rows = table_body.find_all('tr')

	# Loop through the rows
	for row in rows:
    	    # Extract each HTML column from the row
    	    columns = row.find_all('td')

    	    # Loop through the columns
    	    for column in columns:
        	  # Print the column value
        	  print(column.text)