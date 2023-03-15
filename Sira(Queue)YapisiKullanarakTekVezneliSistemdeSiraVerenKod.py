# LINKED LIST (BAĞLI LİSTE) ÜZERİNDE STACK YAPISI

# Düğüm sınıf yapısı oluşturma
class Node:
    def __init__(self, data="", nextt=""):
        self.data = data
        self.nextt = nextt

deger = 1

# Queue dizisinden eleman çıkarma metodu tanımlama
def hizmetVer():
    global root
    
    if root.data == "":
        return "Bekleyen müşteri yok!"
    
    elif root.nextt == None:
        rvalue = root.data
        root.data = ""
        return f"{rvalue} nolu müşterimiz, lütfen vezneye geliniz!.."
    
    rvalue = root.data
    root = root.nextt
    return f"{rvalue} nolu müşterimiz, lütfen vezneye geliniz!.."

# Queue dizisine eleman ekleme fonksiyonu tanımlama
def siraAl():
    global deger
    global sirasonu
    
    if deger > 1000:
        deger = 1
    
    if root.data == "":
        root.data = deger
        sirasonu = root
    
    else:
        sirasonu.nextt = Node()
        sirasonu.nextt.data = deger
        sirasonu.nextt.nextt = None
        sirasonu = sirasonu.nextt
    
    deger += 1
    return f"Sıra numaranız: {deger-1}"

# Queue dizisindeki elemanları ekrana bastırma fonksiyonu tanımlama
def bastir():
    iterr = root
    
    while iterr != None:
        if iterr.data != "":
            print(iterr.data, end=" ")
        iterr = iterr.nextt
    print()

# OUTPUT:
# Queue dizi sınıfından bir tane düğün nesnesi oluşturma
root = Node()
root.nextt = None

# Vezneden sıra fişi alanların ekrana bastırılması
bastir()
# >>> Bekleyen müşteri yok!

# Banka veznesine 10 kişinin sıra fişi alması
for i in range(10):
    print(siraAl())

# >>>
# Sıra numaranız: 1
# Sıra numaranız: 2
# Sıra numaranız: 3
# Sıra numaranız: 4
# Sıra numaranız: 5
# Sıra numaranız: 6
# Sıra numaranız: 7
# Sıra numaranız: 8
# Sıra numaranız: 9
# Sıra numaranız: 10

# Vezneden sıra fişi alanların ekrana bastırılması
bastir()
# >>>
# Bekleyen müşteriler:
# 1 2 3 4 5 6 7 8 9 10 

# Banka veznesinin 5 kişiye hizmet vermesi
for i in range(5):
    print(hizmetVer())

# >>>
# 1 nolu müşterimiz, lütfen vezneye geliniz!..
# 2 nolu müşterimiz, lütfen vezneye geliniz!..
# 3 nolu müşterimiz, lütfen vezneye geliniz!..
# 4 nolu müşterimiz, lütfen vezneye geliniz!..
# 5 nolu müşterimiz, lütfen vezneye geliniz!..

# Banka veznesine 20 kişinin sıra fişi alması
for i in range(25):
    siraAl()

# Vezneden sıra fişi alanların ekrana bastırılması
bastir()
# >>>
# Bekleyen müşteriler:
# 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
# 33 34 35 

# Banka veznesinin 27 kişiye hizmet vermesi
for i in range(27):
    hizmetVer()

# Vezneden sıra fişi alanların ekrana bastırılması
bastir()
# >>>
# Bekleyen müşteriler:
# 33 34 35 

# Banka veznesine 980 kişinin sıra fişi alması
for i in range(980):
    siraAl()

# Banka veznesinin 950 kişiye hizmet vermesi
for i in range(950):
    hizmetVer()

# Vezneden sıra fişi alanların ekrana bastırılması
bastir()
# >>>
# Bekleyen müşteriler:
# 983 984 985 986 987 988 989 990 991 992 993 994 995 996 997 998 999 1000 1 2
# 3 4 5 6 7 8 9 10 11 12 13 14 15 
