clavier = ['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'w', 'x', 'c', 'v', 'b', 'n', ' ']
clavier2 = ['z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'q', 'x', 'c', 'v', 'b', 'n', 'w', ' ']

class Azerty:

    def __init__(self) -> None:
        pass

    def chiffrer(self, mot):
        """Permet de chiffrer du texte sous le format Azerty

        Args:
            mot ([String]): Mot à chiffrer

        Returns:
            [String]: Mot chiffré
        """

        mot.lower()

        motFinal = ""
        for lettre in mot:
            motFinal += clavier2[clavier.index(lettre)]
        return motFinal

    def dechiffrer(self, mot):
        """Permet de déchiffrer du texte sous le format Azerty

        Args:
            mot ([String]): Mot à déchiffrer

        Returns:
            [String]: Mot déchiffré
        """

        mot.lower()

        motFinal = ""
        for lettre in mot:
            motFinal += clavier[clavier2.index(lettre)]
        return motFinal