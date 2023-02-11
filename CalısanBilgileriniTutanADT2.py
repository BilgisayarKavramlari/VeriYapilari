# CLASS YÖNTEMİ - 2
# v2: Arama Fonksiyonunda Arama Kriteri Seçeneklerine Göre Kullanıcıdan Anahtar
# Sözcüğü input() ile Alınıyor

# çalışan sınıfının oluşturulması
class Calisan:
    # sınıf özelliği tanımlanması
    personel = []
    
    # nesne özellikleirnin tanımlanması
    def __init__(self, tc_kimlik_no, isim, soyisim, maas, departman):
        self.tc_kimlik_no = tc_kimlik_no
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.departman = departman
    
    # sınıfa yeni nesne ekleme fonksiyonu tanımlanması
    def personelEkle(self):
        
        # yeni nesne eklemeden önce daha önce eklenip eklenmediğinin kontrol
        # edilmesi
        if self.tc_kimlik_no not in [x[0] for x in self.personel]:
            self.personel.append([self.tc_kimlik_no, self.isim, self.soyisim,
                                  self.departman, self.maas])
            print(f"{self.isim} adlı kişi personel olarak eklendi..")
        
        else:
            print(f"{self.isim} adlı kişi daha önceden eklenmiştir!")
    
    # personel listesinin isim - soyisimlerinin ekrana bastırılması
    def personelIsimYazdir(self):
        print("Personel Listesi:")
        
        for i in self.personel:
            print(i[1], i[2])
    
    # personel listesinin isim, soyisim be bülümlerinin ekrana bastırılması
    def personelBolumYazdir(self):
        print("Personel Listesi:")
        
        for i in self.personel:
            print(i[1], i[2], "-", i[3])
    
    # dört kritere göre personel listesinden arama yapılıp ekrana bastırılması
    def personelAra(self):
        print("""Arama kriterini seçiniz;
    1) TC Kimlik No
    2) İsim
    3) Soyisim
    4) Departman
    5) Maaş""")
        secim = int(input("\nLütfen 1 ile 4 arasında bir sayı giriniz: "))
        
        if secim == 1:
            anahtar = input("Lütfen personelin TC Kimlik nosunu giriniz: ")
            
        elif secim == 2:
            anahtar = input("Lütfen personelin ismini giriniz: ")
        
        elif secim == 3:
            anahtar = input("Lütfen personelin soyismini giriniz: ")
        
        elif secim == 4:
            anahtar = input("Lütfen departman ismi giriniz: ")
        
        elif secim == 5:
            anahtar = input("Lütfen maaş giriniz: ")
        
        flag = False
        
        for i in self.personel:
            if anahtar.lower() == i[secim-1].lower():
                print(f"\nTC Kimlik No: {i[0]}\nAdı\t\t\t: {i[1]}\nSoyadı\
\t\t: {i[2]}\nDepartmanı\t: {i[3]}\nMaaşı\t\t: {i[4]}")
                flag = True
        
        if flag == False:
            print("Aranan kriterlere göre sonuç bulunamadı!")

# çalışan sınıfından çalışan1, çalışan2, çalışan3, çalışan4, çalışan5, çalışan6
# nesnelerinin oluşturulması
c1 = Calisan("12345", "Ali", "Çalışkan", "30000", "IT")
c2 = Calisan("23456", "Veli", "Başarılı", "33000", "Satınalma")
c3 = Calisan("34567", "Ayşe", "Yıldız", "35000", "Pazarlama")
c4 = Calisan("45678", "Ali", "Akpak", "27000", "Satış")
c5 = Calisan("56789", "Ömer", "Başarılı", "25000", "Lojistik")
c6 = Calisan("67890", "Fatma", "Balçiçek", "35000", "IT")

print(c1.isim)
# >>> Ali

print(c2.isim)
# >>> Veli

print(c3.isim)
# >>> Ayşe

print()

# çalışan nesnelerinin personel listesine eklenmesi
c1.personelEkle()
# >>> Ali adlı kişi personel olarak eklendi..

