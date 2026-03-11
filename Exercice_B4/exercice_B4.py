nbSaisi = input("Veuillez entrer un nombre qui soit multiple de 20 : ")
saisiOK = False

while saisiOK==False:
    if nbSaisi.isnumeric()==False:
        print("Votre saisi n'est pas un nombre, recommencez !")
        nbSaisi = input("Veuillez entrer un nombre : ")
        saisiOK = False
    elif int(nbSaisi)%20 != 0:
        print("Votre nombre n'est pas un multiple de 20 !")
        nbSaisi = input("Veuillez entrer un nombre : ")
        saisiOK = False
    else:
        saisiOK = True