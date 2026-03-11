limiteImpairs = input("Entrez un nombre entier : ")
isLimiteEntier = False

while isLimiteEntier == False:
    if limiteImpairs.isnumeric() == False:
        print("Votre saisie n'est pas un nombre !")
        limiteImpairs = input("Entrez un nombre entier :")
        isLimiteEntier=False
    else:
        isLimiteEntier=True
    
intLimiteImpairs = int(limiteImpairs)

i=1
carre=0
sommeCarre=0
compteur=0
while compteur < intLimiteImpairs:
    carre=i*i
    sommeCarre+=carre
    i+=2
    compteur+=1

print(f"Voici le carré de la somme des {limiteImpairs} premiers nombre imprairs : {sommeCarre}")