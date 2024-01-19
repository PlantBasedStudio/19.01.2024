import csv
import requests 
from bs4 import BeautifulSoup 

#url
url_travel = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
page = requests.get(url_travel) #contenu de la page

soup = BeautifulSoup(page.content, 'html.parser') #parser de la page

titles = []
for link in soup.find_all('h3') :
    title = link.find("a")
    titles.append(title.string)
    
prices = []
for price in soup.find_all('p', class_='price_color') :
    prices.append(price.string)

print(titles[0])
print(prices[0])

#Definir une en-tête
header = ['Title', 'Price_including_tax'] #Fournir un agent utilisateur ? 

with open("data.csv", "w") as file_csv:
    writer = csv.writer(file_csv, delimiter=",")
    writer.writerow(header)
    for titles, prices in zip(titles, prices):
        line = [titles, prices]
        writer.writerow(line)