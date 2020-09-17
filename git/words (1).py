#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy

help(numpy)

# In[5]:


s = """ this is 
a multiline
String"""

print(s)

# In[7]:


help(str)

# In[23]:


from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    # ici line.decode transforme le type byte en type list le split() a chaque espace il fait un append du mot suivant
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)

story.close()
print(type(story_words))
print()
print(story_words)

# In[30]:


from urllib.request import urlopen


def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        # ici line.decode transforme le type byte en type list le split() a chaque espace il fait un append du mot suivant
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    for word in story_words:
        print(word)


if __name__ == '__main__':
    fetch_words()

# In[40]:


from urllib.request import urlopen


def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        # ici line.decode transforme le type byte en type list le split() a chaque espace il fait un append du mot suivant
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main():
    words = fetch_words()
    print_items(words)


if __name__ == '__print_items__':
    print_items(fetch_words())
else:
    main()

# In[14]:


import sys
from urllib.request import urlopen


def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        # ici line.decode transforme le type byte en type list le split() a chaque espace il fait un append du mot
        # suivant
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__print_items__':
    print_items(fetch_words())
else:
    main('http://sixty-north.com/c/t.txt')
    # main(sys.argv[1]) ici il faut entrer l'url lors de l'execussion

# # MODULE 6 PLURALSIGHT

# In[13]:


a = 457
print("id de a sur le disque: ", id(a))
b = 4657
print("id de b sur le disque: ", id(b))
a = b
print("nouvel id de a: ", id(a))
b = a

print('nouvel id de b: ', id(b))
print()

c = id(b) == id(a)
print(c)
print(type(c))
c = a is b
print(c)
print(type(c))

s = [4, 8, 9, 11]
r = s  # ici on modifie R et ça affecte S
r[1] = 17
print(s)


# In[18]:


# demonstration du passage par argument
def fonct(f):
    return f


a = [10, 5, 85]

c = fonct(a)

c is a
# demonstration du passage par argument
a = 457
print("id de a sur le disque: ", id(a))
b = 4657
print("id de b sur le disque: ", id(b))
a = b
print("nouvel id de a: ", id(a))
b = a

print('nouvel id de b: ', id(b))
print()

c = id(b) == id(a)
print(c)
print(type(c))
c = a is b
print(c)
print(type(c))


# In[26]:


def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


c = banner(border='#', message="LOIC SALO, tu n'es rien mouf")

# In[34]:


import time

time.ctime()


def show_actual_time(arg=time.ctime()):
    print(arg)


# ici on constate que le time ne change pas car il sagit du passage par adresse
show_actual_time()


# In[38]:


# Demonstration du systeme de type dynamique
def add(a, b):
    return a + b


print(add(5, 7))
print()
print(add(3.1, 7.9))
print()
print(add([1, 7], [10, 1.9]))
print()
print(add("string1", " string2"))


# In[41]:


# Mutable default value

def add_spam(menu=[]):
    menu.append("Spam")
    return menu


breakfast = ['poulet', 'frites']
print(add_spam(breakfast))

lunch = ['baked beans']
print(add_spam(lunch))

add_spam()  # ici spam se repète
add_spam()


# In[50]:


def add_spam(menu=None):  # ici spam ne se repète pas
    if menu is None:
        menu = []

    menu.append("Spam")
    return menu


add_spam()
add_spam()

# In[52]:


count = 0


def show_count():
    print(count)


def set_count(c):
    count = c


show_count()
set_count(5)
show_count()

print()


def set_count(c):
    global count  # le mot clé global nous permet de rendre une variable locale en variable globale
    count = c


show_count()
set_count(5)
show_count()

#
# # MODULE 7 

# In[71]:


a = (354)

b = (354,)
print(type(a), type(b))

t = 1, 3, 54, 8, 11, 20
print(type(t))


def minmax(items):
    return min(items), max(items)


print(minmax(t))
print(type(minmax(t)))

a, b = minmax(t)

print(a, b)

