import modules.fonctions

nbSaisi = input("Entrez un nombre plus grand que 0 :")
nbSaisi = modules.fonctions.saisiNb(nbSaisi)

intNbSaisi = int(nbSaisi)
modules.fonctions.isNbParfait(intNbSaisi)