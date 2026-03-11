def isLengthOK(length):
    isCoordOK = False

    while isCoordOK == False:
        if int(length) >= 1 and int(length) <= 30:
            isCoordOK = True
        else:
            print("Taille non ok !")
            length = input("Entrez la taille de votre liste (un nombre compris entre 0 et 30) : ")
            
            isCoordOK = False

    return length
