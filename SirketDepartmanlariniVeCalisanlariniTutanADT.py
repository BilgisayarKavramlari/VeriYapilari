class Sirket:
    def __init__(self, unvan, yonetici):
        self.unvan = unvan
        self.yonetici = yonetici
        self.butce = 0        
        self.departmanlar = []
        self.personel = []
    
    def departmanEkle(self, departman_isim, departman_no, departman_butce,
                 departman_yonetici):
        if departman_isim.lower() not in [x[0].lower() for x in self.departmanlar]:
            self.departmanlar.append([departman_isim, departman_no,
                                     departman_butce, departman_yonetici])
            print(f"{departman_isim} departmanı oluşturuldu..")
            self.butce += departman_butce
        
        else:
            print(f"{departman_isim} adlı departman daha önceden \
oluşturulmuştur!")
    
    def departmanAra(self, departman_isim):
        flag = False
        
        for i in self.departmanlar:
            if departman_isim.lower() == i[0].lower():
                print(f"Departmanın ismi\t\t: {i[0]}\nDepartmanın numarası\t: \
{i[1]}\nDepartmanın bütçesi\t\t: {i[2]}\nDepartmanın yöneticisi\t: {i[3]}\n")
                flag = True
        
        if flag == False:
            print("Aranan kriterlere göre sonuç bulunamadı!")
    
    def departmanYazdir(self):
        print("Departmanlar:\n")
        
        for i in self.departmanlar:
            print(f"Departmanın ismi\t\t: {i[0]}\nDepartmanın numarası\t: \
{i[1]}\nDepartmanın bütçesi\t\t: {i[2]}\nDepartmanın yöneticisi\t: {i[3]}\n")
    
    def calisanEkle(self, tc_kimlik_no, calisan_isim, calisan_soyisim,
                    calisan_maas, calisan_departman):
        if tc_kimlik_no not in [x[0] for x in self.personel]:
            self.personel.append([tc_kimlik_no, calisan_isim, calisan_soyisim,
                                  calisan_departman, calisan_maas])
            print(f"{calisan_isim} adlı kişi personel olarak eklendi..")
        
        else:
            print(f"{calisan_isim} adlı kişi daha önceden eklenmiştir!")
    
    def calisanAra(self, anahtar, deger):
        flag = False
        
        for i in self.personel:
            if anahtar == "tc_kimlik_no":
                if deger.lower() == i[0].lower():
                    print(f"TC Kimlik No: {i[0]}\nAdı\t\t\t: {i[1]}\nSoyadı\
\t\t: {i[2]}\nDepartmanı\t: {i[3]}\nMaaşı\t\t: {i[4]}\n")
                    flag = True
            
            elif anahtar == "isim":
                if deger.lower() == i[1].lower():
                    print(f"TC Kimlik No: {i[0]}\nAdı\t\t\t: {i[1]}\nSoyadı\
\t\t: {i[2]}\nDepartmanı\t: {i[3]}\nMaaşı\t\t: {i[4]}\n")
                    flag = True
            
            elif anahtar == "soyisim":
                if deger.lower() == i[2].lower():
                    print(f"TC Kimlik No: {i[0]}\nAdı\t\t\t: {i[1]}\nSoyadı\
\t\t: {i[2]}\nDepartmanı\t: {i[3]}\nMaaşı\t\t: {i[4]}\n")
                    flag = True
            
            elif anahtar == "departman":
                if deger.lower() == i[3].lower():
                    print(f"TC Kimlik No: {i[0]}\nAdı\t\t\t: {i[1]}\nSoyadı\
\t\t: {i[2]}\nDepartmanı\t: {i[3]}\nMaaşı\t\t: {i[4]}\n")
                    flag = True
            
            elif anahtar == "maas":
                if deger.lower() == i[4].lower():
                    print(f"TC Kimlik No: {i[0]}\nAdı\t\t\t: {i[1]}\nSoyadı\
\t\t: {i[2]}\nDepartmanı\t: {i[3]}\nMaaşı\t\t: {i[4]}\n")
                    flag = True
        
        if flag == False:
            print("Aranan kriterlere göre sonuç bulunamadı!")
    
    def calisanYazdir(self):
        print("Personel Listesi:\n")
        
        for i in self.personel:
            print(f"TC Kimlik No: {i[0]}\nAdı\t\t\t: {i[1]}\nSoyadı\
\t\t: {i[2]}\nDepartmanı\t: {i[3]}\nMaaşı\t\t: {i[4]}\n")