c2.personelEkle()
# >>> Veli adlı kişi personel olarak eklendi..

c3.personelEkle()
# >>> Ayşe adlı kişi personel olarak eklendi..

Calisan.personelEkle(c4)
# >>> Ali adlı kişi personel olarak eklendi..

Calisan.personelEkle(c5)
# >>> Ömer adlı kişi personel olarak eklendi..

Calisan.personelEkle(c6)
# >>> Fatma adlı kişi personel olarak eklendi..

print()

# personel listesinin içeriği nesne ve sınıf üzerinden erişilmesi
print(c1.personel)
print(c2.personel)
print(c3.personel)
print(Calisan.personel)

# >>>
# [['12345', 'Ali', 'Çalışkan', 'IT', '30000'],
# ['23456', 'Veli', 'Başarılı', 'Satınalma', '33000'],
# ['34567', 'Ayşe', 'Yıldız', 'Pazarlama', '35000'],
# ['45678', 'Ali', 'Akpak', 'Satış', '27000'],
# ['56789', 'Ömer', 'Başarılı', 'Lojistik', '25000'],
# ['67890', 'Fatma', 'Balçiçek', 'IT', '35000']]

# [['12345', 'Ali', 'Çalışkan', 'IT', '30000'],
# ['23456', 'Veli', 'Başarılı', 'Satınalma', '33000'],
# ['34567', 'Ayşe', 'Yıldız', 'Pazarlama', '35000'],
# ['45678', 'Ali', 'Akpak', 'Satış', '27000'],
# ['56789', 'Ömer', 'Başarılı', 'Lojistik', '25000'],
# ['67890', 'Fatma', 'Balçiçek', 'IT', '35000']]

# [['12345', 'Ali', 'Çalışkan', 'IT', '30000'],
# ['23456', 'Veli', 'Başarılı', 'Satınalma', '33000'],
# ['34567', 'Ayşe', 'Yıldız', 'Pazarlama', '35000'],
# ['45678', 'Ali', 'Akpak', 'Satış', '27000'],
# ['56789', 'Ömer', 'Başarılı', 'Lojistik', '25000'],
# ['67890', 'Fatma', 'Balçiçek', 'IT', '35000']]

# [['12345', 'Ali', 'Çalışkan', 'IT', '30000'],
# ['23456', 'Veli', 'Başarılı', 'Satınalma', '33000'],
# ['34567', 'Ayşe', 'Yıldız', 'Pazarlama', '35000'],
# ['45678', 'Ali', 'Akpak', 'Satış', '27000'],
# ['56789', 'Ömer', 'Başarılı', 'Lojistik', '25000'],
# ['67890', 'Fatma', 'Balçiçek', 'IT', '35000']]

print()

# personel listesi yazdir() methodu ile ekrana bastırılması
c1.personelIsimYazdir()

# >>>
# Personel Listesi:
# Ali Çalışkan
# Veli Başarılı
# Ayşe Yıldız
# Ali Akpak
# Ömer Başarılı
# Fatma Balçiçek

print()

c2.personelIsimYazdir()

# >>>
# Personel Listesi:
# Ali Çalışkan
# Veli Başarılı
# Ayşe Yıldız
# Ali Akpak
# Ömer Başarılı
# Fatma Balçiçek

print()

c3.personelIsimYazdir()

# >>>
# Personel Listesi:
# Ali Çalışkan
# Veli Başarılı
# Ayşe Yıldız
# Ali Akpak
# Ömer Başarılı
# Fatma Balçiçek

print()

Calisan.personelIsimYazdir(c1)

# >>>
# Personel Listesi:
# Ali Çalışkan
# Veli Başarılı
# Ayşe Yıldız
# Ali Akpak
# Ömer Başarılı
# Fatma Balçiçek

print()

Calisan.personelIsimYazdir(c2)

# >>>
# Personel Listesi:
# Ali Çalışkan
# Veli Başarılı
# Ayşe Yıldız
# Ali Akpak
# Ömer Başarılı
# Fatma Balçiçek

