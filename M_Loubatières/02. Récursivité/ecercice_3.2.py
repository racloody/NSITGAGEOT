"""Cette programme calcule la factorielle d'un nombre choisi par l'utilisateur"""
n = int(input("Definir un nombre n : ")) #L'utilisateur choisit un nombre n
fact = 1 #On initialise la variable fact avec 1

#La fonction calcule la factorielle du nombre n
def factorielle(n):
    if isinstance(n, int): #On verifie que n est entier
        if n == 0:
            return 1 #Si n = 0 On retourne 1
        else :
            return n*factorielle(n-1) #Sinon on calcule la factorielle

print(factorielle(n))
