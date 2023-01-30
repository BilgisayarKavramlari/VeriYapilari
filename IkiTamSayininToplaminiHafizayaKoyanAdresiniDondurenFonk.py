# Pointer Class (Gösterici Sınıf)'ı Oluşturma Yöntemiyle

# Pointer sınıfı oluşturma
class Pointer:
    def __init__(self, deger, sonraki=None):
        self.deger = deger
        self.sonraki = sonraki
        self.adres = id(deger)

# Pointerların toplamamının adresini döndürme fonksiyonu oluşturma
def topla(x, y):
    p3 = Pointer(x.deger + y.deger)
    return p3.adres

# İki tane pointer oluşturup tam sayı değerini gösterme
p1 = Pointer(15)
p2 = Pointer(25)

# İki pointerı fonksiyona gönderip değerlerini toplatma ve adresini bastırma
print("p1 ve p2 pointerlarının toplamının hafızadaki adresi:", topla(p1, p2))



# OUTPUT:
# >>> p1 ve p2 pointerlarının toplamının hafızadaki adresi: 1837813034512

# Check:
print(id(40))
# >>> 1837813034512
