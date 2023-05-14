import random
import os

lists = []
a = 0

def drawing_numbers(a, lists):
    while a < 6:
        lists.append(random.randint(1,10))
        list(set(lists))
        a = len(set(lists))
        a += 1
    return "Numbers have been drawn!"
    
def sugestion():
    number=input("Guess one of the drawn numbers: ")
    if number.isdigit():
        number=int(number)
        guess(lists, number)
    else:
        print("You have to enter a number!")
        sugestion()
    return "Have a nice day!"
        
def guess(lists, number):
    a = 0
    while a < 5:
        if number == lists[a]:
            print("Good job!")
            break
        else:
            a += 1
    if a == 5:
        print("You didn't guess :(")
        decision()

def decision():
    decision=input("Do you want to try again? [Y/N]")
    if decision == "Y" or decision == "y":
        os.system('cls' if os.name=='nt' else 'clear')
        print("Make another try - the numbers haven't changed!")
        sugestion()
    elif decision == "N" or decision == "n":
        print("See you")
    
print(drawing_numbers(a, lists))
print(sugestion())
