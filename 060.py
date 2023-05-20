# Przygotuj aplikację która.
# Będzie miała wbudowany cennik wszystkich produktów.
# Przygotuje listę zakupów, złożoną z unikalnych produktów oraz podanej obok liczby produktów do kupienia.
# Wyliczy wartość zakupów i poda ją w podsumowaniu.\
# złe odwołanie w pętli for. Postaraj się odwołać do elementu i i po tym iterować funkcję for
price = {
    "jajka": 5,
    "chleb": 2,
    "mleko": 3,
    "masło": 8,
    "jabłka": 1,
}

a = 0
cost = []
products = ["jajka", "mleko", "chleb", "jajka", "masło", "jajka", "jabłka", "chleb"]

def lists(a, cost, products):
    to_buy = list(set(products))
    length = len(to_buy)
    for i in products:
        if a < length:
            product = to_buy[a]
            print(product, "\t", products.count(product), "\t\t", (products.count(product)) * (price[product]), "zł")
            a += 1
            if a < length:
                all_money(a, cost, products)
            else:
                break
    return ""
            
def all_money(a, cost, products):
    to_buy = list(set(products))
    product = to_buy[a]
    cost.append((products.count(product)) * (price[product]))
    total_cost = sum(cost)
    return total_cost
    
print("Lists of product to buy: ")
print("Iteam:\t Piece.: \t Price:\n")
print(lists(a, cost, products))
print("Total cost:", all_money(a, cost, products), "zł")
