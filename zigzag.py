# Format du code ZigZag
# X---X---X---X---X---X
# -X-X-X-X-X-X-X-X-X-
# --X---X---X---X---X

mot = input("Quel est le mot que vous souhaitez coder en ZIGZAG ?")

ligne1 = mot[::4] # on prend un lettre sur 4
ligne2 = mot[1::2] # on prend un lettre sur 2 mais pas la 1re
ligne3 = mot[2::4] # on prend un lettre sur 4 a partir de la 3e

print(tab1 + tab2 + tab3) #Renvoi le message codé avec le code ZigZag