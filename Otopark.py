# LINKED LIST (BAĞLI LİSTE) ÜZERİNDE STACK YAPISI

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

# Stack dizisinin elemanlarını ekrana bastırma fonksiyonu tanımlamak
def bastir(r):
    while r != None:
        if r.data != "":
            print(r.data, end=" ")
        r = r.nextt
    print()

# İki farklı stack dizisinin ilk elemanını gösteren iki düğüm tanımlamak
# 1. stack; araçların park sırası için
# 2. stack; öndeki araçları erişirken arkadaki araçları koymak için

# root1
otopark = Node()
otopark.nextt = None

# root2
bahce = Node()
bahce.nextt = None

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
arac_sayisi = 0
iterr = otopark

while iterr != None:
    iterr = iterr.nextt
    arac_sayisi += 1

print("Araç sayısı:", arac_sayisi)

# Otopark içerisinde herhangi bir araca erişmek:

# Otoparktan çıkarılacak aracı kullanıcıdan almak
x = int(input("\nOtoparktan çıkarılacak aracı giriniz: "))

# Çıkarılacak aracın sırasını bulmak
sira = 1
iterr = otopark

while iterr != None:
    if iterr.data == x:
        flag = True
        break
    
    iterr = iterr.nextt
    sira += 1

# Kullanıcının girdiği araç otoparkta yoksa;
else:
    print("\nİstediğiniz araç otoparkta yok!!!")
    flag = False

# Kullanıcının girdiği araç otoparkta varsa;
if flag:
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
otopark = Node()
otopark.nextt = None

bahce = Node()
bahce.nextt = None

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
arac_sayisi = 0
iterr = otopark

while iterr != None:
    iterr = iterr.nextt
    arac_sayisi += 1

print("Otoparktaki araç sayısı:", arac_sayisi)

# 3 nolu aracın sırasını bulmak
sira = 1
iterr = otopark

while iterr != None:
    if iterr.data == 3:
        break
    
    iterr = iterr.nextt
    sira += 1

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
