somme = 0
while somme != 9:
    nbSaisi = input("Entrez un nombre compris entre 100 et 999 : ")

    isBoucleOK = False
    while isBoucleOK == False:
        if nbSaisi.isnumeric() == False or (int(nbSaisi) < 100 or int(nbSaisi) > 999):
            print("Votre nombre doit être compris entre 100 et 999 !")
            nbSaisi = input("Entrez un nombre compris entre 100 et 999 : ")
        else:
            isBoucleOK = True

    i=0        
    while i < len(nbSaisi):
        premierChiffre = nbSaisi[i]
        deuxiemeChiffre = nbSaisi[i+1]
        troisiemeChiffre = nbSaisi[i+2]
        i=len(nbSaisi)+1

    somme = int(premierChiffre) + int(deuxiemeChiffre) + int(troisiemeChiffre)

    if somme == 9:
        print(f"Félicitations, la somme de vos chiffres du nombre {nbSaisi} vaut bien 9 !")
    else:
        print(f"La somme de vos chiffres du nombre {nbSaisi} ne vaut pas 9, recommencez !")

    