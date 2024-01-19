
#! Déclaration des variables :

#! String 
book = "Gatsby le Mangnifique"

#! Affectation d'une nouvelle valeur : 
book = "Moby Dick"
print(book)
# -> "Moby Dick"

#! Integer 
year = 1996

#! Float
price = 9.9


#! f-string
first_name = "Jackie" #snake_case
last_name = "Tuning" #snake_case
age = 99
print(f"Bonjour, je m'appelle {first_name} {last_name} et j'ai {age} ans.")
# La F-string permet d'afficher un ensemble de valeur dans une string en appellant les variables avec {}


#! boolean
is_true = True
is_false = False

#! Determiner un type avec la fonction type()
print(type(first_name))
# Retourne str


#!Liste (ensemble d'éléments):
fruits = ["apple", "orange", "pineapple", "strawberry"]
print(fruits[0]) # Affichera apple
print(fruits[-1]) # Affichera strawberry

#!Une string est une liste
print(first_name[2]) # retourne C

#!Affectation d'un élément de liste : 
fruits[0] = "Banana"
print(fruits[0]) # Affichera Banana

#!Ajouter un élement :
fruits.append("Lemon")

#!Retirer :
fruits.remove("Banana")

#!longueur element
print(len(fruits))

#!trier Alphabetique :
fruits.sort()
print(fruits)

#!Ajouter +++ element :
fruits.extend("Kiwi") #Iteration de chaque element !
print(fruits)

#!Tuples - NON MODIFIABLE : 
social_media = ("Facebook", "Twitter", "Google+")

#! Trouver un element : (in)
print("Banana" in fruits) #False


#!Dictionary
my_dictionary ={"key":"value"}

props = {
    'name' : 'test',
    'begin_date' : "02-28-2024",
    'end_date' : "02-29-2024",
    'image_url' : "/img/eaz.png",
    'price' : "8.9"
}
print(props['name'])
#On peut aussi créer un dict en disant par exemple props = dict() ou encore propos = {}

#!Supprimer clé:valeur
del(props["price"])
print(props.keys())