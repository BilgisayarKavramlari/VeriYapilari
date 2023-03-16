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

sayac = 0

# Queue dizisinden eleman çıkarma fonksiyonu tanımlama
def hizmetVer():
    global sayac
    
    if (dizi1.sirasonu == dizi1.sirabasi) and (dizi2.sirasonu == dizi2.sirabasi):
        return "Bekleyen müşteri yok!"
    else:
        sayac += 1
    
    if ((sayac % 3 == 1) and (dizi1.sirasonu != dizi1.sirabasi)) or (dizi2.sirasonu == dizi2.sirabasi):
        if (dizi1.sirasonu - dizi1.sirabasi) <= (dizi1.boyut / 4):
            temp = Queue(int(dizi1.boyut/2))
            
            temp.sirabasi = dizi1.sirabasi
            temp.sirasonu = dizi1.sirasonu
            
            for i in range(dizi1.sirasonu-dizi1.sirabasi):
                temp.array[i] = dizi1.array[dizi1.sirabasi+i]
            
            temp.sirasonu -= temp.sirabasi
            temp.sirabasi = 0
            
            del dizi1.array
            dizi1.array = temp.array
            dizi1.boyut = temp.boyut
            dizi1.sirabasi = temp.sirabasi
            dizi1.sirasonu = temp.sirasonu
        
        dizi1.sirabasi += 1
        
        return f"{dizi1.array[dizi1.sirabasi-1]} nolu müşterimiz, lütfen vezneye \
geliniz!.."
    
    else:
        if (dizi2.sirasonu - dizi2.sirabasi) <= (dizi2.boyut / 4):
            temp = Queue(int(dizi2.boyut/2))
            
            temp.sirabasi = dizi2.sirabasi
            temp.sirasonu = dizi2.sirasonu
            
            for i in range(dizi2.sirasonu-dizi2.sirabasi):
                temp.array[i] = dizi2.array[dizi2.sirabasi+i]
            
            temp.sirasonu -= temp.sirabasi
            temp.sirabasi = 0
            
            del dizi2.array
            dizi2.array = temp.array
            dizi2.boyut = temp.boyut
            dizi2.sirabasi = temp.sirabasi
            dizi2.sirasonu = temp.sirasonu
        
        dizi2.sirabasi += 1
        
        return f"{dizi2.array[dizi2.sirabasi-1]} nolu müşterimiz, lütfen vezneye \
geliniz!.."
    
# Queue dizisine eleman ekleme fonksiyonu tanımlama
def siraAl(hizmet_tipi):
    if hizmet_tipi == 1:
        if dizi1.sirasonu >= dizi1.boyut:
            temp = Queue(dizi1.boyut*2)
            temp.sirabasi = dizi1.sirabasi
            temp.sirasonu = dizi1.sirasonu
            temp.deger = dizi1.deger
            
            for i in range(dizi1.sirasonu):
                temp.array[i] = dizi1.array[i]
            
            del dizi1.array
            dizi1.array = temp.array
            dizi1.boyut = temp.boyut
        
        if dizi1.deger > 500:
            dizi1.deger = 1
        
        dizi1.array[dizi1.sirasonu] = dizi1.deger
        dizi1.deger += 1
        dizi1.sirasonu += 1
        return f"Sıra numaranız: {dizi1.array[dizi1.sirasonu-1]}"
    
    elif hizmet_tipi == 2:
        
        if dizi2.sirasonu >= dizi2.boyut:
            temp = Queue(dizi2.boyut*2)
            temp.sirabasi = dizi2.sirabasi
            temp.sirasonu = dizi2.sirasonu
            temp.deger = dizi2.deger
            
            for i in range(dizi2.sirasonu):
                temp.array[i] = dizi2.array[i]
            
            del dizi2.array
            dizi2.array = temp.array
            dizi2.boyut = temp.boyut
        
        if dizi2.deger > 500:
            dizi2.deger = 1
        
        dizi2.array[dizi2.sirasonu] = dizi2.deger + 500
        dizi2.deger += 1
        dizi2.sirasonu += 1
        return f"Sıra numaranız: {dizi2.array[dizi2.sirasonu-1]}"

# Queue dizisindeki elemanları ekrana bastırma fonksiyonu tanımlama
def bastir():
    if (dizi1.sirasonu == dizi1.sirabasi) and (dizi2.sirasonu == dizi2.sirabasi):
        return "Bekleyen müşteri yok!"
    
    else:
        if dizi1.sirasonu != dizi1.sirabasi:
            print("Havale, fatura ödemesi ve cari hesap işlemleri için bekleyen \
müşteriler:")
            
            for i in range(dizi1.sirasonu-dizi1.sirabasi):
                print(dizi1.array[i+dizi1.sirabasi], end=" ")
            print()
        
        if (dizi1.sirasonu != dizi1.sirabasi) and (dizi2.sirasonu != dizi2.sirabasi):
            print()
        
        if dizi2.sirasonu != dizi2.sirabasi:
            print("Yatırım işlemleri ve vadeli hesaplar için bekleyen \
müşteriler:")
            
            for i in range(dizi2.sirasonu-dizi2.sirabasi):
                print(dizi2.array[i+dizi2.sirabasi], end=" ")
            print()

