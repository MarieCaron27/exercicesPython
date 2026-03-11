def saisiNombre(nbSaisi):
    isNbOk = False

    while isNbOk == False:
        if nbSaisi.isnumeric() == False or int(nbSaisi) <= 0:
            print("Votre saisie est incorrecte ! Vous devez entrer un nombre supérieur à 0")
            nbSaisi = input("Entrez un nombre plus grand que 0 :")
        else:
            isNbOk = True
    
    return nbSaisi

def calculNbPremier(intNbSaisi):
    compteur = 1
    while intNbSaisi != 0:
        compteur = 1
        notNbPremier = False
        while compteur <= intNbSaisi and notNbPremier == False: 
            if compteur != 1 and compteur != intNbSaisi:
                if intNbSaisi%compteur==0:
                    notNbPremier = True
            compteur+=1
        
        if notNbPremier == False and intNbSaisi != 1:
            print(f"Le nombre {intNbSaisi} est premier")
        
        intNbSaisi=intNbSaisi-1