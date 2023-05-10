#Zamiana listy na zbiór

digits=[]

def convert():
    ok=True
    while ok==True:
        x=input("Wprowadź liczbę całkowitą: ")
        check=x.isdigit()
        if check==True:
            digits.extend(x)
            ok=True
        else:
            break
    my_set=set(digits)
    my_list=list(my_set)
    return my_list

print(convert())
