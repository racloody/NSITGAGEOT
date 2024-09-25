
#Écrire une fonction qui prend une liste A de taille n et renvoie la liste des permutations de A.
def permutation(a):
    length = len(a)
    for i in range(length):
        for j in range(i+1,length):
            a[i],a[j] = a[j],a[i]
            yield a
            a[i],a[j] = a[j],a[i]