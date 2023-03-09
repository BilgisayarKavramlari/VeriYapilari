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

# 1. polinomun katsayılarının tutulduğu diziyi oluşturma
a = [3, 0, 2, 5]        # 3x^3 + 2x + 5

# 2. polinomun katsayılarının tutulduğu diziyi oluşturma
b = [2, 4, 1, 0, 3]     # 2x^4 + 4x^3 + x^2 + 3

#İki polinomu toplayan fonksiyonu tanımlama
def polinomTopla(d1, d2):
    """
    Fonksiyona parametre olarak gönderilen iki dizinin iki stack yardımıyla iki
    polinomun toplanması..
    """
    # Stack sınıfından İki adet nesne oluşturma
    s1 = Node()
    s1.nextt = None
    
    s2 = Node()
    s2.nextt = None
    
    # Fonksiyona gönderilen ilk diziyi s1 yığınına ekleme
    for i in d1:
        pushItem(s1, i)
    
    # Fonksiyona gönderilen ikinci diziyi s2 yığınına ekleme
    for i in d2:
        pushItem(s2, i)
    
    # Terim sayısı az ve çok olan polinomu bulma
    if len(a) > len(b):
        buyuk = len(a)
        kucuk = len(b)
    else:
        buyuk = len(b)
        kucuk = len(a)
    
    fark = buyuk - kucuk
    
    # toplam polinomun katsayılarının tutulacağı boş dizi tanımlama
    toplam = [None for i in range(buyuk)]
    
    # Az olan terim sayısına göre polinomları toplama
    for i in range(kucuk):
        buyuk -= 1
        toplam[buyuk] = popItem(s1) + popItem(s2)
    
    # Terim sayısı büyük olan polinomun yığınında kalan terimleri toplam dizisine
    # ekleme
    if s1 == 0:
        for i in range(fark):
            buyuk -= 1
            toplam[buyuk] = popItem(s1)
    else:
        for i in range(fark):
            buyuk -= 1
            toplam[buyuk] = popItem(s2)
    
    return toplam

# Toplama fonksiyonunu çağırma
print("İki polinomun toplam sonucu:", polinomTopla(a, b))

# OUTPUT:
# >>> İki polinomun toplam sonucu: [2, 7, 1, 2, 8]
