def saisiNb(nbSaisi):
    isNbOk = False

    while isNbOk == False:
        if nbSaisi.isnumeric() == False or int(nbSaisi) <= 0:
            print("Votre saisie est incorrecte ! Vous devez entrer un nombre supérieur à 0")
            nbSaisi = input("Entrez un nombre plus grand que 0 :")
        else:
            isNbOk = True
    
    return nbSaisi

def isNbParfait(intNbSaisi):
    compteur = 1
    while intNbSaisi != 0:
        compteur = 1
        somme=0
        while compteur <= intNbSaisi: 
            if intNbSaisi%compteur==0 and compteur != intNbSaisi:
                somme+=compteur
            compteur+=1
            
        if intNbSaisi == somme and intNbSaisi != 1:
            print(f"Le nombre {intNbSaisi} est parfait")
            
        intNbSaisi=intNbSaisi-1