
n = int(input("entrer un nombre: "))

fact = 1
i = 1
if n < 2:
    pass
else:
    while i <= n:
        fact = fact * i
        i += 1


print("factorial is: ", fact)