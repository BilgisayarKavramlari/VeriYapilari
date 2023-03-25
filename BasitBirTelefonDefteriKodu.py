import time

class Rehber:
    def __init__(self, ad):
        self.ad = ad
        self.calisma = True
    
    def program(self):
        secim = self.menuSecim()
        
        if secim == 1:
            self.kisiEkle()
        
        elif secim == 2:
            self.kisiSil()
        
        elif secim == 3:
            self.kisiDuzenle()
        
        elif secim == 4:
            self.kisiGoster()
        
        elif secim == 5:
            self.cikis()
    
    def menuSecim(self):
        secim = input(f"""\n**** {self.ad} ****

    1- Kişi Ekle
    2- Kişi Sil
    3- Kişi Düzenle
    4- Kişi Göster
    5- Çıkış

Seçiminizi giriniz: """)
        
        while not secim.isdigit() or int(secim) < 1 or int(secim) > 5:
            secim = input("Lütfen 1 - 5 arasında bir seçim yapınız: ")
            
        secim = int(secim)
        
        return secim
    
    def kisiEkle(self):
        print("\n<< Menü-1: EKLE >>")
        ad = input("\nİsim giriniz: ")
        soyad = input("Soyisim giriniz: ")
        tel_no = input("Telefon numarası giriniz: ")
        
        with open("kisilerim.txt", "r") as dosya:
            kisiListesi = dosya.readlines()
        
        kayit_no = len(kisiListesi) + 1
        
        with open("kisilerim.txt", "a+") as dosya:
            dosya.write(f"{kayit_no}-{ad}-{soyad}-{tel_no}\n")
        
        print(f"\n{ad} {soyad} rehbere kayıt edildi..")
        time.sleep(1.5)
    
    def kisiSil(self):
        print("\n<< Menü-2: SİL >>")
        with open("kisilerim.txt", "r") as dosya:
            kisiler = dosya.readlines()
        
        print()
        
        for kisi in kisiler:
            print(kisi[:-1].split("-")[0] + ".", kisi[:-1].split("-")[1],
                  kisi[:-1].split("-")[2], kisi[:-1].split("-")[3])
        
        if not kisiler:
            print("Silinecek kişi yok!..")
            time.sleep(1.5)
        
        else:
            while True:
                if len(kisiler) == 1:
                    mesaj1 = "\nLütfen silmek istediğiniz kişinin kayıt numarasını \
giriniz (1 adet kayıt): "
                    mesaj2 = "Lütfen 1 nolu kayıt harici seçim yapmayınız: "
                
                elif len(kisiler) == 2:
                    mesaj1 = "\nLütfen silmek istediğiniz kişinin kayıt numarasını \
giriniz (2 adet kayıt): "
                    mesaj2 = "Lütfen 2 kayıt arasından bir seçim yapınız: "
                
                elif len(kisiler) >= 3:
                    mesaj1 = f"\nLütfen silmek istediğiniz kişinin kayıt numarasını \
giriniz (1 - {len(kisiler)} arası): "
                    mesaj2 = f"Lütfen 1 - {len(kisiler)} arasında bir seçim \
yapınız: "
                
                mesaj3 = "\nAna menüye dönmek için basınız ==> <q>"
                
                secim = input(mesaj3 + mesaj1)
                
                if secim == "q":
                    break
                
                while not secim.isdigit() or int(secim) < 1 or int(secim) > len(kisiler):
                    secim = input(mesaj2)
                
                secim = int(secim)
                
                temp = kisiler[secim-1][:-1].split("-")[1] + " " + \
                    kisiler[secim-1][:-1].split("-")[2]
                
                print(f"\n!!! {temp} kişisi rehberden silinecek!.. !!!")
                
                son_uyari = input("\nİPTAL için basınız ==> <q>\nEmin misiniz? \
(e/h): ")
                
                if son_uyari == "q":
                    break
                
                elif son_uyari in ["e", "E", "evet", "Evet", "EVET"]:
                    kisiler.pop(secim-1)
                    yeni_kisiler_listesi = []
                    sayac = 1
                    
                    for kisi in kisiler:
                        yeni_kisiler_listesi.append(str(sayac) + kisi[1:])
                        sayac += 1
                    
                    with open("kisilerim.txt", "w") as dosya:
                        dosya.writelines(yeni_kisiler_listesi)
                    
                    print()
                    print(f"{temp} rehberden silindi..")
                    time.sleep(1.5)
                    break
                
                elif son_uyari in ["h", "H", "hayır", "Hayır", "HAYIR"]:
                    break
    
    def kisiDuzenle(self):
        while True:
            print("\n<< Menü-3: DÜZENLE >>")
            with open("kisilerim.txt", "r") as dosya:
                kisiler = dosya.readlines()
            
            print()
            
            for kisi in kisiler:
                print(kisi[:-1].split("-")[0] + ".", kisi[:-1].split("-")[1],
                      kisi[:-1].split("-")[2], kisi[:-1].split("-")[3])
            
            if not kisiler:
                print("Düzenlenecek kişi yok!..")
                time.sleep(1.5)
                break
            
            else:
                if len(kisiler) == 1:
                    mesaj1 = "\nLütfen düzenlemek istediğiniz kişinin kayıt \
numarasını giriniz (1 adet kayıt): "
                    mesaj2 = "Lütfen 1 nolu kayıt harici seçim yapmayınız: "
                
                elif len(kisiler) == 2:
                    mesaj1 = "\nLütfen düzenlemek istediğiniz kişinin kayıt \
numarasını giriniz (2 adet kayıt): "
                    mesaj2 = "Lütfen 2 kayıt arasından bir seçim yapınız: "
                
                elif len(kisiler) >= 3:
                    mesaj1 = f"\nLütfen düzenlemek istediğiniz kişinin kayıt \
numarasını giriniz (1 - {len(kisiler)} arası): "
                    mesaj2 = f"Lütfen 1 - {len(kisiler)} arasında bir seçim \
yapınız: "
                
                mesaj3 = "\nAna menüye dönmek için basınız ==> <q>"
                
                secim = input(mesaj3 + mesaj1)
                
                if secim == "q":
                    break
                
                while not secim.isdigit() or int(secim) < 1 or int(secim) > len(kisiler):
                    secim = input(mesaj2)
                
                secim = int(secim)
                
                while True:
                    duzenleme_alani = input("""
   1- İsim
   2- Soyisim
   3- Telefon no
    
İPTAL için basınız ==> <q>
Lütfen düzenlemek istediğiniz alanı seçiniz: """)
                    
                    if duzenleme_alani == "q":
                        break
                    
                    elif duzenleme_alani in ["1", "2", "3"]:
                        yeni_kisiler_listesi = []
                        
                        if duzenleme_alani == "1":
                            kayit_no = kisiler[secim-1][:-1].split("-")[0]
                            ad = input("\nİsim giriniz: ")
                            soyad = kisiler[secim-1][:-1].split("-")[2]
                            tel_no = kisiler[secim-1][:-1].split("-")[3]
                        
                        elif duzenleme_alani == "2":
                            kayit_no = kisiler[secim-1][:-1].split("-")[0]
                            ad = kisiler[secim-1][:-1].split("-")[1]
                            soyad = input("\nSoyisim giriniz: ")
                            tel_no = kisiler[secim-1][:-1].split("-")[3]
                        
                        elif duzenleme_alani == "3":
                            kayit_no = kisiler[secim-1][:-1].split("-")[0]
                            ad = kisiler[secim-1][:-1].split("-")[1]
                            soyad = kisiler[secim-1][:-1].split("-")[2]
                            tel_no = input("\nTelefon numarası giriniz: ")
                        
                        for kisi in kisiler:
                            if kisi == kisiler[secim-1]:
                                yeni_kisi = f"{kayit_no}-{ad}-{soyad}-{tel_no}\n"
                                yeni_kisiler_listesi.append(yeni_kisi)
                            
                            else:    
                                yeni_kisiler_listesi.append(kisi)
                        
                        with open("kisilerim.txt", "w") as dosya:
                            dosya.writelines(yeni_kisiler_listesi)
                        
                        print("\nKayıt düzenlendi..")
                        time.sleep(1.5)
                        break
                    
                    else:
                        print("\nYanlış seçim yaptınız!..")
    
    def kisiGoster(self):
        print("\n<< Menü-4: GÖSTER >>")
        with open("kisilerim.txt", "r") as dosya:
            kisiler = dosya.readlines()
        
        if kisiler:
            while True:
                print()
                
                for kisi in kisiler:
                    print(kisi[:-1].split("-")[0] + ".\t" + kisi[:-1].split("-")[1],
                          kisi[:-1].split("-")[2])
                    print("\t" + kisi[:-1].split("-")[3])
                    print("-" * 20)
                
                if len(kisiler) == 1:
                    mesaj1 = "\nLütfen seçmek için kişinin kayıt numarasını \
giriniz (1 adet kayıt): "
                    mesaj2 = "Lütfen 1 nolu kayıt harici seçim yapmayınız: "
                
                elif len(kisiler) == 2:
                    mesaj1 = "\nLütfen seçmek için kişinin kayıt numarasını \
giriniz (2 adet kayıt): "
                    mesaj2 = "Lütfen 2 kayıt arasından bir seçim yapınız: "
                
                elif len(kisiler) >= 3:
                    mesaj1 = f"\nLütfen seçmek için kişinin kayıt numarasını \
giriniz (1 - {len(kisiler)} arası): "
                    mesaj2 = f"Lütfen 1 - {len(kisiler)} arasında bir seçim \
yapınız: "
                
                mesaj3 = "\nAna menüye dönmek için basınız ==> <q>"
                
                secim = input(mesaj3 + mesaj1)
                
                if secim == "q":
                    break
                
                while not secim.isdigit() or int(secim) < 1 or int(secim) > len(kisiler):
                    secim = input(mesaj2)
                
                secim = int(secim)
                
                print()
                print(kisiler[secim-1][:-1].split("-")[1],
                      kisiler[secim-1][:-1].split("-")[2])
                print(kisiler[secim-1][:-1].split("-")[3])
                
                while True:
                    islem = input("""\n\t1- Arama Yap\n\t2- Mesaj Gönder\n\
\nİPTAL için basınız ==> <q>:\nSeçiminizi giriniz: """)
                    
                    if islem == "q":
                        break
                    
                    elif islem == "1":
                        print()
                        print(kisiler[secim-1][:-1].split("-")[1],
                              kisiler[secim-1][:-1].split("-")[2])
                        print("ARANIYOR..")
                        
                        secim = input("\nİPTAL için basınız ==> <q>: ")
                        
                        if secim == "q":
                            break
                    
                    elif islem == "2":
                        mesaj = input("Lütfen göndermek istediğiniz mesajı \
yazınız:\n>> ")
                        print("\nMESAJ GÖNDERİLDİ..")
                        time.sleep(1)
                        print(f"\nGönderilen mesaj:\n<<<{mesaj}>>>")
                        time.sleep(3)
                        break
                    
                    else:
                        print("\nYanlış seçim yaptınız!..")
        
        else:
            print("\nRehber boşşş!..")
            time.sleep(1.5)
    
    def cikis(self):
        while True:
            print("\n<< Menü-5: ÇIKIŞ >>")
            mesaj1 = "\nÇIKIŞ yapmak istediğinize emin misiniz? (e/h): "
            mesaj2 = "\nİPTAL için basınız ==> <q>"
            
            secim = input(mesaj2 + mesaj1)
            
            if secim == "q":
                break
            
            elif secim in ["e", "E", "evet", "Evet", "EVET"]:
                print("\n<<< Rehber uygulamasından çıkış yapıldı!.. >>>")
                menu.calisma = False
                break
            
            elif secim in ["h", "H", "hayır", "Hayır", "HAYIR"]:
                break
            
            else:
                print("\nYanlış seçim yaptınız!..")

