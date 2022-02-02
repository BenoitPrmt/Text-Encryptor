class ZigZag:

    def __init__(self) -> None:
        pass

    def chiffrer(self, mot):
        """Permet de chiffrer du texte sous le format ZigZag

        Format du ZigZag (Les X représentant les lettres):
        X---X---X---X---X---X
        -X-X-X-X-X-X-X-X-X-
        --X---X---X---X---X

        Args:
            mot ([String]): Mot à chiffrer

        Returns:
            [String]: Mot chiffré
        """

        ligne1 = mot[::4] # on prend un lettre sur 4
        ligne2 = mot[1::2] # on prend un lettre sur 2 mais pas la 1re
        ligne3 = mot[2::4] # on prend un lettre sur 4 a partir de la 3e

        return ligne1 + ligne2 + ligne3