def isSaisiNbOK(nbEntier):
    isNbEntier = False

    while isNbEntier == False:
        if nbEntier.isnumeric() == False:
            print("Votre saisie n'est pas correcte ! Vous devez saisir un nombre entier positif !")
            nbEntier = input("Entrez un entier positif : ")
        else:
            isNbEntier = True
    
    return nbEntier

def calculFactorielle(intNbEntier) :
    if intNbEntier == 1 or intNbEntier == 0:
        factorielle = 1
    else:
        factorielle = 1
        while intNbEntier != 0:
            factorielle*=intNbEntier
            intNbEntier = intNbEntier - 1

    return factorielle
        

    