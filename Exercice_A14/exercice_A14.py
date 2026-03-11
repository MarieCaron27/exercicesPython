premierNombre = input("Entrez un premier entier positif : ")
deuxiemeNombre = input("Entrez un deuxième entier positif : ")
operande = input("Entrez une opérande (+,-,*,/) : ")

isNbOk = False
while isNbOk == False:
    if premierNombre.isnumeric() == False or deuxiemeNombre.isnumeric() == False:
        print("Vos saisies sont incorrectes ! Vous devez entrer deux entiers positifs !")
        premierNombre = input("Entrez un premier entier positif : ")
        deuxiemeNombre = input("Entrez un deuxième entier positif : ")
    else:
        isNbOk = True

intPremierNombre = int(premierNombre)
intDeuxiemeNombre = int(deuxiemeNombre)

resultat = 0
match operande:
    case '+':
        resultat = intPremierNombre+intDeuxiemeNombre
    case '-':
        resultat = intPremierNombre-intDeuxiemeNombre
    case '*':
        resultat = intPremierNombre*intDeuxiemeNombre
    case '/':
        if intDeuxiemeNombre == 0:
            raise SystemExit('Le dénominateur vaut 0 !')
        else:
            resultat = intPremierNombre/intDeuxiemeNombre
    case _:
        raise SystemExit('Votre opérande est incorrecte !')
    

print(f"Le résultat de l'opération {intPremierNombre}{operande}{intDeuxiemeNombre} vaut {resultat}")