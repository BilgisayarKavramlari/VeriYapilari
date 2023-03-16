# LINKED LIST (BAĞLI LİSTE) ÜZERİNDE STACK YAPISI

# Düğüm sınıf yapısı oluşturma
class Node:
    def __init__(self, data="", nextt=""):
        self.data = data
        self.nextt = nextt

deger1 = 1
deger2 = 501
sayac = 0

# Queue dizisinden eleman çıkarma fonksiyonu tanımlama
def hizmetVer():
    global root1
    global root2
    global sayac
    
    if (root1.data == "") and (root2.data == ""):
        return "Bekleyen müşteri yok!"
    else:
        sayac += 1
    
    if ((sayac % 3 == 1) and (root1.data != "")) or (root2.data == ""):
        if root1.nextt == None:
            rvalue = root1.data
            root1.data = ""
            return f"{rvalue} nolu müşterimiz, lütfen vezneye geliniz!.."
        
        rvalue = root1.data
        root1 = root1.nextt
        return f"{rvalue} nolu müşterimiz, lütfen vezneye geliniz!.."
    
    else:
        if root2.nextt == None:
            rvalue = root2.data
            root2.data = ""
            return f"{rvalue} nolu müşterimiz, lütfen vezneye geliniz!.."
        
        rvalue = root2.data
        root2 = root2.nextt
        return f"{rvalue} nolu müşterimiz, lütfen vezneye geliniz!.."

# Queue dizisine eleman ekleme fonksiyonu tanımlama
def siraAl(hizmet_tipi):
    global deger1
    global deger2
    global sirasonu1
    global sirasonu2
    
    if hizmet_tipi == 1:
        if deger1 > 500:
            deger1 = 1
        
        if root1.data == "":
            root1.data = deger1
            sirasonu1 = root1
        
        else:
            sirasonu1.nextt = Node()
            sirasonu1.nextt.data = deger1
            sirasonu1.nextt.nextt = None
            sirasonu1 = sirasonu1.nextt
        
        deger1 += 1
        return f"Sıra numaranız: {deger1-1}"
    
    elif hizmet_tipi == 2:
        if deger2 > 1000:
            deger2 = 501
        
        if root2.data == "":
            root2.data = deger2
            sirasonu2 = root2
        
        else:
            sirasonu2.nextt = Node()
            sirasonu2.nextt.data = deger2
            sirasonu2.nextt.nextt = None
            sirasonu2 = sirasonu2.nextt
        
        deger2 += 1
        return f"Sıra numaranız: {deger2-1}"

# Queue dizisindeki elemanları ekrana bastırma fonksiyonu tanımlama
def bastir():
    if (root1.data == "") and (root2.data == ""):
        return "Bekleyen müşteri yok!"
    
    else:
        if root1.data != "":
            print("Havale, fatura ödemesi ve cari hesap işlemleri için bekleyen \
müşteriler:")
            
            iterr = root1
            
            while iterr != None:
                if iterr.data != "":
                    print(iterr.data, end=" ")
                iterr = iterr.nextt
            print()
        
        if (root1.data != "") and (root2.data != ""):
            print()
        
        if root2.data != "":
            print("Yatırım işlemleri ve vadeli hesaplar için bekleyen \
müşteriler:")
            
            iterr = root2
            
            while iterr != None:
                if iterr.data != "":
                    print(iterr.data, end=" ")
                iterr = iterr.nextt
            print()

# Queue dizi sınıfından iki hizmet tipi için iki tane düğüm oluşturma
root1 = Node()
root1.nextt = None

root2 = Node()
root2.nextt = None

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

# Banka veznesine tip 1 hizmet için 20 kişinin sıra fişi alması
for i in range(20):
    siraAl(1)

# Banka veznesine tip 2 hizmet için 40 kişinin sıra fişi alması
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

# Banka veznesine tip 2 hizmet için 950 kişinin sıra fişi alması
for i in range(950):
    siraAl(2)

# Banka veznesinin 1430 kişiye hizmet vermesi
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
