class Boite:
    """
    Attributs et methodes de boites,
    
    """

    def __init__(self, largeur, hauteur, longueur):

        if isinstance(largeur, int) and isinstance(hauteur, int) and isinstance(longueur, int):
            self.largeur = largeur
            self.hauteur = hauteur
            self.longueur = longueur

    
    def volume(self):
        return self.largeur * self.hauteur * self.longueur
    
    def rentre_dans(self, bt2):
        return self.longueur <= bt2.longueur and self.hauteur <= bt2.hauteur and self.largeur <= bt2.largeur
boite1 = Boite(3, 2, 1)
boite2 = Boite(6, 6, 6)
print (boite1.rentre_dans(boite2))
print(boite1.volume())