menu = Rehber("Telefon Rehberi")

while menu.calisma:
    menu.program()
    
    if menu.calisma == False:
        break

# OUTPUT:
# >>>
#==================================================
# **** Telefon Rehberi ****
    
#     1- Kişi Ekle
#     2- Kişi Sil
#     3- Kişi Düzenle
#     4- Kişi Göster
#     5- Çıkış

# Seçiminizi giriniz: 2

#==================================================
# << Menü-2: SİL >>

# Silinecek kişi yok!.. (Uyarı 1,5 sn ekranda bekliyor)

#==================================================
# **** Telefon Rehberi ****
    
#     1- Kişi Ekle
#     2- Kişi Sil
#     3- Kişi Düzenle
#     4- Kişi Göster
#     5- Çıkış

# Seçiminizi giriniz: 3

#==================================================
# << Menü-3: DÜZENLE >>

# Düzenlenecek kişi yok!.. (Uyarı 1,5 sn ekranda bekliyor)

#==================================================
# **** Telefon Rehberi ****
    
#     1- Kişi Ekle
#     2- Kişi Sil
#     3- Kişi Düzenle
#     4- Kişi Göster
#     5- Çıkış

# Seçiminizi giriniz: 4

#==================================================
# << Menü-4: GÖSTER >>

