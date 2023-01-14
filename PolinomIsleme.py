# Array (Dizi) Sınıfı Oluşturma Yöntemiyle

# Dizi sınıfı oluşturma
class Array(list):
    def __init__(self, size, *args):    # *args: dizi tanımlanırkenki değerleri
        self.size = size

        # Diziyi, başta girilen değerleriyle birlikte tanımlama
        if args:
            if type(args[0]) in [type(list()), type(set()), type(tuple())]:
                if self.size != len(args[0]):
                    print("error: list assignment index out of range")
                    return None
                
                else:
                    for i in args[0]:
                        self.append(i)
            else:
                if self.size != len(args):
                    print("error: list assignment index out of range")
                    return None
                else:
                    for i in args:
                        self.append(i)

        # Diziyi boş tanımlama
        else:
            for i in range(size):
                self.append(None)

    # Diziye boyut harici eleman eklenmesi engelleme
    def append(self, object):
        if len(self) == self.size:
            return "error: request for member ‘append’ in something not a \
structure or union"
        else:
            self += [object]

    # Diziye boyut harici eleman eklenmesi engelleme
    def insert(self, index, object):
        if len(self) == self.size:
            return "error: request for member ‘append’ in something not a \
structure or union"

    # Listeden eleman çıkarma özelliği dizi için engelleme
    def remove(self, value):
        return "error: request for member ‘remove’ in something not a \
structure or union"

    # Listeden eleman çıkarma özelliği dizi için engelleme
    def pop(self, *value):
        return "error: request for member ‘pop’ in something not a \
structure or union"

    # Dizi elemanlarına indis harici erişim ve ekrana bastırma engelleme
    def __str__(self):
        return str(type(self))

    # Dizi elemanlarına indis harici erişim ve ekrana bastırma engelleme
    def __repr__(self):
        return repr(type(self))

# Bir polinomun katsayılarının yer aldığı dizi
a = Array(4, [3, 0, 2, 5])      # 3x^3 + 2x + 5

# Dizinin boyutunu tanımlama
boyut = a.size

# Kullanıcıdan polinomdaki x'in değerini alma
x = int(input("Polinomdaki x değerini giriniz: "))
print()

# Polinomun denklemini ekrana basma
denklem = ""
derece = boyut
for i in range(boyut):
    derece -= 1
    denklem = f"{a[i]}x^{derece}"
    if derece != 0:
        denklem += " + "
    print(denklem, end="")
print()

# Polinomu kullanıcıdan alınan x değerine göre çözme
toplam = 0
derece = boyut
for i in range(boyut):
    derece -= 1
    toplam += (a[i] * (x ** derece))

print("Çözüm:", toplam)

# OUTPUT:
Polinomdaki x değerini giriniz: 2

3x^3 + 0x^2 + 2x^1 + 5x^0
Çözüm: 33

# OUTPUT_2:
Polinomdaki x değerini giriniz: 3

3x^3 + 0x^2 + 2x^1 + 5x^0
Çözüm: 92