print()

Calisan.personelIsimYazdir(c3)

# >>>
# Personel Listesi:
# Ali Çalışkan
# Veli Başarılı
# Ayşe Yıldız
# Ali Akpak
# Ömer Başarılı
# Fatma Balçiçek

print()

c1.personelBolumYazdir()

# >>>
# Personel Listesi:
# Ali Çalışkan - IT
# Veli Başarılı - Satınalma
# Ayşe Yıldız - Pazarlama
# Ali Akpak - Satış
# Ömer Başarılı - Lojistik
# Fatma Balçiçek - IT

print()

c2.personelBolumYazdir()

# >>>
# Personel Listesi:
# Ali Çalışkan - IT
# Veli Başarılı - Satınalma
# Ayşe Yıldız - Pazarlama
# Ali Akpak - Satış
# Ömer Başarılı - Lojistik
# Fatma Balçiçek - IT

print()

c3.personelBolumYazdir()

# >>>
# Personel Listesi:
# Ali Çalışkan - IT
# Veli Başarılı - Satınalma
# Ayşe Yıldız - Pazarlama
# Ali Akpak - Satış
# Ömer Başarılı - Lojistik
# Fatma Balçiçek - IT

print()

Calisan.personelBolumYazdir(c1)

# >>>
# Personel Listesi:
# Ali Çalışkan - IT
# Veli Başarılı - Satınalma
# Ayşe Yıldız - Pazarlama
# Ali Akpak - Satış
# Ömer Başarılı - Lojistik
# Fatma Balçiçek - IT

print()

Calisan.personelBolumYazdir(c2)

# >>>
# Personel Listesi:
# Ali Çalışkan - IT
# Veli Başarılı - Satınalma
# Ayşe Yıldız - Pazarlama
# Ali Akpak - Satış
# Ömer Başarılı - Lojistik
# Fatma Balçiçek - IT

print()

Calisan.personelBolumYazdir(c3)

# >>>
# Personel Listesi:
# Ali Çalışkan - IT
# Veli Başarılı - Satınalma
# Ayşe Yıldız - Pazarlama
# Ali Akpak - Satış
# Ömer Başarılı - Lojistik
# Fatma Balçiçek - IT

print()

# personel sayısının ekrana bastırılması
print("Personel Sayısı:", len(Calisan.personel))
# >>> Personel Sayısı: 6

print()

# personel listesinde nesne arayıp bilgilerine erişilmesi
c1.personelAra()

# >>>
# Arama kriterini seçiniz;
#     1) TC Kimlik No
#     2) İsim
#     3) Soyisim
#     4) Departman
#     5) Maaş

# Lütfen 1 ile 4 arasında bir sayı giriniz: 1
# Lütfen personelin TC Kimlik nosunu giriniz: 123
# Aranan kriterlere göre sonuç bulunamadı!

# >>>
# Arama kriterini seçiniz;
#     1) TC Kimlik No
#     2) İsim
#     3) Soyisim
#     4) Departman
#     5) Maaş

# Lütfen 1 ile 4 arasında bir sayı giriniz: 1
# Lütfen personelin TC Kimlik nosunu giriniz: 12345

# TC Kimlik No  : 12345
# Adı			: Ali
# Soyadı		: Çalışkan
# Departmanı	: IT
# Maaşı         : 30000

print()

c2.personelAra()

# >>>
# Arama kriterini seçiniz;
#     1) TC Kimlik No
#     2) İsim
#     3) Soyisim
#     4) Departman
#     5) Maaş

# Lütfen 1 ile 4 arasında bir sayı giriniz: 2
# Lütfen personelin ismini giriniz: Ayşe

# TC Kimlik No  : 34567
# Adı			: Ayşe
# Soyadı		: Yıldız
# Departmanı	: Pazarlama
# Maaşı         : 35000

print()

c3.personelAra()

# >>>
# Arama kriterini seçiniz;
#     1) TC Kimlik No
#     2) İsim
#     3) Soyisim
#     4) Departman
#     5) Maaş

