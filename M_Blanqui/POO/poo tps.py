"""Programme qui calcule une opération entre deux heures différentes (opération et soustraction)"""
class temps():
    def __init__(self,h,m,s):
        self.heure = h #Heure
        self.minute = m #Minute
        self.seconde = s #Seconde

    def __str__(self):
        return "{}:{}:{}".format(self.heure,self.minute,self.seconde) #Affiche l'heure sous la forme HH:MM:SS

    def __add__(self,tps2): #Modifie l'opérateur + pour l'addition de deux temps
        sec_fin = (self.seconde + tps2.seconde) % 60
        min_fin = (self.minute + tps2.minute + (self.seconde + tps2.seconde)//60) % 60
        hr_fin = (self.heure + tps2.heure + (self.minute + tps2.minute)//60)
        temps_fin = temps(hr_fin,min_fin,sec_fin)
        return temps_fin
    
    def __sub__(self,tps2): #Modifie l'opérateur - pour la soustraction de deux temps
        if tps2.heure <= self.heure:
            if tps2.seconde > self.seconde or tps2.minute > self.minute:
                if tps2.seconde > self.seconde :
                    self.minute += -1
                    self.seconde += 60
                    if self.minute < tps2.minute:
                        self.heure+= -1
                        self.minute += 60

                    hr_fin = self.heure - tps2.heure
                    min_fin = self.minute - tps2.minute
                    sec_fin = self.seconde - tps2.seconde
                    temps_fin = temps(hr_fin,min_fin,sec_fin)
                    return temps_fin
            
                elif tps2.minute > self.minute:
                    self.heure += -1
                    self.minute += 60
                    hr_fin = self.heure - tps2.heure
                    min_fin = self.minute - tps2.minute
                    sec_fin = self.seconde - tps2.seconde
                    temps_fin = temps(hr_fin,min_fin,sec_fin)
                    return temps_fin
            else:
                hr_fin = self.heure - tps2.heure
                min_fin = self.minute - tps2.minute
                sec_fin = self.seconde - tps2.seconde
                temps_fin = temps(hr_fin,min_fin,sec_fin)
                return temps_fin   
        else:
            return "improssible à déterminer, entrez une heure inferieure à la première" #Envoie un message d'erreur si la soustraction est impossible

heure_1 = input("Entrez une heure 1 sous la forme HH:MM:SS : ") #Demande à l'utilisateur d'entrer une heure
hours1 , minutes1 , seconds1 = heure_1.split(':') #Sépare l'entrée utilisateur grâce au caractère ":", il les répartit en 3 variables hours1,minutes1 et seconds1
heure_2 = input("Entrez une heure 2 sous la forme HH:MM:SS : ") #Demande à l'utilisateur d'entrer une deuxième heure
hours2 , minutes2 , seconds2 = heure_2.split(':') #Sépare l'entrée utilisateur grâce au caractère ":", il les répartit en 3 variables hours2,minutes2 et seconds2

hours1 , minutes1 , seconds1, hours2 , minutes2 , seconds2 = int(hours1) , int(minutes1) , int(seconds1) , int(hours2) , int(minutes2) , int(seconds2) #convertit les strings en int gr^ca à l'assignation multiple

#associe les variables demandées à l'utilisateur sur les attributs de la classe
temps1=temps(hours1,minutes1,seconds1)
temps2=temps(hours2,minutes2,seconds2)
#Laisser l'utilisateur choisir entre l'addition et la soustraction
opé=input("Choisissez une opération (+/-) : ")
#Afficher le resultat selon l'opération choisie
if opé == "-": 
    print(f"Le résultat est {temps1-temps2}")
else:
    print(f"Le résultat est {temps1+temps2}")