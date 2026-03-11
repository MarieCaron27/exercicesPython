x = input("Veuillez entrer un premier entier positif (compris entre 0 et 2) : ")
y = input("Veuillez entrer un deuxième entier positif (compris entre 0 et 2) : ")
monPlan = [[7,2,6],[3,5,1],[8,4,9]]

isNbOK = False
while isNbOK == False:
    if x.isnumeric() == False or y.isnumeric() == False or int(x) > 2 or int(y) > 2:
        print("Vos saisies ne sont pas correctes ! Vous devez entrer deux entiers positifs compris entre 0 et 2 !")
        x = input("Veuillez entrer un premier entier positif (compris entre 0 et 2) : ")
        y = input("Veuillez entrer un deuxième entier positif (compris entre 0 et 2) : ")
    else:
        isNbOK = True


intX = int(x)
intY = int(y)
p=0

for intX in monPlan:
    for intY in intX:
        p=monPlan[int(x)][int(y)]


print(f"On retrouve le point {p} aux coordonnées {x} et {y}")