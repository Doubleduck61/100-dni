#Napisz kod, który będzie prosił o dwie liczby i będzie je dzielił.
#Zadbaj przy pomocy try / except, o blokadę dzielenia przez 0.

def check(first, second):
    if first.isdigit() and second.isdigit():
        first=int(first)
        second=int(second)
        print("Divide operation:")
        result=first/second
        return result
    else:
        print("You have to enter the numbers!")
        data()
        
first=input("Enter first number: ")
second=input("Enter second number: ")
try:
    print(check(first, second))
except:
    print("You can't divided by 0!")
