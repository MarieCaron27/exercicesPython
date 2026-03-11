nbEntier = []
nbEntierSaisi = 0

while int(nbEntierSaisi)!=-1: 
    nbEntierSaisi = input("Veuillez entrer un nombre naturel : ")

    if int(nbEntierSaisi) !=-1:
        nbEntier.append(int(nbEntierSaisi))


tailleNbEntiers = len(nbEntier)

if tailleNbEntiers == 0:
    raise SystemExit("Aucun nombre saisi !")

i=0
somme=0
while i < tailleNbEntiers:
    somme += nbEntier[i]
    i+=1

moyenne = somme/tailleNbEntiers
print(f"Voici la moyenne de vos valeurs entières : {moyenne}")