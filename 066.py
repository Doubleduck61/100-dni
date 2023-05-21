file_path = "D:\IT\Python\Projekty\plik.txt"
f = open(file_path, "r")

def otwarcie():
    zawartosc = f.readlines() #przypisanie zawartości pliku
    return zawartosc

def stworzenie_slownika(zawartosc):
    produkty = []
    for i in zawartosc:
        produkty.append(i.split(',')) #przypisanie do listy - stworzono podział na produkt - cena
    slownik = dict(produkty)
    return slownik

def wywolanie_slownika(slownik):
    for i in slownik:
        if float(slownik[i]) < 8:
            print(i)
try:
    print(wywolanie_slownika(stworzenie_slownika(otwarcie())))
finally:
    f.close()
