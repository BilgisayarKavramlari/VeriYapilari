class Departman:
    sirket = "Türk Telekom A.Ş."
    departmanlar = []
    yoneticiler = []
    
    def __init__(self, isim, no, butce, yonetici):
        self.isim = isim
        self.no = no
        self.butce = butce
        self.yonetici = yonetici
        
        self.departmanlar.append(self.isim)
        self.yoneticiler.append(self.yonetici)
    
    def departmanInfo(self):
        print(f"Departman İsmi\t\t: {self.isim}\nDepartman Numarası\t: {self.no}\
\nDepartman Bütçesi\t: {self.butce}\nDepartman Yöneticisi: {self.yonetici}")

d1 = Departman("CEO", "01", 1000000, "Ümit Önal")
d2 = Departman("Finans", "02", 100000, "Kaan Aktan")
d3 = Departman("Satınalma", "03", 100000, "Mehmet Beytur")
d4 = Departman("Satış", "04", 100000, "İsmail Bütün")
d5 = Departman("Hukuk", "05", 100000, "Tahsin Kaplan")
d6 = Departman("Teknoloji", "06", 300000, "Yusuf Kıraç")
d7 = Departman("Pazarlama", "07", 200000, "Zeynep Özden")
d8 = Departman("İK", "08", 100000, "Mehmet Emre Vural")

# OUTPUT:

Departman.sirket
# >>> 'Türk Telekom A.Ş.'

Departman.departmanlar
# >>> ['CEO', 'Finans', 'Satınalma', 'Satış', 'Hukuk', 'Teknoloji', 'Pazarlama',
# 'İK']

Departman.yoneticiler
# >>> ['Ümit Önal', 'Kaan Aktan', 'Mehmet Beytur', 'İsmail Bütün',
# 'Tahsin Kaplan', 'Yusuf Kıraç', 'Zeynep Özden', 'Mehmet Emre Vural']

d1.departmanInfo()
# >>>
# Departman İsmi		: CEO
# Departman Numarası	: 01
# Departman Bütçesi	: 1000000
# Departman Yöneticisi: Ümit Önal

d3.departmanInfo()
# >>>
# Departman İsmi		: Satınalma
# Departman Numarası	: 03
# Departman Bütçesi	: 100000
# Departman Yöneticisi: Mehmet Beytur
