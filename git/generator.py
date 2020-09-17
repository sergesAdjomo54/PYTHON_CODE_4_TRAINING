def topten():
    yield 5


def topseven():
    return 5


# val1 nous retourne 5 normalement
val1 = topseven()
print(val1)

# val nous retourne bien 5 mais en {generator}
val = topten()
print(val)

# pour afficher le nombre 5 il faut utiliser soit un iterator {__next()__} soit la boucle for qui l'utilise
# implicitement la boucle for utilise le {__next()__} iterator de manière implicite

print(val.__next__())
