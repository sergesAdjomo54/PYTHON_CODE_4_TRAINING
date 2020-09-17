"""Ecrire un progrmme qui affiche les tables de multiplication de 1 à 10"""

for i in range(1, 10):
    print()
    for j in range(1, 11):
        print("{} x {} = {}".format(i, j, (i * j)))


