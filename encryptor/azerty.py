mot = input("Quel mot souhaitez vous encoder en AZERTY ?")

# On génère 2 listes :
# La première est la liste des caractères du clavier Azerty
# La seconde est la liste des caractères du clavier Azerty décalés d'un cran
clavier = ['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'w', 'x', 'c', 'v', 'b', 'n', ' ']
clavier2 = ['z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'q', 'x', 'c', 'v', 'b', 'n', 'w', ' ']

motFinal = ""

# Pour chaque lettre dans le mot on prend celle qui a la même position mais dans l'autre liste (donc décalée de 1 cran)
for lettre in mot:
    motFinal += clavier2[clavier.index(lettre)]
print(motFinal) # Renvoi le mot codé avec le code Azerty