# Queue dizi sınıfından iki hizmet tipi için iki nesne oluşturma
dizi1 = Queue(2)
dizi2 = Queue(2)

# Vezneden sıra fişi alanların ekrana bastırılması
bastir()
# >>> Bekleyen müşteri yok!

# Banka veznesine tip 1 hizmet için 10 kişinin sıra fişi alması
for i in range(10):
    print(siraAl(1))

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

# Banka veznesine tip 2 hizmet için 20 kişinin sıra fişi alması
for i in range(20):
    print(siraAl(2))

# >>>
# Sıra numaranız: 501
# Sıra numaranız: 502
# Sıra numaranız: 503
# Sıra numaranız: 504
# Sıra numaranız: 505
# Sıra numaranız: 506
# Sıra numaranız: 507
# Sıra numaranız: 508
# Sıra numaranız: 509
# Sıra numaranız: 510
# Sıra numaranız: 511
# Sıra numaranız: 512
# Sıra numaranız: 513
# Sıra numaranız: 514
# Sıra numaranız: 515
# Sıra numaranız: 516
# Sıra numaranız: 517
# Sıra numaranız: 518
# Sıra numaranız: 519
# Sıra numaranız: 520

# Vezneden sıra fişi alanların ekrana bastırılması
bastir()
# >>>
# Havale, fatura ödemesi ve cari hesap işlemleri için bekleyen müşteriler:
# 1 2 3 4 5 6 7 8 9 10 

# Yatırım işlemleri ve vadeli hesaplar için bekleyen müşteriler:
# 501 502 503 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 

# Banka veznesinin 10 kişiye hizmet vermesi
for i in range(10):
    print(hizmetVer())

# >>>
# 1 nolu müşterimiz, lütfen vezneye geliniz!..
# 501 nolu müşterimiz, lütfen vezneye geliniz!..
# 502 nolu müşterimiz, lütfen vezneye geliniz!..
# 2 nolu müşterimiz, lütfen vezneye geliniz!..
# 503 nolu müşterimiz, lütfen vezneye geliniz!..
# 504 nolu müşterimiz, lütfen vezneye geliniz!..
# 3 nolu müşterimiz, lütfen vezneye geliniz!..
# 505 nolu müşterimiz, lütfen vezneye geliniz!..
# 506 nolu müşterimiz, lütfen vezneye geliniz!..
# 4 nolu müşterimiz, lütfen vezneye geliniz!..

# Vezneden sıra fişi alanların ekrana bastırılması
bastir()
# >>>
# Havale, fatura ödemesi ve cari hesap işlemleri için bekleyen müşteriler:
# 5 6 7 8 9 10 

# Yatırım işlemleri ve vadeli hesaplar için bekleyen müşteriler:
# 507 508 509 510 511 512 513 514 515 516 517 518 519 520 

# Banka veznesine tip 1 hizmet için 25 kişinin sıra fişi alması
for i in range(20):
    siraAl(1)

# Banka veznesine tip 2 hizmet için 50 kişinin sıra fişi alması
for i in range(40):
    siraAl(2)

# Vezneden sıra fişi alanların ekrana bastırılması
bastir()
# >>>
# Havale, fatura ödemesi ve cari hesap işlemleri için bekleyen müşteriler:
# 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 

# Yatırım işlemleri ve vadeli hesaplar için bekleyen müşteriler:
# 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525
# 526 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544
# 545 546 547 548 549 550 551 552 553 554 555 556 557 558 559 560 

# Banka veznesinin 30 kişiye hizmet vermesi
for i in range(30):
    hizmetVer()

# Vezneden sıra fişi alanların ekrana bastırılması
bastir()
# >>>
# Havale, fatura ödemesi ve cari hesap işlemleri için bekleyen müşteriler:
# 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 

# Yatırım işlemleri ve vadeli hesaplar için bekleyen müşteriler:
# 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545
# 546 547 548 549 550 551 552 553 554 555 556 557 558 559 560 

# Banka veznesine tip 1 hizmet için 480 kişinin sıra fişi alması
for i in range(480):
    siraAl(1)

# Banka veznesine tip 2 hizmet için 480 kişinin sıra fişi alması
for i in range(950):
    siraAl(2)

# Banka veznesinin 950 kişiye hizmet vermesi
for i in range(1430):
    hizmetVer()

# Vezneden sıra fişi alanların ekrana bastırılması
bastir()
# >>>
# Havale, fatura ödemesi ve cari hesap işlemleri için bekleyen müşteriler:
# 491 492 493 494 495 496 497 498 499 500 1 2 3 4 5 6 7 8 9 10 

# Yatırım işlemleri ve vadeli hesaplar için bekleyen müşteriler:
# 981 982 983 984 985 986 987 988 989 990 991 992 993 994 995 996 997 998 999
# 1000 501 502 503 504 505 506 507 508 509 510 
