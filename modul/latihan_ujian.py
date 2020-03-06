def movezero(list):
    nlist = []
    zero = 1
    for i in list:
        if i != 0 or type(i) == type(False):
            nlist.append(i)
        else:
            zero += 1
    for i in range(zero):
        nlist.append(0)
    return nlist

    print(movezero(False,1,1,1,23,0,'a',0,'b'))

######################################################

def spinword(string):
    word = []
    for i in string.split():
        if len(i) >= 5:
            word.append(i[::-1])
        else:
            word.append(i)
    # return ' '.join(word) # CARA CEPET PAKE JOIN
    z = ''
    for idx, val in enumerate(word):
        if idx == len(word)-1:
            z += val
        else:
            z += val
            z += ' '
    return z
print(spinword(hey everyone warriors))