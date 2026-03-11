import math

a = input("Entrez un premier nombre entier et différent de 0 : ")
b = input("Entrez un deuxième nombre entier : ")
c = input("Entrez un troisième nombre entier : ")
isNbOK = False

while isNbOK == False:
    if a.isnumeric() == False or b.isnumeric() == False or c.isnumeric() == False:
        print("Une ou plusieurs de vos saisies ne sont pas correctes ! Vous devez entrer trois nombres entiers !")
        a = input("Entrez un premier nombre entier et différent de 0 : ")
        b = input("Entrez un deuxième nombre entier : ")
        c = input("Entrez un troisième nombre entier : ")
    elif int(a) == 0:
        print("Le premier nombre doit être différent de 0 !")
        a = input("Entrez un premier nombre entier et différent de 0 : ")
    else:
        isNbOK = True

intA = int(a)
intB = int(b)
intC = int(c)

carreB = intB*intB
multiplication4AC = 4*intA*intC
soustraction = carreB-multiplication4AC
solution1 = (-intB+(math.sqrt(abs(soustraction))))/2*intA
solution2 = (-intB-(math.sqrt(abs(soustraction))))/2*intA

if solution1 == solution2:
    print(f"L'équation {a}x^2 + {b}x + {c} admet une solution : {round(solution1,2)}.")
elif solution1 == 0 or solution2 == 0:
    if solution1 == 0:
        print(f"L'équation {a}x^2 + {b}x + {c} admet une solution : {round(solution2,2)}.")
    else:
        print(f"L'équation {a}x^2 + {b}x + {c} admet une solution : {round(solution1,2)}.")
elif solution1 == 0 and solution2 == 0:
    print("L'équation admet 0 solution.")
else :
    print(f"L'équation {a}x^2 + {b}x + {c} admet deux solutions : {round(solution1,2)} et {round(solution2,2)}.")