def verificationNbs(premierEntier,deuxiemeEntier):
    isNbOK = False

    while isNbOK == False:
        if premierEntier.isnumeric() == False or deuxiemeEntier.isnumeric() == False:
            print("Vos saisies ne sont pas des nombres, recommencez !")
            premierEntier = input("Entrez un premier entier : ")
            deuxiemeEntier = input("Entrez un deuxième entier (plus petit que le premier) : ")
        elif int(premierEntier) <= int(deuxiemeEntier):
            print("Votre deuxième entier doit être plus petit que le premier !")
            premierEntier = input("Entrez un premier entier : ")
            deuxiemeEntier = input("Entrez un deuxième entier (plus petit que le premier) : ")
        else:
            isNbOK = True
    
    return premierEntier,deuxiemeEntier

def calculPGCD(intPremierEntier,intDeuxiemeEntier):
    soustraction = intPremierEntier - intDeuxiemeEntier
    i = intDeuxiemeEntier

    while soustraction != i:
        if soustraction > i:
            soustraction = soustraction - i
        else:
            i = i - soustraction

    return i

def menuFinProgramme():
    print("\nSouhaitez-vous recommencez ce programme ou l'arrêter ?")
    print("\nPour continuer, tapez 27.")
    print("\nSinon, tapez sur une autre touche de votre clavier.")
    valeurClavier = input("Allez-y : ")

    return valeurClavier

    