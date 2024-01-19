import csv
import requests 
from bs4 import BeautifulSoup 
import re

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
page = requests.get(url) #contenu de la page

soup = BeautifulSoup(page.content, 'html.parser') #parser de la page

product_page_url = url

table = soup.find('table', class_="table")
book = {
    
}
rows = soup.find_all('tr')
for row in rows:
    key = row.find('th').string
    value = row.find('td').string
    book[key] = value

universal_product_code = book['UPC']
title = soup.find('h1')
price_including_tax = book['Price (incl. tax)']
price_excluding_tax = book['Price (excl. tax)']
number_available = int(
    (re.search(
        r'\d+', book['Availability']
        )
    ).group()
    )  #! a revoir je pense
product_description = soup.find('p').string  #! pas bon
category = "test" #! non plus
review_rating = book['Number of reviews'] #! pas ça je pense
image_url = "test" #! pas bon