# Rehber boşşş!.. (Uyarı 1,5 sn ekranda bekliyor)

#==================================================
# **** Telefon Rehberi ****
    
#     1- Kişi Ekle
#     2- Kişi Sil
#     3- Kişi Düzenle
#     4- Kişi Göster
#     5- Çıkış

# Seçiminizi giriniz: 1

#==================================================
# << Menü-1: EKLE >>

# İsim giriniz: Ali
# Soyisim giriniz: Caliskan
# Telefon numarası giriniz: 505 123 45 67

# Ali Caliskan rehbere kayıt edildi.. (Uyarı 1,5 sn ekranda bekliyor)

#==================================================
# **** Telefon Rehberi ****
    
#     1- Kişi Ekle
#     2- Kişi Sil
#     3- Kişi Düzenle
#     4- Kişi Göster
#     5- Çıkış

# Seçiminizi giriniz: 1

#==================================================
# << Menü-1: EKLE >>

# İsim giriniz: Ayse
# Soyisim giriniz: Yildiz
# Telefon numarası giriniz: 506 123 45 67

# Ayse Yildiz rehbere kayıt edildi.. (Uyarı 1,5 sn ekranda bekliyor)

#==================================================
# **** Telefon Rehberi ****
    
#     1- Kişi Ekle
#     2- Kişi Sil
#     3- Kişi Düzenle
#     4- Kişi Göster
#     5- Çıkış