# OUTPUT:

s = Sirket("Türk Telekom A.Ş.", "Ümit Önal")

s.unvan
# >>> 'Türk Telekom A.Ş.'

s.yonetici
# >>> 'Ümit Önal'

s.butce
# >>> 0

s.departmanlar
# >>> []

s.personel
# >>> []

s.departmanEkle("CEO", "01", 1000000, "Ümit Önal")
s.departmanEkle("Finans", "02", 100000, "Kaan Aktan")
s.departmanEkle("Satınalma", "03", 100000, "Mehmet Beytur")
s.departmanEkle("Satış", "04", 100000, "İsmail Bütün")
s.departmanEkle("Hukuk", "05", 100000, "Tahsin Kaplan")
s.departmanEkle("Teknoloji", "06", 300000, "Yusuf Kıraç")
s.departmanEkle("Pazarlama", "07", 200000, "Zeynep Özden")
s.departmanEkle("İK", "08", 100000, "Mehmet Emre Vural")

# >>>
# CEO departmanı oluşturuldu..
# Finans departmanı oluşturuldu..
# Satınalma departmanı oluşturuldu..
# Satış departmanı oluşturuldu..
# Hukuk departmanı oluşturuldu..
# Teknoloji departmanı oluşturuldu..
# Pazarlama departmanı oluşturuldu..
# İK departmanı oluşturuldu..

s.departmanEkle("Finans", "02", 100000, "Kaan Aktan")
# >>> Finans adlı departman daha önceden oluşturulmuştur!

s.departmanEkle("Satış", "04", 100000, "İsmail Bütün")
# >>> Satış adlı departman daha önceden oluşturulmuştur!

s.departmanEkle("Teknoloji", "06", 300000, "Yusuf Kıraç")
# >>> Teknoloji adlı departman daha önceden oluşturulmuştur!

s.departmanAra("Denetim")
# >>> Aranan kriterlere göre sonuç bulunamadı!

s.departmanAra("Satınalma")
# >>>
# Departmanın ismi		    : Satınalma
# Departmanın numarası	  : 03
# Departmanın bütçesi		  : 100000
# Departmanın yöneticisi	: Mehmet Beytur

s.departmanAra("Teknoloji")
# >>> 
# Departmanın ismi		: Teknoloji
# Departmanın numarası	: 06
# Departmanın bütçesi		: 300000
# Departmanın yöneticisi	: Yusuf Kıraç

s.departmanAra("satis")
# >>> Aranan kriterlere göre sonuç bulunamadı!

s.departmanAra("satış")
# >>>
# Departmanın ismi		: Satış
# Departmanın numarası	: 04
# Departmanın bütçesi		: 100000
# Departmanın yöneticisi	: İsmail Bütün

s.departmanlar
# >>>
# [['CEO', '01', 1000000, 'Ümit Önal'],
#  ['Finans', '02', 100000, 'Kaan Aktan'],
#  ['Satınalma', '03', 100000, 'Mehmet Beytur'],
#  ['Satış', '04', 100000, 'İsmail Bütün'],
#  ['Hukuk', '05', 100000, 'Tahsin Kaplan'],
#  ['Teknoloji', '06', 300000, 'Yusuf Kıraç'],
#  ['Pazarlama', '07', 200000, 'Zeynep Özden'],
#  ['İK', '08', 100000, 'Mehmet Emre Vural']]

s.departmanYazdir()
# >>>
# Departmanlar:

# Departmanın ismi		: CEO
# Departmanın numarası	: 01
# Departmanın bütçesi		: 1000000
# Departmanın yöneticisi	: Ümit Önal

# Departmanın ismi		: Finans
# Departmanın numarası	: 02
# Departmanın bütçesi		: 100000
# Departmanın yöneticisi	: Kaan Aktan

# Departmanın ismi		: Satınalma
# Departmanın numarası	: 03
# Departmanın bütçesi		: 100000
# Departmanın yöneticisi	: Mehmet Beytur

# Departmanın ismi		: Satış
# Departmanın numarası	: 04
# Departmanın bütçesi		: 100000
# Departmanın yöneticisi	: İsmail Bütün

# Departmanın ismi		: Hukuk
# Departmanın numarası	: 05
# Departmanın bütçesi		: 100000
# Departmanın yöneticisi	: Tahsin Kaplan