a = 'Adjomo'
b = 'serges'
a, b = b, a  # changement par valeur effectuer en une ligne
print("\n")
u = "Serges Adjomo"
tuple(u)  # convertir une chaine de caratère en tuple
for i in u:
    print(i)

c = 54 in t
r = 100 not in t
print(c)
print(r)

# In[91]:


couleur = ';'.join(['rouge', 'vert', 'jaune', 'noir'])
print(couleur)
print(couleur.split(';'))
print(''.join(couleur.split(';')))

chaine = ['mange', 'boie', 'dors', 'chie']
print(chaine)
c = ''.join(chaine)
print(c)
print()
c = ''.join(chaine).partition('boie')  # {partition} sépare la chaine de gauche et droite
print(c)

départ, separator, arrivée = "Douala:Yaounde".partition(':')  # {separator} indique le moment de separation de paquet
print(départ, arrivée)

départ, _, arrivée = "Douala:Yaounde".partition(':')  # {separator} est remplacer par {underscore '_'}
print(départ, arrivée)

# In[102]:


a = "The age of {0} is {1}.".format('ango', 27)
print(a)
a = "The age of {} is {}.".format('ango', 27)
print(a)
a = "The Galactic position x={posi[0]}, y={posi[1]}, z={posi[2]}".format(posi=(65.2, 25.4, 45.2))
print(a)
import math

a = "Math constants: pi={m.pi:.3f}, e={m.e:.3f}.".format(m=math)
print(a)
val = 4 * 30
a = "The value is {value}".format(value=val)
print(a)

a = f'la valeur est: {val}'
print(a)
import datetime

a = f'Le temps actuel est :  {datetime.datetime.now().isoformat()}.'
print(a)

# In[110]:


# La fonction {range}
a = range(5)
print(a)

for i in range(2):
    print(i)

a = list(range(4, 14, 2))  # Le 3e chiffre 2 réprésente le pas
print(a)
a = range(5, 10)  # Ici l'interval est le suivant   [5, 10[
print(a)
print(list(a))

# In[122]:


# La fonction {enumerate}
t = [6, 372, 8860, 14880, 2096886]
for i in enumerate(t):  # Enumerate converti la liste [t] en {tuple}
    print(i)

for i, v in enumerate(t):
    print(f'i ={i}, v={v}')

# In[184]:


#####################################
# LES LIST
#####################################
a = [[1, 2], [3, 4]]
b = a[:]
print(a is b)  # passage par adresse ici l'adresse de b n'est pas l'adresse de a
print(a == b)
print(a[0] is b[0])  # passage par valeur: les valeurs de a sont les valeurs de b
a[1].append(5)
print(a)
print(b)

w = "the quick brown fox jumps over the lae dog".split()
i = w.index('fox')
print(i)
print(w[i])
# w.index('jjllkj') ceci nous rapporte une erreure car il n"est pas présent
print("le mot \'the\' apparait {} fois".format(w.count("the")))
print(2 in a[0])
print(45 not in a[1])

# LE MOT CLE {del}, {remove}, {extend} et {insert}
a = w
print(a)
del a[3]
print(a)
a.remove('dog')
print(a)
b = 'quick'
print(b in a)
del a[a.index('quick')]
print(b in a)
print(a)
a.insert(a.index('brown'), "quick")
print("insert inserer un valeur\n", a)
# Lorsqu'on veut remove ou del un élément qui n'est pas dans la liste on a une erreure
print()
print(a)
print(' '.join(a))
b = [15, 19, 25]
n = [14, 20, 111]
k = b + n
print()
print("concatener deux listes\n", k)
k.extend([120, 555, 888])
print("Extend ajoute un liste a la liste k\n", k)
# La fonction {reverse} et {sort()}

k.reverse()
print("Inverser la liste: \n", k)
k.sort()
print("Ordre croissant\n", k)
k.sort(reverse=True)
print("odre décroissant\n", k)

# In[198]:


