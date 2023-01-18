# Dizi Sınıfı Oluşturma (Array Class)
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

# MxN boyutunda dizi tanımlama (3x5 iki boyutlu dizi)
a = Array(3, [[1, 3, 5, 7, 9],
              [0, 2, 4, 6, 8],
              [1, 2, 3, 5, 7]])

m = 5
n = 3

# İki boyutlu (3 satırlı, 5 sütunlu) diziyi ekrana bastırma (3x5)
print("2 boyutlu A dizisi (3x5):")
for i in range(n):
    for j in range(m):
        print(a[i][j], end=" ")
    print()
print()

# M boyutunda N tane boş dizi tanımlama (M = 5, N = 3)
a1 = Array(5)
a2 = Array(5)
a3 = Array(5)

# İki boyutlu A dizisinin 3 farklı diziye bölünmesi
for i in range(m):      # 1. dizi
    a1[i] = a[0][i]

for i in range(m):      # 2. dizi
    a2[i] = a[1][i]

for i in range(m):
    a3[i] = a[2][i]

# Bölünen N tane diziyi ekrana basma
print("1. dizi:", end=" ")
for i in range(m):
    print(a1[i], end=" ")
print()

print("2. dizi:", end=" ")
for i in range(m):
    print(a2[i], end=" ")
print()

print("3. dizi:", end=" ")
for i in range(m):
    print(a3[i], end=" ")
print()

# OUTPUT:
2 boyutlu A dizisi (3x5):
1 3 5 7 9 
0 2 4 6 8 
1 2 3 5 7 

1. dizi: 1 3 5 7 9 
2. dizi: 0 2 4 6 8 
3. dizi: 1 2 3 5 7 
