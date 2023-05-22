import os
file_path = "D:\IT\Python\Projekty\qptodo.txt"
f=open(file_path, "a")
ok=True

def start():
    os.system('cls' if os.name=='nt' else 'clear')
    print("[1] Dodanie zadania do listy")
    print("[2] Wyszukanie zadania")
    print("[3] Exit")
    decyzja=input("Co chcesz zrobić? [1/2/3]")
    if decyzja.isdigit():
        decyzja=int(decyzja)
        if decyzja >= 1 and decyzja <=3:
            return decyzja
    else:
        start()

def decyzyja(decyzja):
    os.system('cls' if os.name=='nt' else 'clear')
    if decyzja == 1:
        print(dodawanie())
    elif decyzja == 2:
        print(wyszukiwanie())
    elif decyzja == 3:
        print(wyjscie())
    else:
        start()

def dodawanie():
    while ok==True:
        zadanie = str(input("Podaj zadanie do zrobienia ('Exit' zakończy pętlę): "))
        zadanie_zmienione=zadanie.lower()
        zadanie_zmienione=zadanie.capitalize()
        if zadanie == "Exit":
            break
        f.write(zadanie_zmienione+"\n")
    decyzyja(start())

def wyszukiwanie():
    f.close()
    os.system('cls' if os.name=='nt' else 'clear')
    g = open(file_path, "r")
    zawartosc = g.readlines()
    lista_zadan = []
    for i in range(len(zawartosc)):
        zawartosc[i] = zawartosc[i].replace("\n","")
    for i in zawartosc:
        lista_zadan.append(i) #przypisanie do listy - stworzono podział
    #print(produkty)
    szukanie=input("Jakiej frazy szukasz? ")
    rozdrobnienie(szukanie, lista_zadan)

def rozdrobnienie(szukanie, lista_zadan):
    a=0
    b=0
    c=0
    rozdrobniona_lista=[]
    for i in range(len(lista_zadan)):
        while b < len(lista_zadan):
            lista_zadan[b] = lista_zadan[b].replace(" ",",")
            b+=1
    #print(produkty)
    for i in lista_zadan:
        rozdrobniona_lista.extend(i.split(','))
    porównanie_z_bazą_danych(szukanie, lista_zadan, rozdrobniona_lista,a,c)

def porównanie_z_bazą_danych(szukanie, lista_zadan, rozdrobniona_lista,a,c):
    while a < len(rozdrobniona_lista):
        a += 1
        if a == len(rozdrobniona_lista):
                print("Nie ma zadania z taką frazą :(")
                break
        elif szukanie != rozdrobniona_lista[a]:
            if rozdrobniona_lista[a] == rozdrobniona_lista[a].capitalize():
                c+=1
        elif szukanie == rozdrobniona_lista[a]:
            for i in range(len(lista_zadan)):
                lista_zadan[c] = lista_zadan[c].replace(","," ")
            print(f"Zadanie którego szukasz to:\n{lista_zadan[c]}")
            return ""

def wyjscie():
    f.close()
    print("Do widzenia!")
    ok = False

print(decyzyja(start()))