# Lütfen 1 ile 4 arasında bir sayı giriniz: 2
# Lütfen personelin ismini giriniz: ali

# TC Kimlik No  : 12345
# Adı			: Ali
# Soyadı		: Çalışkan
# Departmanı	: IT
# Maaşı         : 30000

# TC Kimlik No  : 45678
# Adı			: Ali
# Soyadı		: Akpak
# Departmanı	: Satış
# Maaşı         : 27000

print()

Calisan.personelAra(c4)

# >>>
# Arama kriterini seçiniz;
#     1) TC Kimlik No
#     2) İsim
#     3) Soyisim
#     4) Departman
#     5) Maaş

# Lütfen 1 ile 4 arasında bir sayı giriniz: 3
# Lütfen personelin soyismini giriniz: balçiçek

# TC Kimlik No  : 67890
# Adı			: Fatma
# Soyadı		: Balçiçek
# Departmanı	: IT
# Maaşı         : 35000

print()

Calisan.personelAra(c5)

# >>>
# Arama kriterini seçiniz;
#     1) TC Kimlik No
#     2) İsim
#     3) Soyisim
#     4) Departman
#     5) Maaş

# Lütfen 1 ile 4 arasında bir sayı giriniz: 3
# Lütfen personelin soyismini giriniz: Başarılı

# TC Kimlik No  : 23456
# Adı			: Veli
# Soyadı		: Başarılı
# Departmanı	: Satınalma
# Maaşı         : 33000

# TC Kimlik No  : 56789
# Adı			: Ömer
# Soyadı		: Başarılı
# Departmanı	: Lojistik
# Maaşı         : 25000

print()

Calisan.personelAra(c6)

# >>>
# Arama kriterini seçiniz;
#     1) TC Kimlik No
#     2) İsim
#     3) Soyisim
#     4) Departman
#     5) Maaş

# Lütfen 1 ile 4 arasında bir sayı giriniz: 4
# Lütfen departman ismi giriniz: it

# TC Kimlik No  : 12345
# Adı			: Ali
# Soyadı		: Çalışkan
# Departmanı	: IT
# Maaşı         : 30000

# TC Kimlik No  : 67890
# Adı			: Fatma
# Soyadı		: Balçiçek
# Departmanı	: IT
# Maaşı         : 35000

print()

c1.personelAra()

# >>>
# Arama kriterini seçiniz;
#     1) TC Kimlik No
#     2) İsim
#     3) Soyisim
#     4) Departman
#     5) Maaş

# Lütfen 1 ile 4 arasında bir sayı giriniz: 4
# Lütfen departman ismi giriniz: lojistik

# TC Kimlik No  : 56789
# Adı			: Ömer
# Soyadı		: Başarılı
# Departmanı	: Lojistik
# Maaşı         : 25000

print()

c1.personelAra()

# >>>
# Arama kriterini seçiniz;
#     1) TC Kimlik No
#     2) İsim
#     3) Soyisim
#     4) Departman
#     5) Maaş

# Lütfen 1 ile 4 arasında bir sayı giriniz: 5
# Lütfen maaş giriniz: 33000

# TC Kimlik No  : 23456
# Adı			: Veli
# Soyadı		: Başarılı
# Departmanı	: Satınalma
# Maaşı         : 33000

print()

c1.personelAra()

# >>>
# Arama kriterini seçiniz;
#     1) TC Kimlik No
#     2) İsim
#     3) Soyisim
#     4) Departman
#     5) Maaş

# Lütfen 1 ile 4 arasında bir sayı giriniz: 5
# Lütfen maaş giriniz: 35000

# TC Kimlik No  : 34567
# Adı			: Ayşe
# Soyadı		: Yıldız
# Departmanı	: Pazarlama
# Maaşı         : 35000

# TC Kimlik No  : 67890
# Adı			: Fatma
# Soyadı		: Balçiçek
# Departmanı	: IT
# Maaşı         : 35000
