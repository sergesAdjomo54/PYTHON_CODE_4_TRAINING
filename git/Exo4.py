"""Construire la liste des 30 premier entier naturel positif non nul"""

La = []
i = 1


n = 2
while True:
    n = n + 1
    if n % i != 0:
        i = i + 1
    elif len(La) <= 30:
        La.append(i)

print(La)
