variable = -1
somme = 0
produit = 1
compteur = 0
while int(variable) != 0:
    variable = input("Veuillez entrer un nombre (pour arrêter tapez sur 0) : ")
    if variable.isnumeric() == False:
        print("Votre variable n'est pas un nombre !")
        variable = input("Veuillez entrer un nombre (pour arrêter tapez sur 0) : ")
    elif int(variable) != 0:
        somme+=int(variable)
        produit*=int(variable)
        compteur+=1


moyenneArithmetique = somme/compteur
print(f"Voici les variables : somme = {somme}, produit = {produit}, moyenne arithmétique = {moyenneArithmetique} et compteur = {compteur}")
