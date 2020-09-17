"""Ecrire un scrip longueurChaine.py qui demande de saisir deux chaines de caractère et qui affiche la plus grande des
deux chaines"""

ch1 = input("Entrer la chaine 1: ")
ch2 = input("Entrer le chaine 2: ")

if len(ch1) > len(ch2):
    print(ch1)
elif len(ch1) == len(ch2):
    print("Les deux chaines sont égales.")
else:
    print(ch2)

