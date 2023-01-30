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

# Birinci polinomun katsayılarının yer aldığı dizi
a = Array(3, [5, 0, 3])      # 5x^2 + 0x + 3

# İkinci polinomun katsayılarının yer aldığı dizi
b = Array(4, [2, 2, 0, 3])      # 2x^3 + 2x^2 + 0x + 3

# 10x^5 + 10x^4 + 15x^2 + 6x^3 + 6x^2 + 0x + 9
# 10x^5 + 10x^4 + 6x^3 + 21x^2 + 0x + 9
# 10 10 6 21 0 9

# a ve b polinomlarının çarpımının yer aldığı boş dizi
c = Array(6)

# Dizilerin boyutunu tanımlama
boyut_a = a.size
boyut_b = b.size

# Çözüm:

# İki polinomu çarpma, çarpım sonucu oluşan denklemin katsayılarını ve 
# derecelerini bir listeye ekleme
denklem = []
derece_a = boyut_a
for i in range(boyut_a):
    derece_a -= 1
    derece_b = boyut_b
    
    for j in range(boyut_b):
        derece_b -= 1
        
        if (a[i] * b[j] != 0) or (a[i] + b[j] == 0):
            if a[i] + b[j] == 0:
                denklem.append([(a[i] * b[j]), (derece_a)])
            else:
                denklem.append([(a[i] * b[j]), (derece_a + derece_b)])

# Denklemin katsayılarını başka listeye aktarıp ekrana basma
sonuc = []

for i in denklem:
    sonuc.append(i[0])

print(*sonuc)

# OUTPUT:
# 10 10 15 0 6 6 9
