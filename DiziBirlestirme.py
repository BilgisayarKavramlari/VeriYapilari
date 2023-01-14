# Array (Dizi) Sınıfı Oluşturma Yöntemiyle

# Dizi sınıfı oluşturma
class Array(list):
    def __init__(self, size, *args):    # *args: dizi tanımlanırkenki değerleri
        self.size = size

        # Diziyi, başta girilen değerleriyle birlikte tanımlama
        if args:
            if type(args[0]) in [type(list()), type(set()), type(tuple())]:
                for i in args[0]:
                    self.append(i)
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

# Dizi boyutu 3 olan örnek bir dizi oluşturma
a = Array(3, [1, 2, 3])

# Dizi boyutu 4 olan örnek başka bir dizi oluşturma
b = Array(4, [6, 7, 8, 9])

# a ve b dizisinin elemanları toplamı kadar boş dizi oluşturma (3 + 4 = 7 boyutlu)
c = Array(7)

# Önce a dizisini c dizisine ekleme
for i in range(3):
    c[i] = a[i]

# Sonra b dizisini c dizisine ekleme (a dizisi elemanlarının en son eklendiği
# yerden eklemeye başlanacak)
for i in range(3, 7):
    c[i] = b[i-3]    # b dizisinin ilk indisinden başlamak için i'den 3 çıkartılacak

# a dizisini ekrana basma
print("\nA:", end=" ")

for i in range(3):
    print(a[i], end=" ")
print()

# b dizisini ekrana basma
print("\nB:", end=" ")

for i in range(4):
    print(b[i], end=" ")
print()

# c dizisini ekrana basma
print("\nC:", end=" ")

for i in range(7):
    print(c[i], end=" ")
print()

# OUTPUT:
A: 1 2 3 

B: 6 7 8 9 

C: 1 2 3 6 7 8 9 
