"""Programme qui calcule une puissance choisie par l'utilisateur sur un nombre également choisi par ce dernier."""
n = int(input("Definir un nombre n : ")) #L'utilisateur choisit un nombre n
a = int(input("Définir sa puissance a : ")) #L'utilisateur choisit la puissance a

#La fonction calcule la puissance a du nombre n
def puissance (a,n):
    if isinstance (n, int): #On verifie que n est entier
        if n == 0:
            return 1 # Si n = 0 On retourne 1
        elif a == 0 :
            print("undefined")
        else :
            return a*puissance(a, n-1) #Sinon on calcule la puissance
print(puissance(a,n)) #On affiche la puissance
