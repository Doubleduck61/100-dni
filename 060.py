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

a=0
cost=[]
products = ["jajka", "mleko", "chleb", "jajka", "masło", "jajka", "jabłka", "chleb"]

to_buy = list(set(products))
length=len(to_buy)
print("Lists of product to buy: ")
print("Iteam:\t Piece.: \t Price:")
for i in products:
    if a < length:
        product=to_buy[a]
        print(product,"\t",products.count(product),"\t\t",(products.count(product))*(price[product]),"zł")
        a+=1
        cost.append((products.count(product))*(price[product]))
        total_cost=sum(cost)
        
print()
print("Total cost is: ",total_cost,"zł")
