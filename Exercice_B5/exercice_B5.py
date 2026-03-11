premierNb = input("Entrez un premier entier : ")
deuxiemeNb = input("Entrez un deuxième entier (plus petit que le premier) : ")
isNbOk = False

while isNbOk == False:
    if premierNb.isnumeric() == False or deuxiemeNb.isnumeric() == False:
        print("Vous n'avez pas saisi des nombres !")
        premierNb = input("Entrez un premier entier : ")
        deuxiemeNb = input("Entrez un deuxième entier : ")
        isNbOk = False
    elif int(premierNb) <= int(deuxiemeNb):
        print("Le premier entier est plus petit que le deuxième !")
        premierNb = input("Entrez un premier entier : ")
        deuxiemeNb = input("Entrez un deuxième entier : ")
        isNbOk = False
    else:
        isNbOk=True

intPremierNb = int(premierNb)
intDeuxiemeNb = int(deuxiemeNb)

while intPremierNb != intDeuxiemeNb:
    if intPremierNb > intDeuxiemeNb:
        intPremierNb = intPremierNb - intDeuxiemeNb
    else:
        intDeuxiemeNb = intDeuxiemeNb - intPremierNb

print(f"Voici le PGCD de {premierNb} et de {deuxiemeNb} : {intPremierNb}")