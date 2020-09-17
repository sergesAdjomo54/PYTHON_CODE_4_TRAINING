d = open('MyData', 'r')  ###################################
d1 = open('MyData', 'r')  # LECTURE DANS UN FICHIER TEXTE
d2 = open('MyData', 'r')  ###################################

print(d.read())  # lire dans un fichier

print("-----------------------------------")
print(d1.readline(), end="")  # ici on affiche une ligne et le {end=""} empeche d'aller a la ligne
print(d2.readline(5))  # on peut aussi preciser le nombre de caractere qu'on veut afficher

###################################
# ECRIRE DANS UN FICHIER TEXTE
###################################

f = open('MonSon', 'w')
# f.write("hello i'm ing odt")  # si je commente cette ligne la prochaine ligne va ecraser son contenu
# parce que au lieu d'utiliser {'w'} je devrais plutot utliser {'a'}
# qui signifie append
f.write("Overdose de punchline. fumer de l'herbe jusqu'a devenir comme picolo.")

f1 = open('MonSon', 'a')
f1.write("Ajoute moi a la suite\n")

# copie le contenu de {d} dans {f} .... contenu de Mydata dans Monson
d3 = open('MyData', 'r')
f2 = open('MonSon', 'a')
for data in d3:
    f2.write(data)

d.close()
d1.close()
d2.close()
d3.close()
f.close()
f1.close()
f2.close()



###########################################
# ECRITURE ET LECTURE DANS UN FICHIER IMAGE
###########################################

read_image = open('IMG_HS.JPG', 'rb') # on utilise {rb} pour << read binary >> lorsqu'il s'agit des fichier non texte

write_image = open('MyPic', 'wb')

for i in read_image:
    write_image.write(i)


read_image.close()
write_image.close()




