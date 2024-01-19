import requests #Utile pour récupérer du contenu sur une page
from bs4 import BeautifulSoup #beautifulsoup est la pour parser  les contenus.
#! pip install beautifulsoup4
# ETL -> Extract, Transform, Load

url = "https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
page = requests.get(url)

# Scrap
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find('h1').string
price = soup.find('p', class_='price_color').string
print(title, price)

# Obtenir par balise -> .find('balise') 
# Obtenir par classe -> .find_all('class_='class_name')
# Obtenir par titre de page -> soup.title
# Obtenir par ID -> soup.find(id="id")

# Convertir en chaine -> .string
#! Il est possible de récupérer plusieurs objets avec un find_all, et de les envoyer dans une liste avec une boucle for x in elements_recup -> liste.append(x.string)
