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
print("Lista produktów do kupienia: ")
print("Towar:\t Szt.: \t Cena:")
for i in products:
    if a < dlugosc:
        produkt=to_buy[a]
        print(to_buy[a],"\t",products.count(produkt),"\t",price[produkt])
        a+=1
