entierAMultiplier = input("Veuillez entrez un entier : ")
limiteMultiplication = input("Jusqu'à quel nombre souhaitez-vous mutliplier votre entiez : ")

if entierAMultiplier.isnumeric() == False or limiteMultiplication.isnumeric() == False:
    raise SystemExit("Vos saisies ne sont pas des nombres !")

intEntierAMultiplier = int(entierAMultiplier)
intLimiteMultiplication = int(limiteMultiplication)

i=0
while i <= intLimiteMultiplication:
    resultat = i*intEntierAMultiplier
    print(f"Voici la multiplication de {i} par {intEntierAMultiplier} : {resultat}")
    i+=1

