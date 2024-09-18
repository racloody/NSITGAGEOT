#a. Définir une classe Personne avec pour attributs le nom et le prénom de la personne.b. .c.  Définir une classe Groupe avec deux attributs, une liste de personnes et une liste d’amis, et deux méthodes, l’une pour ajouter une personne et l’autre pour déclarer deux personnes amies. On s’assurera que les deux personnes amies font bien partie du groupe.d.  Ajouter une méthode qui permet de lister les amis d’une personne.9     On considère le programme suivant :1class Chat:   def bonjour(self):       print('miaou')class Chien:   def bonjour(self):       print('ouaf')c = Chat()c.bonjour()c = Chien()c.bonjour()1a.  Qu’affiche le programme ? Comment expliquer ce résultat ?b.  Donner un autre exemple qui exploite cette propriété.10   a. Écrire et tester les définitions complètes des classes Point et Segment du cours.La classe Turtle de la bibliothèque Python turtle contient la méthode goto(x, y) qui déplace la tortue à la position donnée et les méthodes penup() et pendown() pour lever et baisser le crayon.b.  Utiliser ces méthodes pour implémenter une classe Dessin avec deux méthodes, croix pour tracer une croix à une position donnée, et trait pour tracer un trait entre deux points.c.  Ajouter une méthode dessiner aux classes Point et Segment du cours pour afficher le point par une croix et le segment par un trait.d.  Écrire un programme qui crée des points et des segments à des positions aléatoires (en utilisant la fonc-tion randint(min, max) de la bibliothèque Python random) et les affiche.1   a. Implémenter le type abstrait Point de trois façons """
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return "{} {}".format(self.nom, self.prenom)
# Définir une classe Amis avec pour attributs deux personnes et une méthode ami qui prend une personne p en paramètre et retourne l’autre personne si p est l’un des deux amis, ou None sinon
class Amis(Personne):
    def __init__(self, nom, prenom, ami):
        super().__init__(nom, prenom)
        self.ami = ami 

    def __str__(self):
        return "{} {} ami {}".format(self.nom, self.prenom, self.ami)

    def ami(self, p):
        if p == self.ami:
            return self.ami 
        else:
            return None
class Groupe:
    def __init__(self, liste_personnes, liste_amis):
        self.liste_personnes = liste_personnes
        self.liste_amis = liste_amis

    def __str__(self):
        return "{} {}".format(self.liste_personnes, self.liste_amis)

    def ajouter_personne(self, p):
        self.liste_personnes.append(p)

    def ajouter_amis(self, p1, p2):
        self.liste_amis.append(Amis(p1.nom, p1.prenom, p2))

    def lister_amis(self, p):
        for i in self.liste_amis:
            if i.ami(p) != None:
                print(i)

#executez le programme

    