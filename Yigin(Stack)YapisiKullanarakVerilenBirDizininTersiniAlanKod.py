# ARRAY (DİZİ) ÜZERİNDE STACK YAPISI

# Stack sınıf yapısı oluşturmak
class Stack:
    def __init__(self, boyut):
        self.boyut = boyut
        self.tepe = 0
        self.dizi = []

        for i in range(self.boyut):
            self.dizi.append(None)

# Stack dizisinden eleman çıkarma fonksiyonu tanımlamak
def popItem(s):
    if s.tepe == 0:
        return "Dizi boş!!!"

    elif s.tepe <= (s.boyut / 4):
        s.boyut = int(s.boyut / 2)

        for i in range(s.tepe):
            s.dizi.pop()

    s.tepe -= 1
    return s.dizi[s.tepe]

# Stack dizisine eleman ekleme fonksiyonu tanımlamak
def pushItem(s, a):
    if s.tepe >= s.boyut:
        s.boyut *= 2

        for i in range(s.boyut - s.tepe):
            s.dizi.append(None)

    s.dizi[s.tepe] = a
    s.tepe += 1

# Stack dizisinin elemanlarını ekrana bastırma fonksiyonu tanımlamak
def bastir(s):
    for i in range(s.tepe):
        print(s.dizi[i], end=" ")
    print()

# İki adet 2 boyutlu Stack dizisi oluşturmak
s1 = Stack(2)
s2 = Stack(2)

# s1 dizisine 0'dan 90'a kadar for döngüsüyle 10 adet eleman eklemek
for i in range(10):
    pushItem(s1, i * 10)

# s1 ve s2 dizilerini ekrana bastırmak
bastir(s1)
# >>> 90 80 70 60 50 40 30 20 10 0 

bastir(s2)
# >>> 

# s1 dizisindeki elemanları tek tek diziden çıkarmak ve pop() edilenleri s2
# dizisine eklemek
for i in range(10):
    pushItem(s2, popItem(s1))

# s1 ve s2 dizilerini ekrana bastırmak
bastir(s1)
# >>> 

bastir(s2)
# >>> 90 80 70 60 50 40 30 20 10 0 
