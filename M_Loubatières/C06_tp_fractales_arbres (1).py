# coding: utf-8
#
# Chapitre 6 - TP 2 - Dessiner des fractales (page 129)
#

from math import cos, sin, radians
from matplotlib.colors import rgb2hex
from dessin import Dessin, Trait, Arc, main_loop


# constantes
TAILLE = 800  # taille de la surface de dessin
# la surface de dessin, avec un fond blanc
dessin_arbre = Dessin("white", TAILLE, TAILLE)


def ytree(
    n,
    x,
    y,
    orientation_arbre,
    longueur,
    ecart_angulaire_fils=radians(22.5),
    ratio_longueur=0.8,
    n_max=None,
):



    if n >= 0:
        if n_max == None:
            n_max = n
        x1 = x + cos(orientation_arbre) * longueur
        y1 = y + sin(orientation_arbre) * longueur
        couleur = rgb2hex((0.0, 1.0, 0.0))
        if n_max >= 1:
            couleur = rgb2hex((0.0, float(n_max - n) / (n_max), 0.0))
        Trait(dessin_arbre, x, y, x1, y1, couleur)

        ytree(n - 1, x1, y1, orientation_arbre, longueur * ratio_longueur,
              ecart_angulaire_fils, ratio_longueur, n_max)

        ytree(n - 1, x1, y1, orientation_arbre + ecart_angulaire_fils, longueur * ratio_longueur,
              ecart_angulaire_fils, ratio_longueur, n_max)

        ytree(n - 1, x1, y1, orientation_arbre - ecart_angulaire_fils, longueur * ratio_longueur,
              ecart_angulaire_fils, ratio_longueur, n_max)

def dessiner_arbre_binaire_arc(n, x, y, w):
    if n > 0:
        Arc(dessin_arbre, x - w / 2, y, x + w / 2, y + w, 0, 180)
        dessiner_arbre_binaire_arc(n - 1, x - w / 2, y + w, w / 2)
        dessiner_arbre_binaire_arc(n - 1, x + w / 2, y + w, w / 2)


def dessiner_arbre_binaire_trait(n, x, y, w, h):
    if n > 0:
        Trait(dessin_arbre, x, y, x - w / 2, y + h)
        Trait(dessin_arbre, x, y, x + w / 2, y + h)
        dessiner_arbre_binaire_trait(n - 1, x - w / 2, y + h, w / 2, h)
        dessiner_arbre_binaire_trait(n - 1, x + w / 2, y + h, w / 2, h)


# Test :
ytree(10, 100, 200, 0, 50, radians(22.5), .8)
dessiner_arbre_binaire_arc(5, 600, 20, 160)
dessiner_arbre_binaire_trait(5, 600, 400, 160, 40)

main_loop()