# Departmanın ismi		: Teknoloji
# Departmanın numarası	: 06
# Departmanın bütçesi		: 300000
# Departmanın yöneticisi	: Yusuf Kıraç

# Departmanın ismi		: Pazarlama
# Departmanın numarası	: 07
# Departmanın bütçesi		: 200000
# Departmanın yöneticisi	: Zeynep Özden

# Departmanın ismi		: İK
# Departmanın numarası	: 08
# Departmanın bütçesi		: 100000
# Departmanın yöneticisi	: Mehmet Emre Vural

s.butce
# >>> 2000000

s.calisanEkle("12345", "Ali", "Çalışkan", "30000", "Teknoloji")
s.calisanEkle("23456", "Veli", "Başarılı", "33000", "Satınalma")
s.calisanEkle("34567", "Ayşe", "Yıldız", "35000", "Pazarlama")
s.calisanEkle("45678", "Ali", "Akpak", "27000", "Satış")
s.calisanEkle("56789", "Ömer", "Başarılı", "25000", "Finans")
s.calisanEkle("67890", "Fatma", "Balçiçek", "35000", "Teknoloji")

# >>>
# Ali adlı kişi personel olarak eklendi..
# Veli adlı kişi personel olarak eklendi..
# Ayşe adlı kişi personel olarak eklendi..
# Ali adlı kişi personel olarak eklendi..
# Ömer adlı kişi personel olarak eklendi..
# Fatma adlı kişi personel olarak eklendi..

s.calisanEkle("12345", "Ali", "Çalışkan", "30000", "Teknoloji")
# >>> Ali adlı kişi daha önceden eklenmiştir!

s.calisanEkle("34567", "Ayşe", "Yıldız", "35000", "Pazarlama")
# >>> Ayşe adlı kişi daha önceden eklenmiştir!

s.calisanAra("tc_kimlik_no", "56789")
# >>>
# TC Kimlik No  : 56789
# Adı			    : Ömer
# Soyadı		  : Başarılı
# Departmanı	: Lojistik
# Maaşı       : 25000

s.calisanAra("isim", "ali")
# >>>
# TC Kimlik No: 12345
# Adı			: Ali
# Soyadı		: Çalışkan
# Departmanı	: Teknoloji
# Maaşı		: 30000

# TC Kimlik No: 45678
# Adı			: Ali
# Soyadı		: Akpak
# Departmanı	: Satış
# Maaşı		: 27000

s.calisanAra("departman", "teknoloji")
# >>>
# TC Kimlik No  : 12345
# Adı           : Ali
# Soyadı        : Çalışkan
# Departmanı    : IT
# Maaşı         : 30000

# TC Kimlik No  : 67890
# Adı           : Fatma
# Soyadı        : Balçiçek
# Departmanı    : IT
# Maaşı         : 35000

s.personel
# >>>
# [['12345', 'Ali', 'Çalışkan', 'Teknoloji', '30000'],
#  ['23456', 'Veli', 'Başarılı', 'Satınalma', '33000'],
#  ['34567', 'Ayşe', 'Yıldız', 'Pazarlama', '35000'],
#  ['45678', 'Ali', 'Akpak', 'Satış', '27000'],
#  ['56789', 'Ömer', 'Başarılı', 'Lojistik', '25000'],
#  ['67890', 'Fatma', 'Balçiçek', 'Teknoloji', '35000']]

s.calisanYazdir()
# >>>
# Personel Listesi:

# TC Kimlik No: 12345
# Adı			: Ali
# Soyadı		: Çalışkan
# Departmanı	: Teknoloji
# Maaşı		: 30000

# TC Kimlik No: 23456
# Adı			: Veli
# Soyadı		: Başarılı
# Departmanı	: Satınalma
# Maaşı		: 33000

# TC Kimlik No: 34567
# Adı			: Ayşe
# Soyadı		: Yıldız
# Departmanı	: Pazarlama
# Maaşı		: 35000

# TC Kimlik No: 45678
# Adı			: Ali
# Soyadı		: Akpak
# Departmanı	: Satış
# Maaşı		: 27000

# TC Kimlik No: 56789
# Adı			: Ömer
# Soyadı		: Başarılı
# Departmanı	: Finans
# Maaşı		: 25000

# TC Kimlik No: 67890
# Adı			: Fatma
# Soyadı		: Balçiçek
# Departmanı	: Teknoloji
# Maaşı		: 35000
