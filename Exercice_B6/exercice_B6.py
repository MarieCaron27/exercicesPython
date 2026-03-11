import modules.fonctions

valeurClavier = '27'
while valeurClavier == '27':
    premierEntier = input("Entrez un premier entier : ")
    deuxiemeEntier = input("Entrez un deuxième entier (plus petit que le premier) : ")

    mesEntiers = modules.fonctions.verificationNbs(premierEntier,deuxiemeEntier)

    i=0
    while i < len(mesEntiers):
        premierEntier = mesEntiers[i]
        deuxiemeEntier = mesEntiers[i+1]
        i=len(mesEntiers)

    intPremierEntier = int(premierEntier)
    intDeuxiemeEntier = int(deuxiemeEntier)

    pGCD = modules.fonctions.calculPGCD(intPremierEntier,intDeuxiemeEntier)

    print(f"Voici le PGCD de {intPremierEntier} et {intDeuxiemeEntier} : {pGCD}.")
    valeurClavier = modules.fonctions.menuFinProgramme()

    if valeurClavier != '27':
        print('Fin du programme !')

