import os
file_path = "D:\IT\Python\Projekty\qptodo.txt"
f=open(file_path, "a")
ok=True

def start():
    os.system('cls' if os.name=='nt' else 'clear')
    print("[1] Dodanie zadania do listy")
    print("[2] Wyszukanie zadania")
    print("[3] Exit")
    decyzja=int(input("Co chcesz zrobić? [1/2/3]"))
    return decyzja
    
def dodawanie():
    while ok==True:
        x = str(input("Podaj zadanie do zrobienia: "))
        p=x.lower()
        p=x.capitalize()
        if x == "Exit":
            break
        f.write(p+"\n")
    decyzyja(start())

def wyszukiwanie():
    f.close()
    os.system('cls' if os.name=='nt' else 'clear')
    g = open(file_path, "r")
    zawartosc = g.readlines()
    produkty = []
    for i in range(len(zawartosc)):
        zawartosc[i] = zawartosc[i].replace("\n","")
    for i in zawartosc:
        produkty.append(i) #przypisanie do listy - stworzono podział
    #print(produkty)
    szukanie=input("Jakiej frazy szukasz? ")
    a=0
    b=0
    c=0
    dodatkowa_lista=[]
    for i in range(len(produkty)):
        while b < len(produkty):
            produkty[b] = produkty[b].replace(" ",",")
            b+=1
    #print(produkty)
    for i in produkty:
        dodatkowa_lista.extend(i.split(','))
    #print(dodatkowa_lista)
    while a < len(dodatkowa_lista):
        a += 1
        if a == len(dodatkowa_lista):
                print("Nie ma zadania z taką frazą :(")
                break
        elif szukanie != dodatkowa_lista[a]:
            if dodatkowa_lista[a] == dodatkowa_lista[a].capitalize():
                c+=1
        elif szukanie == dodatkowa_lista[a]:
            for i in range(len(produkty)):
                produkty[c] = produkty[c].replace(","," ")
            print(f"Zadanie któego szukasz to:\n{produkty[c]}")
            return ""

def wyjscie():
    f.close()
    print("Do widzenia!")
    ok = False
    
def decyzyja(decyzja):
    if decyzja == 1:
        print(dodawanie())
    elif decyzja == 2:
        print(wyszukiwanie())
    elif decyzja == 3:
        print(wyjscie())
    else:
        start()

print(decyzyja(start()))
