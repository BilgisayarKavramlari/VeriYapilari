# ARRAY (DİZİ) ÜZERİNDE STACK YAPISI

# OTOPARK

# SORU:
# Bir otopark işletmecisinin aşağıdaki şekilde arka arkaya park edilebilen park
# alanları bulunmaktadır. Parklardan herhangi bir aracın çıkması için arkasındaki
# bütün araçların çıkması gerekir. (1) Bu işletmecinin otoparktaki herhangi bir
# arabaya erişmek için en az kaç park alanına ihtiyacı vardır. (2) Bu işletmecinin
# herhangi bir arabasına erişmesini sağlayan kodu yazınız. (3) Örneğin aşağıdaki
# park sisteminde 3 numaralı arabaya erişmek istemesi durumunda sırasıyla yapması
# gereken adımları yazınız. 7 2 3 8 1 9 boş boş Yukarıdaki şekilde giriş ve
# çıkışların hepsi sağ taraftan yapılmaktadır, park alanının ön tarafı ve yanları
# duvar ile kapalıdır.


# ÇÖZÜM:

# 1) İşletmecinin otoparktaki herhangi bir arabaya erişmek için en az 2 park
     # alanına ihtiyacı vardır.

# 2) İşletmecinin herhangi bir arabasına erişmesini sağlayan kod:

# Stack dizisi için sınıf yapısı oluşturmak
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
        return "Stack boş!!!"
    
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

# Stack dizisindeki elemanları ekrana bastırma fonksiyonu tanımlamak
def bastir(s):
    for i in range(s.tepe):
        print(s.dizi[i], end=" ")
    print()

# Stack sınıfından iki tane dizi nesnesi oluşturmak
# 1. stack; araçların park sırası için
# 2. stack; öndeki araçları erişirken arkadaki araçları koymak için
otopark = Stack(2)
bahce = Stack(2)

# Otoparkın kapasitesini kullanıcıdan almak
n = int(input("Otoparkın araç kapasitesi: "))

# Gelen araçları otoparka park etmek
print("Park edilecek araçlar: ")
for i in range(n):
    arac = int(input(">> "))
    
    if arac == 0:
        break
    
    pushItem(otopark, arac)

# Otoparktaki araçların ekrana bastırılması
print("\nOtoparktaki araçlar:", end=" ")
bastir(otopark)

# Otoparktaki araçların sayısı
arac_sayisi = otopark.tepe
print("Araç sayısı:", arac_sayisi)

# Otopark içerisinde herhangi bir araca erişmek:

# Otoparktan çıkarılacak aracı kullanıcıdan almak
x = int(input("\nOtoparktan çıkarılacak aracı giriniz: "))

# Çıkarılacak aracın sırasını bulmak
for i in range(arac_sayisi):
    if otopark.dizi[i] == x:
        sira = i + 1
        break

# Çıkarılacak aracın akrasını açmak
for i in range(arac_sayisi - sira):
    pushItem(bahce, popItem(otopark))

# Erişilen aracı müşteriye teslim etmek
print(popItem(otopark), "nolu araç müşteriye teslim edildi.")

# Bahçedeki araçları geri otoparka almak
for i in range(arac_sayisi - sira):
    pushItem(otopark, popItem(bahce))

print("Otoparktaki araçlar:", end=" ")
bastir(otopark)

##############################################

# 3) Örnek bir park sisteminde 3 numaralı arabaya erişmek istemesi durumunda
# sırasıyla yapması gereken adımlar:

ornek_park = [7, 2, 3, 8, 1, 9]

# Stack sınıfından iki tane dizi nesnesi oluşturmak
# 1. stack; araçların park sırası için
# 2. stack; öndeki araçları erişirken arkadaki araçları koymak için
otopark = Stack(2)
bahce = Stack(2)

print("Hedef: 3 nolu aracı otoparktan çıkarıp müşteriye teslim etmek")

# 1. ADIM:
print("\n1. ADIM: ")
# Örnek park listesindeki araçların otopark stak dizisine eklemek - push()
for i in ornek_park:
    pushItem(otopark, i)

# Otoparktaki ve bahçedeki araçları ekrana bastırmak
print("Otoparktaki araçlar\t:", end=" ")
bastir(otopark)

print("Bahçedeki araçlar\t:", end=" ")
bastir(bahce)

# Otopark içerisindeki 3 nolu araca erişmek:

# 2. ADIM:
print("\n2. ADIM:")
# Otoparktaki araçların sayısı
arac_sayisi = otopark.tepe
print("Otoparktaki araç sayısı:", arac_sayisi)

# 3 nolu aracın sırasını bulmak
for i in range(arac_sayisi):
    if otopark.dizi[i] == 3:
        sira = i + 1
        break

print("3 nolu aracın sırası:", sira)

# 3. ADIM:
print("\n3. ADIM:")
# 3 nolu aracın akrasındaki araçları çıkarmak
for i in range(arac_sayisi - sira):
    pushItem(bahce, popItem(otopark))    

# 3 nolu aracın arkası boşaltıldıktan sonra otoparktaki ve bahçedeki araçları
# ekrana bastırmak
print("Otoparktaki araçlar\t:", end=" ")
bastir(otopark)

print("Bahçedeki araçlar\t:", end=" ")
bastir(bahce)

# 4. ADIM:
print("\n4. ADIM:")
# 3 nolu aracı müşteriye teslim etmek
print(popItem(otopark), "nolu araç müşteriye teslim edildi.")

# 3 nolu araç çıkartıldıktan sonra otoparktaki ve bahçedeki araçları ekrana
# bastırmak
print("Otoparktaki araçlar\t:", end=" ")
bastir(otopark)

print("Bahçedeki araçlar\t:", end=" ")
bastir(bahce)

# 5. ADIM:
print("\n5. ADIM:")
# Bahçedeki araçları geri otoparka almak
for i in range(arac_sayisi - sira):
    pushItem(otopark, popItem(bahce))

# Bahçedeki araçlar tekrar otoparka koyulduktan sonra son durumu ekrana bastırmak
print("Otoparktaki araçlar\t:", end=" ")
bastir(otopark)

print("Bahçedeki araçlar\t:", end=" ")
bastir(bahce)

# OUTPUT:
# Hedef: 3 nolu aracı otoparktan çıkarıp müşteriye teslim etmek

# 1. ADIM: 
# Otoparktaki araçlar : 7 2 3 8 1 9 
# Bahçedeki araçlar   : 

# 2. ADIM:
# Otoparktaki araç sayısı : 6
# 3 nolu aracın sırası    : 3

# 3. ADIM:
# Otoparktaki araçlar : 7 2 3 
# Bahçedeki araçlar   : 9 1 8 

# 4. ADIM:
# 3 nolu araç müşteriye teslim edildi.
# Otoparktaki araçlar : 7 2 
# Bahçedeki araçlar   : 9 1 8 

# 5. ADIM:
# Otoparktaki araçlar : 7 2 8 1 9 
# Bahçedeki araçlar   : 
