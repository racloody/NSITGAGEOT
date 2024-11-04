from pile import Pile
def multi(a,n):
    """ a est un float, n un entier>0n renvoir n*a sans utiliser la touche *"""
    if n == 1:
        return a
    else:
        return a+multi(a,n-1)   

print(multi(6,2))

def sommePositifs(L):
    """renvoie la somme des nombres strictements positifs de la liste L."""
    if len (L) == 0:
        return 0
    a = L.pop()
    if a > 0:
        return a + sommePositifs(L)
    else:
        return sommePositifs(L)

print(sommePositifs([-1,1,-2,3,-4,5,-3]))

def positifs(L):
    """
    Renvoie la liste des nombres positifs de la liste L en conservant l’ordre.
    """
    if not L:
        return []
    elif L[0] > 0:
        return [L[0]] + positifs(L[1:])
    else:
        return positifs(L[1:])

print(positifs([-1,1,-2,12,-4,5,-3]))

def nb_chemins(nb_marches):
    """Retourne le nombre de façons de monter un escalier en montant
    d'une ou deux marches à chaque pas."""
    assert nb_marches > 0, 'nb_marches > 0 !!'

    if nb_marches == 1:
        return 1
    elif nb_marches == 2:
        return 2
    else:
        return nb_chemins(nb_marches - 1) + nb_chemins(nb_marches - 2)
    
print(nb_chemins(4))

def chemins(n):
    """
    Retourne la liste des chemins pour monter un escalier en montant d'une ou deux marches à chaque fois.
    """
    if n == 0:
        return [[]]
    elif n == 1:
        return [[1]]
    else:
        chemins_1 = chemins(n - 1)
        chemins_2 = chemins(n - 2)
        
        chemins_n = []
        for chemin in chemins_1:
            chemins_n.append(chemin + [1])
        for chemin in chemins_2:
            chemins_n.append(chemin + [2])
        
        return chemins_n
print(chemins(1))
print(chemins(2))

def permut(liste):
    """
    Retourne la liste des permutations de la liste.
    """
    if len(liste) == 1:
        return [liste]
    else:
        L2 = []
        for i in range(len(liste)):
            for perm in permut(liste[:i] + liste[i+1:]):
                L2.append(perm + [liste[i]])
        return L2
print(permut(['a','b']))
print(permut(['a','b','c']))

def expo_rapide(x,n):
    """calcule x**n: x(float), n(int)"""
    if n == 0:  
        return 1
    else:
        return x*expo_rapide(x,n-1)

print(expo_rapide(2,3))

def addition(p):
    """
    Remplace les deux nombres du sommet de la pile p par leur somme.
    """
    if p.est_vide():
        return
    a = p.depiler()
    if p.est_vide():
        p.empiler(a)  
        return
    b = p.depiler()
    p.empiler(a + b)


p = Pile()
p.empiler(3)
p.empiler(7)
addition(p)
print(p.elements) 




p=Pile() 


p.empiler(p,3)
p.empiler(p,5)
addition(p)          
p.empiler(p,7)
multiplication(p)  
