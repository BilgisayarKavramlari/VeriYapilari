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

# İki farklı stack dizisinin ilk elemanını gösteren iki düğüm tanımlamak
katsayi = Node()
katsayi.nextt = None

derece = Node()
derece.nextt = None

# Polinomun katsayılarının tutulduğu diziyi oluşturma
a = [3, 0, 2, 5]    # 3x^3 + 2x + 5

# Dizinin boyutunu tanımlama
n = len(a)

# Polinom dizisini stack yapısına ekleme
for i in a:
    pushItem(katsayi, i)

# Polinomdaki terimlerin derecelerini stack yapısına ekleme
for i in range(n-1, -1, -1):
    pushItem(derece, i)

# Kullanıcıdan polinomdaki x'in değerini alma
x = int(input("Polinomdaki x değerini giriniz: "))

# Polinomu kullanıcıdan alınan x değerine göre çözme
toplam = 0

for i in range(n):
    toplam += popItem(katsayi) * (x ** popItem(derece))

print("Çözüm:", toplam)

# OUTPUT:
# Polinomdaki x değerini giriniz: 2
# >>> Çözüm: 33

# OUTPUT 2:
# Polinomdaki x değerini giriniz: 3
# >>> Çözüm: 92
