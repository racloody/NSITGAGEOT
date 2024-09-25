l = list
def permut(l):
    if len(l) == 1:
        yield l
    else:
        for i in range(len(l)):
            for j in permut(l[:i] + l[i+1:]):
                yield l[i:i+1] + j
                