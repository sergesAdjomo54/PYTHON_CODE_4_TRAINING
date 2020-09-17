def energie_potentielle(masse, hauteur, g, energie_limite):
    E = masse * hauteur * g
    return E > energie_limite


print(energie_potentielle(80,15,5,100))



