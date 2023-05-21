file_path = "D:\IT\Python\Projekty\plik.txt"
produkty = []

def otwarcie():
    f = open(file_path, "r")
    zawartosc = f.readlines() #przypisanie zawartości pliku
    for i in range(0,len(zawartosc)):  
        zawartosc[i] = zawartosc[i].replace("\n","") #kasujemy \n
    return zawartosc

def stworzenie_slownika(zawartosc, produkty):
    for i in zawartosc:
        produkty.append(i.split(',')) #przypisanie do listy - stworzono podział na produkt - cena
    slownik = dict(produkty)
    return slownik

def wywolanie_slownika(slownik):
    for i in slownik:
        if float(slownik[i]) < 8:
            print(i)

print(wywolanie_slownika(stworzenie_slownika(otwarcie(), produkty)))
