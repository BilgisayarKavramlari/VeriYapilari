# ARRAY (DİZİ) ÜZERİNDE QUEUE YAPISI

# Queue dizisi için sınıf yapısı oluşturma
class Queue:
    def __init__(self, boyut):
        self.boyut = boyut
        self.array = []
        self.sirabasi = 0
        self.sirasonu = 0
        self.deger = 1
        
        for i in range(1, self.boyut+1):
            self.array.append(None)
    
    # Queue dizisinden eleman çıkarma metodu tanımlama
    def hizmetVer(self):
        if self.sirasonu == self.sirabasi:
            return "Bekleyen müşteri yok!"
        
        elif (self.sirasonu - self.sirabasi) <= (self.boyut / 4):
            temp = Queue(int(self.boyut/2))
            
            temp.sirabasi = self.sirabasi
            temp.sirasonu = self.sirasonu
            
            for i in range(self.sirasonu-self.sirabasi):
                temp.array[i] = self.array[self.sirabasi+i]
            
            temp.sirasonu -= temp.sirabasi
            temp.sirabasi = 0
            
            del self.array
            self.array = temp.array
            self.boyut = temp.boyut
            self.sirabasi = temp.sirabasi
            self.sirasonu = temp.sirasonu
        
        self.sirabasi += 1
        
        return f"{self.array[self.sirabasi-1]} nolu müşterimiz, lütfen vezneye \
geliniz!.."
    
    # Queue dizisine eleman ekleme fonksiyonu tanımlama
    def siraAl(self):
        if self.sirasonu >= self.boyut:
            temp = Queue(self.boyut*2)
            temp.sirabasi = self.sirabasi
            temp.sirasonu = self.sirasonu
            temp.deger = self.deger
            
            for i in range(self.sirasonu):
                temp.array[i] = self.array[i]
            
            del self.array
            self.array = temp.array
            self.boyut = temp.boyut
        
        if self.deger > 1000:
            self.deger = 1
        
        self.array[self.sirasonu] = self.deger
        self.deger += 1
        self.sirasonu += 1
        return f"Sıra numaranız: {self.array[self.sirasonu-1]}"
    
    # Queue dizisindeki elemanları ekrana bastırma fonksiyonu tanımlama
    def bastir(self):
        if self.sirasonu == self.sirabasi:
            return "Bekleyen müşteri yok!"
        
        else:
            print("Bekleyen müşteriler:")
            
            for i in range(self.sirasonu-self.sirabasi):
                print(self.array[i+self.sirabasi], end=" ")
            print()

# OUTPUT:
# Queue dizi sınıfından bir nesne oluşturma
dizi = Queue(2)

# Vezneden sıra fişi alanların ekrana bastırılması
dizi.bastir()
# >>> Bekleyen müşteri yok!

# Banka veznesine 10 kişinin sıra fişi alması
for i in range(10):
    print(dizi.siraAl())

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
dizi.bastir()
# >>>
# Bekleyen müşteriler:
# 1 2 3 4 5 6 7 8 9 10 

# Banka veznesinin 5 kişiye hizmet vermesi
for i in range(5):
    print(dizi.hizmetVer())

# >>>
# 1 nolu müşterimiz, lütfen vezneye geliniz!..
# 2 nolu müşterimiz, lütfen vezneye geliniz!..
# 3 nolu müşterimiz, lütfen vezneye geliniz!..
# 4 nolu müşterimiz, lütfen vezneye geliniz!..
# 5 nolu müşterimiz, lütfen vezneye geliniz!..

# Banka veznesine 20 kişinin sıra fişi alması
for i in range(25):
    dizi.siraAl()

# Vezneden sıra fişi alanların ekrana bastırılması
dizi.bastir()
# >>>
# Bekleyen müşteriler:
# 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
# 33 34 35 

# Banka veznesinin 27 kişiye hizmet vermesi
for i in range(27):
    dizi.hizmetVer()

# Vezneden sıra fişi alanların ekrana bastırılması
dizi.bastir()
# >>>
# Bekleyen müşteriler:
# 33 34 35 

# Banka veznesine 980 kişinin sıra fişi alması
for i in range(980):
    dizi.siraAl()

# Banka veznesinin 950 kişiye hizmet vermesi
for i in range(950):
    dizi.hizmetVer()

# Vezneden sıra fişi alanların ekrana bastırılması
dizi.bastir()
# >>>
# Bekleyen müşteriler:
# 983 984 985 986 987 988 989 990 991 992 993 994 995 996 997 998 999 1000 1 2
# 3 4 5 6 7 8 9 10 11 12 13 14 15 
