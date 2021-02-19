import math

def debugTableau(tableau):
    print("##########")
    for ligne in tableau:
        print(ligne)
    print("##########")


mot = input("Quel mot souhaitez vous encoder en SPIRALE ?")

# Arrondi supérieur de la racine carré de la longueur du mot
nombre = math.ceil(math.sqrt(len(mot)))

# Créer une liste des caractères du mot
mot2 = []
for lettre in mot:
    mot2.append(lettre)
print(mot2)


# Créer un tableau vide (rempli de *) avec une taille adaptée au mot
tableau = []
ligne = []
for i in range(nombre):
    for j in range(nombre):
        ligne.append("*")
    tableau.append(ligne)
    ligne = []
print(tableau)

longueurMaxTableau = nombre -1
longueurMinTableau = 0

ligne = 0
colonne = longueurMaxTableau


# On place les lettres dans le tableau en partant d'en haut à droite
for lettre in mot2:
    print(f"debug coo:lettre='{lettre}', ligne={ligne}, colonne={colonne}")
    tableau[ligne][colonne] = lettre

    if colonne == longueurMaxTableau and ligne != longueurMaxTableau: # deplacement vers le bas
        ligne += 1
    
    elif ligne == longueurMaxTableau and colonne != longueurMinTableau : # nombre-1 = 2 si c'est la derniere ligne mais pas la dernier e colonne on se deplace ver la droite
        colonne -= 1
    
    elif colonne == longueurMinTableau and ligne != longueurMinTableau: # deplacment vers le haut
        ligne -= 1
    
    elif ligne == longueurMinTableau and colonne != longueurMaxTableau: # deplacement vers la droite
        colonne += 1


    if ligne == longueurMinTableau and colonne == longueurMaxTableau:
        longueurMaxTableau -= 1
        longueurMinTableau += 1

        ligne = longueurMinTableau
        colonne = longueurMaxTableau

    debugTableau(tableau)

motFinal=""

# On rejoint chaque ligne du tableau et on les mets dans la variable "motFinal"
for ligne in tableau:
    motFinal += "".join(ligne)

print(motFinal) # Renvoi le mot codé avec le code Spirale