a = [12, 45, 0, 12]
b = a[:]
print(b)
print(b is a)
print(b == a)
a.append(777)  # pourquoi cette ligne ne modifie pas la liste b?
print(f'a = {a} et b = {b}')
#################################
a = [[12, 5], [4, 2]]
b = a[:]
print(b is a)
print(b == a)
a[1].append(777)  # Pouquoi cette ligne modifie aussi la liste b?
print(f'a = {a} et b = {b}')
# Qelle différence entre {a == b} et {a is b}


# In[230]:


#####################################
# LES DICTIONNAIRES
#####################################
nom_et_ages = [('Alice', 32), ('Bob', 48), ('charlie', 28), ('Daniel', 33)]
d = dict(nom_et_ages)
print("d\n", d)
phonetic = dict(a='alpha', b='bravo', c='charlie', d='delta')
print("phonetic\n", phonetic)
e = d.copy()
print("e\n", e)
print()
# Le mot clé {update}peu ajouter un élément,modifier,ajouter un autre dict
u = d.update(phonetic)
stock = {'GOOG': 884, 'AAPL': 416, 'IBM': 194}
print('Stock\n', stock)
stock.update({'GOOG': 8845, 'YHOO': 25})
print('stock update\n', stock)

# In[265]:


# Utilisation de la boucle for sur le dict

cap = dict(kmer='yde',
           france='paris',
           congo='brazza'
           )
type(cap)
print(cap)
for key in cap:
    print(f'cle {key} : valeur {cap[key]}')

print()
cap1 = {'kmer': 'yde',
        'france': 'paris',
        'congo': 'brazza'
        }
print("---------les valeurs----------")
for value in cap1.values():
    print(value)
print("---------les clefs-------")
for key in cap1.keys():
    print(key)

# La méthode {items()} de dict
m = {'nom': 'Adjomo', 'prenom': 'serges', 'proffession': 'artiste'}
print('----------------------------')
for key, value in m.items():
    print(f'{key} = {value}')

print('nom' in m)
print('Adjomo' in m)
print('Adjomo' not in m)
print('----------------del------------')
del m['nom']
print(m)
print('--------modifier une valeur-----------')
m['prenom'] += ' thibaut'
print(m)
print('--------ajouter une clef et sa valeur-----------')
m['nom'] = 'Adjomo'
print(m)
# La fonction {pprint} de la bibliothèque {pprint}

print('--------classer par ordre alphabétique-----------')
from pprint import pprint

a = {'1': 'a',
     'a': '1',
     '5': 'j',
     '11': 'e'
     }

print(a)
print()
pprint(a)  # cette fonction classe par ordre alphabétique les valeurs et non les clefs

# In[289]:


#####################################
# LES SET
#####################################

p = {6, 25, 496, 57687}
print(p)
print(type(p))
d = {}
print(type(d))
e = ()
print(type(e))
r = set()
print(type(r))
s = set([4, 15, 857, 777, 6555, 6555])  # le set supprime les doublons dans le cas où il y en a
print(s)
print('-------utilisation dans la boucle for: set est itterable------')
for i in s:
    print(i)

print('-----utilistion du in et not in-----')
print(4 in s)
print(20 not in s)
print('------la méthode add-------')
s.add(20)  # LES ELEMENT SONT TOUJOURS CLASSES EN DESORDRE
print(s)
print('---------la méthode update et remove sur les set------------')
s.update([17, 0, 8, 1])
print(s)
s.remove(0)
print(s)
print('------discard---------')
# {discard} supprime un élément sans retourner d'erreur s'il n'est pas présent contrairement a {remove}
s.discard(100)
print(s)
s.discard(777)
print(s)
print('---la méthode copy----')
p = {6, 25, 496, 57687}
a = {1, 2, 3, 4, 5, 6}
e = {range(5, 15)}
print(type(e))
print(p)
print(e)
p = a.copy()
print('---la copy de a dans p----------')  # la copie écrase tous les éléments présent dans p
print(p)

# In[301]:


