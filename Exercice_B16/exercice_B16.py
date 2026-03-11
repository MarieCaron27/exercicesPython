import modules.fonctions

nbEntier = input("Entrez un entier positif : ")
nbEntier = modules.fonctions.isSaisiNbOK(nbEntier)

intNbEntier = int(nbEntier)
factorielle = modules.fonctions.calculFactorielle(intNbEntier)
print(f"La factorielle de {nbEntier} vaut {factorielle}")