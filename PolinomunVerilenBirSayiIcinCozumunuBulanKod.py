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

# Stack sınıfından üç tane dizi nesnesi oluşturma
katsayi = Stack(2)
derece = Stack(2)
denklem = Stack(2)

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
