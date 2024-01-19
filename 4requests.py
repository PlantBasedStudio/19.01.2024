import requests

resultat = requests.get('https://google.com/')
print(resultat.content) #Retourne tout la page