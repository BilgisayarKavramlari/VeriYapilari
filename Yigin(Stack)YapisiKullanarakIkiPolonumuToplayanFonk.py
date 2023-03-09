# ARRAY (DİZİ) ÜZERİNDE STACK YAPISI

# Stack dizisi için sınıf yapısı oluşturma
class Stack:
    def __init__(self, boyut):
        self.boyut = boyut
        self.tepe = 0
        self.dizi = []
        
        for i in range(self.boyut):
            self.dizi.append(None)

# Stack dizisinden eleman çıkarma fonksiyonu tanımlama
def popItem(s):
    if s.tepe == 0:
        return "Stack boş!!!"
    
    elif s.tepe <= (s.boyut / 4):
        s.boyut = int(s.boyut / 2)
        
        for i in range(s.tepe):
            s.dizi.pop()
    
    s.tepe -= 1
    return s.dizi[s.tepe]

# Stack dizisine eleman ekleme fonksiyonu tanımlama
def pushItem(s, a):
    if s.tepe >= s.boyut:
        s.boyut *= 2
        
        for i in range(s.boyut - s.tepe):
            s.dizi.append(None)
    
    s.dizi[s.tepe] = a
    s.tepe += 1

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
    s1 = Stack(2)
    s2 = Stack(2)
    
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
    if s1.tepe != 0:
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
İki polinomun toplam sonucu: [2, 7, 1, 2, 8]
