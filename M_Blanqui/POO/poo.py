class Personnage:
    """
    Personnage d'un jeu de type hack 'n slash
    Attributs :
        nom : chaine de caratères, nom du personnage
        pv : entier positif ou nul, points de vie du personnage
        degats : entier strictement positif, dégats maximum du personnage
        position : couple d'entiers donnant l'abscisse et l'ordonnée du   
        personnage sur la carte
    Méthodes:
        init() constructeur de la classe Personnage Uniquement pour les  
        attributs _pv et _position
        deplacement(paramètres) : permet de changer la position du personnage
        attaque() : renvoie les dégâts faits à l'adversaire
    """

    def __init__(self,nom_perso,points_vie,val_degats,position_depart=(0,0)):
        self._nom=nom_perso
        self._pv=points_vie
        self._degats=val_degats
        self._position=position_depart

    def getNom(self):
        return self._nom
    
    def getPv(self):
        return self._pv
    
    def getDegats(self):
        return self._degats
    
    def getPosition(self):
        return self._position
    
    def setPv(self,new_pv):
        self._pv=new_pv
    
    def setPosition(self,(x,y)):
        self._position=(x,y)

    def setDegats(self,new_degats):
        if isinstance(new_degats,int) and new_degats>=0:
            self._degats=new_degats
        
    
    

        