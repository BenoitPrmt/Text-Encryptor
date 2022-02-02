from encryptor.azerty import Azerty
from encryptor.zigzag import ZigZag

choice = input("Choisissez un mode: \n1 - Chiffrer\n2 - Déchiffrer\n")
mot = input("Entrez le mot à chiffrer:\n")
format = input("Entrez le format: \n1 -> Azerty\n2 -> ZigZag\n")

if(format == "1"):
    azerty = Azerty()

    if(choice == "1"):
        motChiffre = azerty.chiffrer(mot)
        print("Mot chiffré: " + motChiffre)

    else: 
        motChiffre = azerty.dechiffrer(mot)
        print("Mot déchiffré: " + motChiffre)

elif(format == "2"):
    zigzag = ZigZag()

    if(choice == "1"):
        motChiffre = zigzag.chiffrer(mot)
        print("Mot chiffré: " + motChiffre)

    else: 
        print("Il n'est pas possible de déchiffrer un mot sous le format ZigZag")