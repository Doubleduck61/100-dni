#Twoim zadaniem jest stworzenie WŁASNEJ funkcji substring.
#Nie używaj systemowej, tylko napisz ją od zera (nie używaj slice(), ani [x:y])
#A jak już zaimplementujesz, wykonaj przy jej pomocy następujące zadania testowe -
#Z "Zero To Junior" wyciągnij 4 pierwsze znaki
#Z "Zero To Junior" wyciągnij 5 ostatnich znaków
#Znajdź w "Zero To Junior" ciąg "To" i pobierz wszystkie znaki od litery T do końca
#Wyciągnij z "Zero To Junior" znaki od 3 do 8

def substraction(sentence, sign1, sign2):
    part=""
    for i in range(sign1,sign2):
        part += sentence[i]
    return part
    
print("Enter your sentence: ")
sentence=input()
sign1=int(input("Enter number of start sign: "))
sign2=int(input("Enter number of end sign: "))

part=substraction(sentence, sign1, sign2)
print(part)
