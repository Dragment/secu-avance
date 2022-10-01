# -*- coding: utf-8 -*-

from hashlib import sha256

def genererChaine4():
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    listMdp = []
    for a in alpha:
        for b in alpha:
            for c in alpha:
                for d in alpha:
                    listMdp += [a+b+c+d]
    return listMdp

def hasherList(listMdp):
    listHash = []
    for mdp in listMdp:
        listHash += [sha256(mdp.encode('utf-8')).hexdigest()]
    return listHash

file = open("testpython.txt", "w") 
mdps = hasherList(genererChaine4())
for w in mdps:
    file.write(w)
    file.write("\n")
file.close()