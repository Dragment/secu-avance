# -*- coding: utf-8 -*-

import os

def cesar(string_to_encode, cipher_shift):
    letters = "abcdefghijklmnopqrstuvwxyz"
    string_to_encode = string_to_encode.lower()
    cipher_shift = int(cipher_shift)
    string_encrypted = ""
    for character in string_to_encode:
        position = letters.find(character)
        new_position = (position + cipher_shift) % 26
        if character in letters:
            string_encrypted = string_encrypted + letters[new_position]
        else:
            string_encrypted = string_encrypted + character
    return string_encrypted
    

#Définir chemin dossier
path = "C:/Users/CE PC/Desktop/cour/M1/sécurité avancé/tp1/dossier a crypter"
os.chdir(path)
#print("Current working directory: {0}".format(os.getcwd()))

#Récupérer liste des fichiers
fileList = os.listdir(path)

#Pour chaque fichier
for file in fileList:
    
    # Ouvrir le fichier et récupérer le contenu
    f = open(file, 'r')
    data = f.read()
    f.close()
    #Crypter les datas
    newDatas = cesar(data, 13) #Avec un décalage de 13 si on lance une seconde fois ça décrypte
    # Remplacer le contenu du fichier
    fw = open(file, 'w')
    fw.write(str(newDatas))
    fw.close()