"""
Stwórz generator hasła:
Hasło musi zawierać co najmniej jedną cyfrę.
Hasło musi zawierać co najmniej jedną dużą literę.
Hasło musi zawierać co najmniej jedną małą literę.
Hasło musi zawierać co najmniej jeden znak specjalny.
Hasło musi mieć między 10 a 15 znaków.
Hasło nie może zawierać znaków "mylących", 1, I, O, 0.
"""

#1 SPOSÓB

import random
import string

password = []
a = 0 
lists = []

def random_digit(lists,a):
    while a < 3:
        lists.extend(str(random.randint(2, 9)))
        a += 1
    return lists

def random_small_letter(lists,a):
    signs = list(string.ascii_lowercase)
    length = len(signs)
    return while_loop(lists, a, length, signs)

def random_big_letter(lists,a):
    signs = list(string.ascii_uppercase)
    signs.remove("O")
    signs.remove("I")
    length = len(signs)
    return while_loop(lists, a, length, signs) 

def special_signs(lists,a):
    signs = list(string.punctuation)
    signs.remove("#")
    length = len(signs)
    return while_loop(lists, a, length, signs)

def while_loop(lists, a, length, signs):
    while a < 3:
        lists.extend(signs[random.randint(0, length-1)])
        a += 1
    lists=[]
    return lists

abbreviation = [random_digit(lists,a),random_small_letter(lists,a),random_big_letter(lists,a),special_signs(lists,a)]
length_abbreviation = len(abbreviation)
i = 0
while i < length_abbreviation:
    password.extend(abbreviation[i])
    i += 1

print("".join(password))

######################################

#2 SPOSÓB
import random
import string

lists = []
quantity = random.randint(10,15)
whole = 0
a=0
c=0
while whole < quantity:
    c+=1
    if c>=5:
        a=random.randint(1, 4)
    elif c<=4:
        a+=1
        
    if a == 1:
        lists.extend(str(random.randint(2, 9)))
        whole += 1

    elif a == 2:
        length=len(string.ascii_lowercase)
        x=random.randint(0, length-1)
        lists.extend(string.ascii_lowercase[x])
        whole += 1

    elif a == 3:
        capital_letter=list(string.ascii_uppercase)
        capital_letter.remove("O")
        capital_letter.remove("I")
        length=len(capital_letter)
        x=random.randint(0, length-1)
        lists.extend(capital_letter[x])
        whole += 1

    else:
        signs=string.punctuation
        length=len(signs)
        x=random.randint(0, length-1)
        lists.extend(signs[x])
        whole += 1

if whole == quantity:
    password = "".join(lists)
    print(password)