# Seçiminizi giriniz: 1

#==================================================
# << Menü-1: EKLE >>

# İsim giriniz: Veli
# Soyisim giriniz: Basarili
# Telefon numarası giriniz: 507 123 45 67

# Veli Basarili rehbere kayıt edildi.. (Uyarı 1,5 sn ekranda bekliyor)

#==================================================
# **** Telefon Rehberi ****
    
#     1- Kişi Ekle
#     2- Kişi Sil
#     3- Kişi Düzenle
#     4- Kişi Göster
#     5- Çıkış

# Seçiminizi giriniz: 1

#==================================================
# << Menü-1: EKLE >>

# İsim giriniz: Fatma
# Soyisim giriniz: Yardimsever
# Telefon numarası giriniz: 555 123 45 67

# Fatma Yardimsever rehbere kayıt edildi.. (Uyarı 1,5 sn ekranda bekliyor)

#==================================================
# **** Telefon Rehberi ****
    
#     1- Kişi Ekle
#     2- Kişi Sil
#     3- Kişi Düzenle
#     4- Kişi Göster
#     5- Çıkış

# Seçiminizi giriniz: 2

#==================================================
# << Menü-2: SİL >>

# 1. Ali Caliskan 505 123 45 67
# 2. Ayse Yildiz 506 123 45 67
# 3. Veli Basarili 507 123 45 67
# 4. Fatma Yardimsever 555 123 45 67

# Ana menüye dönmek için basınız ==> <q>
# Lütfen silmek istediğiniz kişinin kayıt numarasını giriniz (1 - 4 arası): q

#==================================================
# **** Telefon Rehberi ****
    
#     1- Kişi Ekle
#     2- Kişi Sil
#     3- Kişi Düzenle
#     4- Kişi Göster
#     5- Çıkış

# Seçiminizi giriniz: 2

#==================================================
# << Menü-2: SİL >>

# 1. Ali Caliskan 505 123 45 67
# 2. Ayse Yildiz 506 123 45 67
# 3. Veli Basarili 507 123 45 67
# 4. Fatma Yardimsever 555 123 45 67

# Ana menüye dönmek için basınız ==> <q>
# Lütfen silmek istediğiniz kişinin kayıt numarasını giriniz (1 - 4 arası): 3

# Veli Basarili kişisi rehberden silinecek!.. !!!

# İPTAL için basınız ==> <q>
# Emin misiniz? (e/h): e

# Veli Basarili rehberden silindi.. (Uyarı 1,5 sn ekranda bekliyor)

#==================================================
# **** Telefon Rehberi ****
    
#     1- Kişi Ekle
#     2- Kişi Sil
#     3- Kişi Düzenle
#     4- Kişi Göster
#     5- Çıkış

# Seçiminizi giriniz: 3

#==================================================
# << Menü-3: DÜZENLE >>

# 1. Ali Caliskan 505 123 45 67
# 2. Ayse Yildiz 506 123 45 67
# 3. Fatma Yardimsever 555 123 45 67

# Ana menüye dönmek için basınız ==> <q>
# Lütfen düzenlemek istediğiniz kişinin kayıt numarasını giriniz (1 - 3 arası): 3

#    1- İsim
#    2- Soyisim
#    3- Telefon no

# İPTAL için basınız ==> <q>
# Lütfen düzenlemek istediğiniz alanı seçiniz: 1

# İsim giriniz: Ahmet

# Kayıt düzenlendi.. (Uyarı 1,5 sn ekranda bekliyor)

#==================================================
# << Menü-3: DÜZENLE >>

# 1. Ali Caliskan 505 123 45 67
# 2. Ayse Yildiz 506 123 45 67
# 3. Ahmet Yardimsever 555 123 45 67

