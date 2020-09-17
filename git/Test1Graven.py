
def energie_potentielle(masse, hauteur, g, energie_limite):
    E = masse * hauteur * g
    if(energie_limite < E):
       return "Energie limite inférieur a E"
    elif(energie_limite > E):
        return "\nEnergie limite égal à E."
    else:
        return "\nEnergie limite supérieure à E"
    print()
    print("L'énergie potentielle est: " + str(E))
    print("L'énergie limite est: " + str(energie_limite))


    resultat = energie_potentielle(10, 5, 8.28,100)
    print(resultat)