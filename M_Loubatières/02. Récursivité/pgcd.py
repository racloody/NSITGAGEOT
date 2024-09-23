"""Écrire en python une fonction récursive pgcd(a,b) renvoyant le plus grand diviseur commun de
deux nombres a et b.
Pour cela on utilisera le résultat mathématique suivant :"""

def pgcd(a, b):
    if a%b == 0:
        return b
    else :
        return pgcd(b, a%b)
    
print(pgcd(int(input("a : ")), int(input("b : "))))
    
    