#######################################################
# ALGEBRE AVEC LA COLLECTION SET
#######################################################
yeux_bleu = {'olivia', 'harry', 'lilly', 'jack', 'amelia'}
cheveux_blond = {'harry', 'jack', 'amelia', 'mia', 'joshua'}
malade_corona = {'harry', 'amelia'}
porteur_saint = {'harry', 'lilly', 'amelia', 'lola'}
o_blood = {'mia', 'joshua', 'lilly', 'olivia'}
b_blood = {'amelia', 'jack'}
a_blood = {'harry'}
ab_blood = {'joshua', 'lola'}

# union
print('------trouver les gens aux cheveux blond ou les yeux bleu et/ou les deux---------')
# Elements qui sont unique ou les deux donc soit dans l'un soit dns l'autre ou les deux a la fois
print(yeux_bleu.union(cheveux_blond))
print('------Nous pouvons demontrer l\'union est commutative.---------------------')
print(yeux_bleu.union(cheveux_blond) == cheveux_blond.union(yeux_bleu))

# intersection
print('--------------Trouver tous les gens aux cheveux blond et yeux bleu: (intersection)-------------')
# les éléments du 1er ensemble qui sont dans le 2eme ensemble vice versa
print(yeux_bleu.intersection(cheveux_blond))
print('------Nous pouvons demontrer que l\'intersection est commutative.---------------------')
print(yeux_bleu.intersection(cheveux_blond) == cheveux_blond.intersection(yeux_bleu))

# difference
print('-------les cheveux blond sans les yeux bleu (difference)---------------')
# Les élément du 1er ensemble qui ne sont pas dans le 2eme
print(cheveux_blond.difference(yeux_bleu))
print('------Nous pouvons demontrer que la difference est non commutative.---------------------')
print(yeux_bleu.difference(cheveux_blond) == cheveux_blond.difference(yeux_bleu))

# symmetric_difference
print('-------cheveux blond ou yeux bleu mais pas les deux--------')
# Les élément exclusif du 1er ensemble ou du 2eme ensemble mais pas les deux
print(cheveux_blond.symmetric_difference(yeux_bleu))
print(
    '------Nous pouvons demontrer que la difference symetrique est commutative (symmetric_difference).---------------------')
print(yeux_bleu.symmetric_difference(cheveux_blond) == cheveux_blond.symmetric_difference(yeux_bleu))

# issubset
print('--------Tous ceux qui sont malades_corona on aussi les yeux bleux---------------')
# demontrer qu'un ensemble est un sous ensemble d'un autre ensemble
# Tous les élément du 2eme ensemble sont présent dans le 1er
print(malade_corona.issubset(cheveux_blond))

# issuperset
print('--------Tous les porteur saint sont malade_corona---------------')
# demontrer qu'un ensemble est un super ensemble d'un autre ensemble
# Tous les éléments du premier sont présent dans le deuxième
print(porteur_saint.issuperset(malade_corona))

# isdisjoint
# Les ensembles sont totalement différents
print('-----------les groupe sanguin A sont totalement différent du groupe sanguin B')
print(a_blood.isdisjoint(b_blood))

# In[303]:


a = {1, 5, 8}

type(a)
a[1]


# le set n'est pas indexable,count ou reverse


# # MODULE 8 LES EXCEPTIONS

# In[8]:


def convert(s):
    """converting a string to an interger. """
    try:
        number = ''
        tab = []
        for token in s:
            number += tab[token]
        x = int(number)
        print(f'Conversion succeeded! x = {x}')
    except (KeyError, TypeError):
        print(f'Conversion failed!')
        x = -1
    return x


from exceptional import convert

convert("nine")

# In[22]:


import sys


def sqrt(x):
    if x < 0:
        raise ValueError(  # ici on leve l'exception ave le mot clé raise
            "Impossible de calculer la racine carée"
            f" d\'un nombre négatif {x}")

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print('this is never printed')

    except ValueError as e:  # C'est ici qu'on capture l'erreur qu'il a lever
        print(e, file=sys.stderr)
        print("programme execution continues normally here.")


if __name__ == '__main__':
    main()

# In[15]:


from math import sqrt

sqrt(9)
