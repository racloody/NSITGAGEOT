def deux_puissance(n):
    if n==0:
        return 1
    else:
        return 2*deux_puissance(n-1)