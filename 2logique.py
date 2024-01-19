
##! Instructions conditionnelles 
time_is_good = False
if time_is_good :
    print("Let's go the beach guys!")
else:
    print("stay home!")
    
hot = False

#! Structuration avec opérateur logique
if not time_is_good and not hot :
    print("Close the window!")
elif time_is_good and not hot :
    print("Get out but take a jacket!")




##!Opérateur de comparaison : == , != , >, < , <=, >= 
print(hot == True) #return False


#!match : 
fruit = "apple"
match fruit:
    case 'apple':
        print("yes, that's definitely an apple!")
    case 'Bananalalalalalalalalalalalalalalalal':
        print("I think, you should learn what's an apple")
    case _:
        print("No")

#! LOOP

#! For
dog_types = ["golden", "chihuahua", "bulldog"]

for dog in dog_types:
    print("This is a", dog)
#Boucle d'itération sur chaque élement

#! While
max_capacity = 10
actual_capacity = 3
while actual_capacity < max_capacity:
    actual_capacity += 1
# Boucle d'éxécution sur une condition donnée : TANT QUE .. ALORS


#! BREAK - CONTINUE
for i in range(10):
    if i == 5:
        break
#Stoppe le code une fois arrivé à 5 
for i in range(10):
    if i == 3:
        continue #mean, skip this step
        #Do something in other cases here
        
#! functions
def ma_fonction(argument): 
    """Définition

    Args:
        argument (_type_): Attends un argument quelconque pour l'écrire

    Returns:
        _type_: Retournera cet argument
    """
    print(argument)
    return argument

#! Exception / Erreur
while True:
    try:
        x = int(input("Entrez un nombre : "))
        break
    except ValueError:
        print("WRONG, this is not a number")