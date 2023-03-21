class Array:
    def __init__(self, boyut):
        self.boyut = boyut
        self.dizi = []
        
        for i in range(self.boyut):
            self.dizi.append(None)

a = Array(10)

for i in range(10):
    a.dizi[i] = int(input(f"Öğrenci {i+1} notunu giriniz: "))

enbuyuk = 0
enkucuk = 100
toplam = 0

for i in range(10):
    if a.dizi[i] > enbuyuk:
        enbuyuk = a.dizi[i]
    
    if a.dizi[i] < enkucuk:
        enkucuk = a.dizi[i]
    
    toplam += a.dizi[i]

ortalama = toplam / 10

print("\nEn büyük: %d, En küçük: %d, Ortalama: %d\n" %(enbuyuk, enkucuk, ortalama))

yeninot = int(input("Yeni bir not daha giriniz: "))

x = False

for i in range(10):
    if yeninot == a.dizi[i]:
        print("Not zaten girilmiş")
        x = True
        break

if x == False:
    print("Not girilmemiş")

# OUTPUT:
# Öğrenci 1 notunu giriniz: 75
# Öğrenci 2 notunu giriniz: 80
# Öğrenci 3 notunu giriniz: 70
# Öğrenci 4 notunu giriniz: 60
# Öğrenci 5 notunu giriniz: 65
# Öğrenci 6 notunu giriniz: 85
# Öğrenci 7 notunu giriniz: 80
# Öğrenci 8 notunu giriniz: 90
# Öğrenci 9 notunu giriniz: 75
# Öğrenci 10 notunu giriniz: 100

# En büyük: 100, En küçük: 60, Ortalama: 78

# Yeni bir not daha giriniz: 95
# Not girilmemiş

# Yeni bir not daha giriniz: 75
# Not zaten girilmiş
