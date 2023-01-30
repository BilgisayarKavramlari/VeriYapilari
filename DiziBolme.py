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

# Dizi boyutu 9 olan örnek bir dizi oluşturma
a = Array(9, [3, 5, 7, 9, 11, 13, 15, 17, 19])

# Kullanıcıdan diziyi ikiye bölünecek eleman indisini alma
n = int(input("Boyutu 9 olan bir dizi kaçıncı elemandan bölünsün?: "))

# Dizi boyutu (n) olan boş bir dizi oluşturma
b = Array(n)

# Dizi boyutu (9 - n) olan boş bir dizi oluşturma
c = Array(9 - n)

# Önce a dizisinin ilk (n) elemanını b dizisine ekleme
for i in range(n):
    b[i] = a[i]

# Sonra b dizisinin ilk (9 - n) elemanını c dizisine ekleme
for i in range(n, 9):
    c[i-n] = a[i]    # b dizisinin ilk indisinden başlamak için i'den 3 çıkartılacak

# a dizisini ekrana basma
print("\nA:", end=" ")

for i in range(9):
    print(a[i], end=" ")
print()

# b dizisini ekrana basma
print("\nB:", end=" ")

for i in range(n):
    print(b[i], end=" ")
print()

# c dizisini ekrana basma
print("\nC:", end=" ")

for i in range(9 - n):
    print(c[i], end=" ")
print()

# OUTPUT:
Boyutu 9 olan bir dizi kaçıncı elemandan bölünsün?: 3

A: 3 5 7 9 11 13 15 17 19 

B: 3 5 7 

C: 9 11 13 15 17 19 
