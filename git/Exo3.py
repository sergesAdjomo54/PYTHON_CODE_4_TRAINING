"""Ecrire un programme qui a parti de la saisie d'un rayon et d'une hauteur calcul le volume d'un cone droit et
affiche le résultat NB: V = 1/3pirh préciser les types a l'entrer et a l'affichage"""
import math
r = float(input("Entrer le rayon: "))
h = float(input("Entrer la hauteur: "))

m = r*h

v = 1 / 3 * math.pi * m
print(v)