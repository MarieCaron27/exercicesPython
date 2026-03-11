import modules.fonctions

nombreSaisi = input("Entrez un nombre : ")
nombreSaisi = modules.fonctions.verificationNb(nombreSaisi)

somme = modules.fonctions.calculSomme(nombreSaisi)

if somme == int(nombreSaisi):
    print(f"Le nombre {nombreSaisi} est un nombre parfait")
else:
    print(f"Le nombre {nombreSaisi} n'est pas un nombre parfait")