import modules.fonctions

a = input("Entrez un premier entier : ")
b = input("Entrez un deuxième entier (plus grand que a) : ")
c = input("Entrez un troisième entier (plus grand que b) : ")

mesEntiers = modules.fonctions.verificationEntiers(a,b,c)

i=0
intA=0
intB=0
intC=0
while i < len(mesEntiers):
    intA = int(mesEntiers[i])
    intB = int(mesEntiers[i+1])
    intC = int(mesEntiers[i+2])
    i=len(mesEntiers)+1

somme = modules.fonctions.sommeIntervaleAB(intA,intB)
print(f"Voici la somme compris dans l'intervale [ {intA} ; {intB} [ : {somme}") 

somme = modules.fonctions.sommeIntervaleSansASansB(intA,intB)
print(f"Voici la somme compris dans l'intervale ] {intA} ; {intB} [ : {somme}") 

somme = modules.fonctions.sommeIntervaleASansB(intA,intB)
print(f"Voici la somme des nombres pairs compris dans l'intervale [ {intA} ; {intB} [ : {somme}") 

somme = modules.fonctions.sommeDiviseursC(intA,intB,intC)
print(f"Voici la somme des diviseurs de {intC} compris dans l'intervale [ {intA} ; {intB} [ : {somme}")