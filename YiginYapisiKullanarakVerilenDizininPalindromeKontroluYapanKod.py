# LINKED LIST (BAĞLI LİSTE) ÜZERİNDE STACK YAPISI

# Düğüm sınıf yapısı oluşturmak
class Node:
    def __init__(self, data="", nextt=""):
        self.data = data
        self.nextt = nextt

# Stack dizisinden eleman çıkarma fonksiyonu tanımlamak
def popItem(r):
    if r.data == "":
        return "Stack boş!!!"

    elif r.nextt == None:
        rvalue = r.data
        r.data = ""
        return rvalue

    iterr = r

    while iterr.nextt.nextt != None:
        iterr = iterr.nextt

    rvalue = iterr.nextt.data
    iterr.nextt = None
    return rvalue

# Stack dizisine eleman ekleme fonksiyonu tanımlamak
def pushItem(r, a):
    if r.data == "":
        r.data = a
        return

    while r.nextt != None:
        r = r.nextt

    r.nextt = Node()
    r.nextt.data = a
    r.nextt.nextt = None

# Stack dizisi oluşturmak
s = Node()
s.nextt = None

# Palindrome kontrolü yapılacak örnek sayıların listesi:
liste = [3, 5, 7, 7, 5, 3]

# Palindrome kontrolü için sayıların yarısını stack dizine koymak
if len(liste) % 2 == 0:
    n = int(len(liste) / 2)
else:
    n = int(len(liste) / 2) + 1

for i in range(n):
    pushItem(s, liste[i])

# Stack dizisine konulmayan, geriye kalan sayılarla stack'ten alınan 'pop()'
# değerleri karşılaştırmak
if len(liste) % 2 == 0:
    for i in range(n, len(liste)):
        sonuc = popItem(s)
        
        if sonuc == liste[i]:
            flag = True
        else:
            flag = False
            break
else:
    for i in range(n-1, len(liste)):
        sonuc = popItem(s)
        
        if sonuc == liste[i]:
            flag = True
        else:
            flag = False
            break

if flag:
    print("Palindrome’dur")
else:
    print("Palindrome Değildir")

# OUTPUT:
liste = [3, 5, 7, 7, 5, 3]
# >>> Palindrome’dur

# OUTPUT 2:
liste = [1, 2, 3, 4, 5, 6]
# >>> Palindrome Değildir
