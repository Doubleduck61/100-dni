"""
Stwórz generator hasła:
Hasło musi zawierać co najmniej jedną cyfrę.
Hasło musi zawierać co najmniej jedną dużą literę.
Hasło musi zawierać co najmniej jedną małą literę.
Hasło musi zawierać co najmniej jeden znak specjalny.
Hasło musi mieć między 10 a 15 znaków.
Hasło nie może zawierać znaków "mylących", 1, I, O, 0.
"""
import random

lists=[ ]
#3 losowe cyfry
a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
#3 losowe małe litery
litery=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","w","x","y","z"]
dlugosc_litery = len(litery)
d1 = random.randint(0, dlugosc_litery-1)
e1 = random.randint(0, dlugosc_litery-1)
f1 = random.randint(0, dlugosc_litery-1)

d = litery[d1]
e = litery[e1]
f = litery[f1]

#3 losowe duże litery
g1 = random.randint(0, dlugosc_litery-1)
h1 = random.randint(0, dlugosc_litery-1)
i1 = random.randint(0, dlugosc_litery-1)
g2 = litery[g1]
g=g2.upper()
h2 = litery[h1]
h=h2.upper()
i2 = litery[i1]
i = i2.upper()

#Losowanie znaku
znak=["!","@","#","$","%","^","&","*","(",")","_","-","=","+","{","}",",",">","<","/","?"]
dlugosc_znak=len(znak)
j1 = random.randint(0, dlugosc_znak-1)
k1 = random.randint(0, dlugosc_znak-1)
l1 = random.randint(0, dlugosc_znak-1)
j = znak[j1]
k = znak[k1]
l = znak[l1]
a=str(a)
b=str(b)
c=str(c)
lists.extend(a)
lists.extend(d)
lists.extend(b)
lists.extend(k)
lists.extend(f)
lists.extend(g)
lists.extend(i)
lists.extend(c)
lists.extend(j)
lists.extend(h)
lists.extend(l)
lists.extend(e)
haslo="".join(lists)
print(haslo)
