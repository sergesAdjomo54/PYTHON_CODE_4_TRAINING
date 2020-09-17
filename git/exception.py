a = 5
b = 0

try:
    print(a/b)

except Exception as e:  # la variable {e} nous permet d'afficher l'erreur exacte qui a été levée.
    print("Impossible la divions d'un nombre par zero.", e)

finally:
    print("close ressources")  # ce bloc s'execute qu'il y ai erreur ou pas