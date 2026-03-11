import random;
import modules.fonctions;

length = input("Entrez la taille de votre liste (un nombre compris entre 0 et 30) : ")
newLength = modules.fonctions.isLengthOK(int(length))
myList = []

for i in range(int(newLength)):
    myList.append(random.random())

for item in myList:
    print(item)
    