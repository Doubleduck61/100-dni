#Napisz słownik angielsko-polski. Pierwsza litera zawsze powinna być duża.
#Jeśli dane słowo nie jest w słowniku, oznacz je poprzez * na końcu słowa.
dict = {
    "ja":"I",
    "pies":"dog",
    "kot":"cat",
    "siostra":"siostra",
    "brat":"brother",
    "ryba":"fish",
    "dom":"house",
    "telefon":"phone",
    "komputer":"computer",
    "kolano":"knee",
    "mysz":"mouse"
}

def capital_first_letter():
    one=lists[0]
    lists[0]=(one[0:1].upper()+one[1:])
    return lists[0]
    
polish_sentence=input("Enter your sentence in Polish: ")
words=polish_sentence.split()
lists = []

for word in words:
    if word in dict:
        lists.append(dict[word])
    else:
        lists.append(word + "*")

capital_first_letter()

english_sentence=" ".join(lists)
print(english_sentence)
