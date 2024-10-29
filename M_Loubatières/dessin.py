# coding: utf-8

#
# Activité 1 du chapitre 1 (p10) : Un peu de géométrie
# Fichier destiné aux élèves
#

from turtle import goto, penup, pendown, pencolor, speed, hideturtle, done

# pour aller vite et masquer la tortue
speed(0)
hideturtle()

# taille de la croix
TRAIT = 10

def croix(x, y, couleur='black'):
    """ Dessiner une croix aux coordonnées x, y, de la couleur donnée """
    pencolor(couleur)
    penup()
    goto(x-TRAIT, y)
    pendown()
    goto(x+TRAIT, y)

    penup()
    goto(x, y-TRAIT)
    pendown()
    goto(x, y+TRAIT)

def trait(x1, y1, x2, y2, couleur='black'):
    """ Dessiner un segment aux coordonnées données, de la couleur donnée """
    pencolor(couleur)
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)

