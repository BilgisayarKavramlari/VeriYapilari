# DICTIONARY (SÖZLÜK) YÖNTEMİ

# v2: Arama fonksiyonu tek parametre alıyor

# çalışan isimli bir sözlük listesi oluşturulması
calisan = {"ç1": {"tc_kimlik_no": "12345",
                  "isim"        : "Ali",
                  "soyisim"     : "Çalışkan",
                  "maas"        : "30000",
                  "departman"   : "IT"},
           
           "ç2": {"tc_kimlik_no": "23456",
                  "isim"        : "Veli",
                  "soyisim"     : "Başarılı",
                  "maas"        : "33000",
                  "departman"   : "Satınalma"},
           
           "ç3": {"tc_kimlik_no": "34567",
                  "isim"        : "Ayşe",
                  "soyisim"     : "Yıldız",
                  "maas"        : "35000",
                  "departman"   : "Pazarlama"}}

# listeye yeni öğe ekleme fonksiyonu tanımlanması
def personelEkle(tc_kimlik_no, isim, soyisim, maas, departman):
    liste = []

    for i in calisan.values():
        for j in i.values():
            liste.append(j)
    
    if tc_kimlik_no not in liste:
        yeni_calisan = "ç" + str(len(calisan) + 1)
        calisan[yeni_calisan] = {}
        
        calisan[yeni_calisan]["tc_kimlik_no"] = tc_kimlik_no
        calisan[yeni_calisan]["isim"] = isim
        calisan[yeni_calisan]["soyisim"] = soyisim
        calisan[yeni_calisan]["maas"] = maas
        calisan[yeni_calisan]["departman"] = departman
        
        print(f"{isim} adlı kişi personel olarak eklendi..")
    
    else:
        print(f"{isim} adlı kişi daha önceden eklenmiştir!")

# ekrana bastırma fonksiyonu tanımlanması
def personelYazdir():
    print("Personel Listesi:\n")
    
    for i in calisan.values():
        for j in i.values():
            print(j, end=" ")
        print()

# arama fonksiyonu tanımlanması
def personelAra(deger):
    flag = False
    
    for i in calisan.values():
        for j in i.values():
            if j.lower() == deger.lower():
                print(f"TC Kimlik No: {i['tc_kimlik_no']}\nAdı\t\t\t: {i['isim']}\
\nSoyadı\t\t: {i['soyisim']}\nDepartmanı\t: {i['departman']}\nMaaşı\t\t: \
{i['maas']}\n")
                flag = True
    
    if flag == False:
        print("Aranan kriterlere göre sonuç bulunamadı!")

# yeni çalışan eklenmesi
# personelEkle(tc_kimlik_no, isim, soyisim, maas, departman)
personelEkle("45678", "Ali", "Akpak", "27000", "Satış")
# >>> Ali adlı kişi personel olarak eklendi..

personelEkle("56789", "Ömer", "Başarılı", "25000", "Lojistik")
# >>> Ömer adlı kişi personel olarak eklendi..

personelEkle("67890", "Fatma", "Balçiçek", "35000", "IT")
# Fatma adlı kişi personel olarak eklendi..

# daha önce eklenmiş çalışan tekrar ekleme denemesi
personelEkle("45678", "Ali", "Akpak", "27000", "Satış")
# >>> Ali adlı kişi daha önceden eklenmiştir!

# çalışan listesinin ekrana bastırılması
personelYazdir()

# >>>
# Personel Listesi:
    
# 12345 Ali Çalışkan 30000 IT 
# 23456 Veli Başarılı 33000 Satınalma 
# 34567 Ayşe Yıldız 35000 Pazarlama 
# 45678 Ali Akpak 27000 Satış 
# 56789 Ömer Başarılı 25000 Lojistik 
# 67890 Fatma Balçiçek 35000 IT 

print()

# personel sayısının ekrana bastırılması
print("Personel Sayısı:", len(calisan))
# >>> Personel Sayısı: 6

print()

# personel listesinde çalışan arayıp bilgilerine erişilmesi
personelAra("12345")

# >>>
# TC Kimlik No  : 12345
# Adı			: Ali
# Soyadı		: Çalışkan
# Departmanı	: IT
# Maaşı         : 30000

print()

personelAra("123")

# >>> Aranan kriterlere göre sonuç bulunamadı!

print()

personelAra("Ayşe")

# >>>
# TC Kimlik No  : 34567
# Adı			: Ayşe
# Soyadı		: Yıldız
# Departmanı	: Pazarlama
# Maaşı         : 35000

print()

personelAra("ali")

# >>>
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

personelAra("balçiçek")

# >>>
# TC Kimlik No  : 67890
# Adı			: Fatma
# Soyadı		: Balçiçek
# Departmanı	: IT
# Maaşı         : 35000

print()

personelAra("Başarılı")

# >>>
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

personelAra("it")

# >>>
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

personelAra("lojistik")

# >>>
# TC Kimlik No  : 56789
# Adı			: Ömer
# Soyadı		: Başarılı
# Departmanı	: Lojistik
# Maaşı         : 25000

print()

personelAra("33000")

# >>>
# TC Kimlik No  : 23456
# Adı			: Veli
# Soyadı		: Başarılı
# Departmanı	: Satınalma
# Maaşı         : 33000

print()

personelAra("35000")

# >>>
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
