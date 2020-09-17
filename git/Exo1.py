print("calcul de la somme de l\'inverse des carré des n premier entier naturel")
n = int(input("Entrer un nombre: "))
c = 0
for i in range(1, n):
    a = pow(i, -1)
    b = pow(a, 2)
    c = c + b


print(c)


