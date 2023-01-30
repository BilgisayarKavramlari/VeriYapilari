# Pointer Class (Gösterici Sınıf)'ı Oluşturma Yöntemiyle

# Pointer sınıfı oluşturma
class Pointer:
    def __init__(self, deger, sonraki=None):
        self.deger = deger
        self.sonraki = sonraki
        self.adres = id(deger)

# Pointerları toplama fonksiyonu oluşturma
def topla(x, y):
    return x.deger + y.deger

# İki tane pointer oluşturup tam sayı değerini gösterme
p1 = Pointer(15)
p2 = Pointer(25)

# İki pointerı fonksiyona gönderip değerlerini toplatma
print(topla(p1, p2))

# OUTPUT:
40
