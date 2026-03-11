myDate = input("Entrez une date au format jj/mm/yyyy : ")
isDateOK = False

while isDateOK == False:
    if len(myDate) != 10:
        print("La taille de votre date est trop grande ou trop petite... Recommencez !")
        myDate = input("Entrez une date au format jj/mm/yyyy : ")
    elif myDate[0].isnumeric() == False or myDate[1].isnumeric() == False or myDate[2] != '/' or myDate[3].isnumeric() == False or myDate[4].isnumeric() == False or myDate[5] != '/' or myDate[6].isnumeric() == False or myDate[7].isnumeric() == False or myDate[8].isnumeric() == False or myDate[9].isnumeric() == False:
        print("Le format de votre date est incorrecte ! Recommencez !")
        myDate = input("Entrez une date au format jj/mm/yyyy : ")
    else:
        isDateOK = True


jour, mois, annee = myDate.split("/")

jour = int(jour)
mois = int(mois)
annee = int(annee)

if annee >= 1990 and annee <= 2026:
    if (annee%4 == 0 and annee%100 != 0) or annee%400 == 0:
        print("Annee bissextile")
    else:
        print("Annee non bissextile")       
else:
    raise SystemExit("L'année de votre date n'est pas correcte. Elle doit être comprise entre 1990 et 2026 !")



     