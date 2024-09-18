"""Soit (Sn) la suite définie pour tout entier non nul par Sn = 1+2+3+··· +n"""
#Calculer S1, S2, S3, S4 et S5.

def s_recur(n):
	assert n >= 1, "n must be positive"
	if n>1:
    	    return n + s_recur(n - 1)
	else:
    	    return 1


print(s_recur(5))

"""Preuves
S1 = 1 + 2 + 3 + 4 + 5 = 15
S2 = 1 + 2 + 3 + 4 + 5 + 6 = 21
S3 = 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
S4 = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36
S5 = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45

"""