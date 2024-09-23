import random
class Domino:
    def __init__(self, gauche, droite):
        self.gauche = gauche
        self.droite = droite

    def get_gauche(self):
        return self.gauche
    def get_droite(self):
        return self.droite   
    def nbPoints(self):
        """ retourne la sommes des points présents sur les 2 cotés """
        return self.gauche + self.droite
        
    def estBlanc(self,iswitedroite,iwitegauche):
        """ teste si le domino posséde un blanc : 0 sur un des cotés """
        iswitedroite = False
        iwitegauche = False
        if self.droite == 0:
            iswitedroite = True
        if self.gauche == 0:
            iwitegauche = True
    
    def estdouble(self):
        """ teste si le domino est double : 2 sur l'un des cotés """
        if self.droite == self.gauche:
            return True
        else:
            return False
        
    def __str__(self):
        if self.gauche != self.droite:
            return f"-------------------\n|        |        |\n|   {self.gauche}    |    {self.droite}   |\n|        |        |\n-------------------"
        else:
            return f"|-------|\n|       |\n|   {self.droite}   |\n|       |\n|-------|\n|       |\n|   {self.gauche}   |\n|       |\n|-------|"
    
    def afficherDomino(self):
        print(self.gauche, self.droite)

dom1=Domino(0,1)
print(dom1)

class JeuDeDomino:
    """ Classe JeuDeDomino """
    
    def __creerJeu():
        """ Pour créer un jeu de 28 pieces toute différentes """
        jeu = []
        for i in range (7):
            for j in range (i+1):
                jeu.append(Domino(i,j))
        return jeu
    
    def __init__(self):
        """ Constructeur """
        pass
        
    def melanger(self):
        """ Mélange aléatoirement le jeu de dominos """
        pass
        
    def afficherJeu(self):
        """ Affiche toutes les pièces du jeu ou la pioche si il y eu distribution """
        pass
            
    def distribuer(self, nb_joueur):
        """ Extrait des dominos du jeu pour un joueur et retourne une liste de 6 ou 7 dominos """
        pass