from os import system, name
n=0
while n != "q":

    n = input("Definir un nombre n (q pour quitter) : ") #L'utilisateur choisit un nombre n
    fact = 1 #On initialise la variable fact avec 1
    os.system('cls')
    #La fonction calcule la factorielle du nombre n
    def factorielle(n):

        if n == "q":
            return "See you soon"
        else :
            if int(n)==0:
                return 1 #Si n = 0 On retourne 1
            else :
                return int(n)*factorielle(int(n)-1) #Sinon on calcule la factorielle
        
    

    print(factorielle(n))