# Ana menüye dönmek için basınız ==> <q>
# Lütfen düzenlemek istediğiniz kişinin kayıt numarasını giriniz (1 - 3 arası): 1

#    1- İsim
#    2- Soyisim
#    3- Telefon no

# İPTAL için basınız ==> <q>
# Lütfen düzenlemek istediğiniz alanı seçiniz: 2

# Soyisim giriniz: Akinci

# Kayıt düzenlendi.. (Uyarı 1,5 sn ekranda bekliyor)

#==================================================
# << Menü-3: DÜZENLE >>

# 1. Ali Akinci 505 123 45 67
# 2. Ayse Yildiz 506 123 45 67
# 3. Ahmet Yardimsever 555 123 45 67

# Ana menüye dönmek için basınız ==> <q>
# Lütfen düzenlemek istediğiniz kişinin kayıt numarasını giriniz (1 - 3 arası): 2

#    1- İsim
#    2- Soyisim
#    3- Telefon no

# İPTAL için basınız ==> <q>
# Lütfen düzenlemek istediğiniz alanı seçiniz: 3

# Telefon numarası giriniz: 532 123 45 67

# Kayıt düzenlendi.. (Uyarı 1,5 sn ekranda bekliyor)

#==================================================
# << Menü-3: DÜZENLE >>

# 1. Ali Akinci 505 123 45 67
# 2. Ayse Yildiz 532 123 45 67
# 3. Ahmet Yardimsever 555 123 45 67

# Ana menüye dönmek için basınız ==> <q>
# Lütfen düzenlemek istediğiniz kişinin kayıt numarasını giriniz (1 - 3 arası): q

#==================================================
# **** Telefon Rehberi ****
    
#     1- Kişi Ekle
#     2- Kişi Sil
#     3- Kişi Düzenle
#     4- Kişi Göster
#     5- Çıkış

# Seçiminizi giriniz: 4

#==================================================
# << Menü-4: GÖSTER >>

# 1.	Ali Akinci
# 	505 123 45 67
# --------------------
# 2.	Ayse Yildiz
# 	532 123 45 67
# --------------------
# 3.	Ahmet Yardimsever
# 	555 123 45 67
# --------------------

# Ana menüye dönmek için basınız ==> <q>
# Lütfen seçmek için kişinin kayıt numarasını giriniz (1 - 3 arası): 1

# Ali Akinci
# 505 123 45 67

# 	1- Arama Yap
# 	2- Mesaj Gönder

# İPTAL için basınız ==> <q>:
# Seçiminizi giriniz: 1

# Ali Akinci
# ARANIYOR..

# İPTAL için basınız ==> <q>: q

# 1.	Ali Akinci
# 	505 123 45 67
# --------------------
# 2.	Ayse Yildiz
# 	532 123 45 67
# --------------------
# 3.	Ahmet Yardimsever
# 	555 123 45 67
# --------------------

# Ana menüye dönmek için basınız ==> <q>
# Lütfen seçmek için kişinin kayıt numarasını giriniz (1 - 3 arası): 2

# Ayse Yildiz
# 532 123 45 67

# 	1- Arama Yap
# 	2- Mesaj Gönder

# İPTAL için basınız ==> <q>:
# Seçiminizi giriniz: 2
# Lütfen göndermek istediğiniz mesajı yazınız:
# >> Merhaba Ayşe, hocanın verdiği ödevi yapabildin mi?

# MESAJ GÖNDERİLDİ.. (Uyarı 1 sn ekranda bekliyor)

# Gönderilen mesaj:
# <<<Merhaba Ayşe, hocanın verdiği ödevi yapabildin mi?>>>
# (Mesaj 3 sn ekranda bekliyor)

# 1.	Ali Akinci
# 	505 123 45 67
# --------------------
# 2.	Ayse Yildiz
# 	532 123 45 67
# --------------------
# 3.	Ahmet Yardimsever
# 	555 123 45 67
# --------------------

# Ana menüye dönmek için basınız ==> <q>
# Lütfen seçmek için kişinin kayıt numarasını giriniz (1 - 3 arası): q

#==================================================
# **** Telefon Rehberi ****
    
#     1- Kişi Ekle
#     2- Kişi Sil
#     3- Kişi Düzenle
#     4- Kişi Göster
#     5- Çıkış

# Seçiminizi giriniz: 5

#==================================================
# << Menü-5: ÇIKIŞ >>

# İPTAL için basınız ==> <q>
# ÇIKIŞ yapmak istediğinize emin misiniz? (e/h): e

# <<< Rehber uygulamasından çıkış yapıldı!.. >>>
