# Lire un fichier -> open("fichier.txt", "r").   ->>>> MODE PAR DEFAUT SI PAS SPÉCIFIÉ
# Ecrire ("écraser") dans un fichier -> open("fichier.txt", "w").
# Ecrire ("Continuer") dans un fichier -> open("fichier.txt", "a").
# Lire + Ecrire ("Continuer") dans un fichier -> open("fichier.txt", "r+").

#! Création d'un txt
file = open("Hello.txt", "w")
file.write("Hello, Damien!")
file.close()

#! On peut aussi fermer automatiquement le fichier à la fin du bloc d'instruction
with open("Hello.txt") as file:
    for line in file:
        print(line)

#! Pour les CSV, il existe aussi un package Python -> csv.
    #reader() -> lire
    #writer() -> Ecrire
    #DictReader() -> lire l'entête sur la première ligne puis définit les autres suivante en tant que dictionnaire. Fixe la clé sur la première ligne
    #? DictWriter ??
