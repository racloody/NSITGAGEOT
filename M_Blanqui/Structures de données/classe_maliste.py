     
class MaListe():
    def __init__(self):
        """
        initialise un objet correspondant à une liste Python vide
        """
        self.tete= None
        
    def isVide(self):
        """
        @Return : Booléen qui indique si la liste est vide
        """
        return self.tete is None
        
    def ajoute(self,x):
        """
        Ajpoute l'élément x en tête de liste'
        """
        self.tete=Cellule(x,self.tete)
        
    def __len__(self):
        """
        #return : Longueur de la liste
        
        """
        return longueur_rec(self.tete)
    
    def __getitem__(self,i):
        """
        @return : élément à la position i de la liste
        """
        return ieme_element_rec(i,self.tete)
    
    def __str__(self):
        """
        @return : affiche les éléments de la liste dans l'ordre'
        """
        return affiche_liste_rec(self.tete)
            

def longueur(lst):
    compteur=0
    cellule_courante=lst
    while cellule_courante is not None :
        compteur +=1
        cellule_courante=cellule_courante.suivante
    return compteur
 
def longueur_rec(lst):
    """renvoie la longueur de la liste lst
    Méthode récursive
    """
    if lst is None:
        return 0
    else:
        return 1 + longueur_rec(lst.suivante)   

def ieme_element(i,lst):
    """renvoie le n-ième élément de la liste lst
       les éléments sont numérotés à partir de 0
    """
    if lst is None:
        raise IndexError("indice invalide")
    cellule_courante=lst
    for a in range(i):
        if cellule_courante.suivante is None :
            raise IndexError("indice invalide")
        cellule_courante=cellule_courante.suivante
    return cellule_courante.valeur

def ieme_element_rec(i,lst):
    """renvoie le n-ième élément de la liste lst
       les éléments sont numérotés à partir de 0
    """
    if lst is None:
        raise IndexError("indice invalide")
    if i == 0:
        return lst.valeur
    else:
        return ieme_element_rec(i - 1, lst.suivante)

def affiche_liste(lst):
    if lst is None :
            return 'La Liste est vide'
    else :
        cellule_courante=lst
        affich=str(cellule_courante.valeur)
        while cellule_courante.suivante is not None:
            affich=affich+" , " + str(cellule_courante.suivante.valeur)
            cellule_courante=cellule_courante.suivante
        return affich

def affiche_liste_rec(lst):
    if lst is None:
        return ''
    if lst.suivante is None:
        return ''+str(lst.valeur)
    else:
        return ''+str(lst.valeur) + ', ' +affiche_liste_rec(lst.suivante)   