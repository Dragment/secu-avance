
import string
import itertools
import hashlib

outfile = open("UCLC_4_SHA512.txt","w")

def process():
    alphabet_LC = list(string.ascii_lowercase)
    alphabet_UC = list(string.ascii_uppercase)
    possibilities_tuple = list(itertools.combinations(alphabet_LC + alphabet_UC, r=4))

    for t in possibilities_tuple: #Pour chaque tuple dans la liste
        current_string = ''.join(t) # on la convertis en string
        current_string_hashed = hashlib.sha512(str(current_string).encode("utf-8") ).hexdigest() # on la passe en sha512
        outfile.write(current_string_hashed+"\n")



process()