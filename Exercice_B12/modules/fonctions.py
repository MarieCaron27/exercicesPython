def verificationNb(nombreSaisi):
    isNbOK = False

    while isNbOK == False:
        if nombreSaisi.isnumeric() == False:
            print("Votre saisie n'est pas correcte, vous devez entrer un nombre : ")
            nombreSaisi = input("Entrez un nombre : ")
        else:
            isNbOK = True

    return nombreSaisi


def calculSomme(nombreSaisi):
    diviseur = 1
    somme = 0

    while diviseur < int(nombreSaisi):
        if int(nombreSaisi)%diviseur==0:
            somme+=diviseur
        diviseur+=1

    return somme