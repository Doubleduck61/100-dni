#Przygotuj aplikację która.
#Będzie miała wbudowany cennik wszystkich produktów.
#Przygotuje listę zakupów, złożoną z unikalnych produktów oraz podanej obok liczby produktów do kupienia.
#Wyliczy wartość zakupów i poda ją w podsumowaniu.

price = {
    "jajka": 5,
    "chleb": 2,
    "mleko": 3,
    "masło": 8,
    "jabłka": 1,
}

print(price["jajka"])

products = ["jajka", "mleko", "chleb", "jajka", "masło", "jajka", "jabłka", "chleb"]
to_buy = list(set(products))
dlugosc=len(to_buy)
a=0
koszt=[]
print("Lista produktów do kupienia: ")
print("Towar:\t Szt.: \t Cena:")
for i in products:
    if a < dlugosc:
        produkt=to_buy[a]
        print(to_buy[a],"\t",products.count(produkt),"\t",(products.count(produkt))*(price[produkt]),"zł")
        a+=1
        koszt.append((products.count(produkt))*(price[produkt]))
        koszt_calkowity=sum(koszt)
        
print("Należność za wszystko wynosi:",koszt_calkowity,"zł")
