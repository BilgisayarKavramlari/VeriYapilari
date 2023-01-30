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

# Örnek iki karmaşık sayı tanımlama
a = Array(2, [3, "2i"])
b = Array(2, [4, "5i"])

# İki karmaşık sayıyı toplama
c = Array(2)

c[0] = a[0] + b[0]
c[1] = str(int(a[1][0]) + int(b[1][0])) + "i"

# Ekrana bastırma
print(f"({a[0]} + {a[1]}) + ({b[0]} + {b[1]}) = {c[0]} + {c[1]}")

# OUTPUT:
(3 + 2i) + (4 + 5i) = 7 + 7i
