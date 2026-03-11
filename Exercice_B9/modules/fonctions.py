def verificationEntiers(a,b,c):
    isNbOk = False
    while isNbOk == False:
        if a.isnumeric() == False or b.isnumeric() == False or c.isnumeric() == False:
            print("Un ou plusieurs de vos nombres ne sont pas numérique !")
            a = input("Entrez un premier entier : ")
            b = input("Entrez un deuxième entier : ")
            c = input("Entrez un troisième entier : ")
        elif int(a) >= int(b) or int(b) >= int(c):
            print("Votre premier entier doit être plus grand que le deuxième qui lui-même doit être plus grand que le troisième !")
            a = input("Entrez un premier entier : ")
            b = input("Entrez un deuxième entier (plus grand que a) : ")
            c = input("Entrez un troisième entier (plus grand que b) : ")
        else:
            isNbOk=True
    
    return a,b,c

def sommeIntervaleAB(intA,intB):
    i=intA
    somme=0
    while i == intA or i < intB:
        somme+=i
        i+=1
    
    return somme

def sommeIntervaleSansASansB(intA,intB):
    i=intA
    somme=0
    while i < intB:
        if i != intA:
            somme+=i
        i+=1
    
    return somme

def sommeIntervaleASansB(intA,intB):
    i=intA
    somme=0
    while i == intA or i < intB:
        if i%2==0:
            somme+=i
        i+=1
    
    return somme

def sommeDiviseursC(intA,intB,intC):
    i=intA
    somme=0
    while i == intA or i < intB:
        if intC%i==0:
            somme+=i
        i+=1
    
    return somme