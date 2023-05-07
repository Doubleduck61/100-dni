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
