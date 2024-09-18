import random as rd
from time import sleep 
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
    
    def setPv(self,degats):
        self._pv -= degats
    


    def setDegats(self,new_degats):
        if isinstance(new_degats,int) and new_degats>=0:
            self._degats=new_degats
    
    def __str__(self):
        return "Il reste {} PV à {}.".format(self.getPv(),self.getNom())

    def attaque(self,adversaire):
        degats=rd.randint(0,self._degats)
        adversaire.setPv(+degats)
        print("{} attaque {} et lui inflige {} points de dommages.".format(self.getNom(),adversaire.getNom(),degats))

nolan=Personnage("Nolan",80,10)
paul=Personnage("Paul",80,10)

tour = 0
jeu = True
while jeu :

    if tour == 0:
        print("C'est au tour de {} qui a {} PV.".format(nolan.getNom(), nolan.getPv()))
        tour = 1
        nolan.attaque(paul)
        sleep(1)
        if paul.getPv()<=0:
            jeu = False
            print ("Le gagnant est {}.".format(nolan.getNom()))

    else:
        print("C'est au tour de {} qui a {} PV. ".format(paul.getNom(), paul.getPv()))
        tour = 0
        paul.attaque(nolan)
        sleep(1)
        if nolan.getPv()<=0:
            jeu = False
            print ("Le gagnant est {}.".format(paul.getNom()))
        