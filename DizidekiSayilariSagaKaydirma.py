# 1-) Liste Yöntemiyle

# Kullanıcıdan diziyi sağa doğru kaydırılacak sayı istenir:
n = int(input("Dizideki sayılar ne kadar sağa doğru kaydırılacak?: "))

# Örnek dizi tanımlanır
dizi = [3, 5, 7, 9, 11, 13, 15]     # dizi boyutu: 7

# Dizi boyutu artırılmadan önce bir değişkene atanır
size = len(dizi)

# Dizinin ilk hali yazdırılır
print("\nDizinin ilk durumu:")
for i in range(size):
    print(f"dizi[{i}] = ", dizi[i])


# Dizi boyutu değiştirilir (kullanıcıdan girilen sayı kadar artırılır)
for i in range(n):      # dizi boyutu: (7 + n)
    dizi.append(None)

# Dizi elemanları tek tek sağa doğru kaydırılır
for i in range(size-1, -1, -1):     # Kaydırma dizinin son elemanından başlanır
    dizi[i+n] = dizi[i]
    dizi[i] = None

# Dizinin son hali yazdırılır
print("\nDizinin sağa kaydırıldıktan sonraki durumu:")
for i in range(size):
    print(f"dizi[{i+n}] = ", dizi[i+n])

# OUTPUT:
Dizideki sayılar ne kadar sağa doğru kaydırılacak?: 5

Dizinin ilk durumu:
dizi[0] =  3
dizi[1] =  5
dizi[2] =  7
dizi[3] =  9
dizi[4] =  11
dizi[5] =  13
dizi[6] =  15

Dizinin sağa kaydırıldıktan sonraki durumu:
dizi[5] =  3
dizi[6] =  5
dizi[7] =  7
dizi[8] =  9
dizi[9] =  11
dizi[10] =  13
dizi[11] =  15


# 2-) Array (Dizi) Sınıfı Oluşturma Yöntemiyle

# Dizi sınıfı oluşturulur
class Array(list):
    def __init__(self, size, *args):    # *args: dizi tanımlanırkenki değerleri
        self.size = size
        
        # Dizi, başta girilen değerleriyle birlikte tanımlanır
        if args:
            if type(args[0]) == type(list()):
                for i in args[0]:
                    self.append(i)
            else:
                for i in args:
                    self.append(i)
        
        # Dizi boş tanımlanır
        else:
            for i in range(size):
                self.append(None)
    
    # Diziye boyut harici eleman eklenmesi engellenir
    def append(self, object):
        if len(self) == self.size:
            return "error: request for member ‘append’ in something not a \
structure or union"
        else:
            self += [object]
    
    # Diziye boyut harici eleman eklenmesi engellenir
    def insert(self, index, object):
        if len(self) == self.size:
            return "error: request for member ‘insert’ in something not a \
structure or union"
    
    # Listeden eleman çıkarma özelliği dizi için engellenir
    def remove(self, value):
        return "error: request for member ‘remove’ in something not a \
structure or union"
    
    # Listeden eleman çıkarma özelliği dizi için engellenir
    def pop(self, *value):
        return "error: request for member ‘pop’ in something not a \
structure or union"
    
    # Dizi elemanlarına indis harici erişim ve ekrana bastırma engellenir
    def __str__(self):
        return str(type(self))
    
    # Dizi elemanlarına indis harici erişim ve ekrana bastırma engellenir
    def __repr__(self):
        return repr(type(self))


# Kullanıcıdan diziyi sağa doğru kaydırılacak sayı istenir:
n = int(input("Dizideki sayılar ne kadar sağa doğru kaydırılacak?: "))

# Örnek Dizi Tanımlamak (2 alternatif)

# I) Dizi boyutu 7 olacak şekilde boş dizi tanımlanır
dizi = Array(7)

# Diziye dizi boyutu kadar eleman eklenir
dizi[0] = 3
dizi[1] = 5
dizi[2] = 7
dizi[3] = 9
dizi[4] = 11
dizi[5] = 13
dizi[6] = 15

# II) Dizi, en başta değerleriyle birlikte tanımlanır
dizi = Array(7, [3, 5, 7, 9, 11, 13, 15])

# Dizi elemanlarının ilk hali ekrana bastırılır (İlk durum için)
print("\nDizinin ilk durumu:")
for i in range(7):
    print(dizi[i], end=" ")

# Kullanıcının girdiği sayı kadar dizi boyutu büyültülür:
    # Dizi boyutunun büyütülmesi için önce büyük boyutlu dizi tanımlanır, ilk
    # dizinin elemanları tek tek yeni diziye aktarılır, ilk dizi silinir ve
    # yeni oluşturulan dizi mevcut dizi olarak tanımlanır

# Yeni dizi tanımlanır
dizi2 = Array(7+n)

# İlk dizinin elemanları tek tek yeni diziye ktarılır
for i in range(7):
    dizi2[i] = dizi[i]

# İlk dizi silinir
del dizi

# Yeni dizi mevcut dizi olarak tanımlanır
dizi = dizi2

# Yeni dizi de silinir
del dizi2

# Dizi elemanları tek tek sağa doğru kaydırılır
for i in range(6, -1, -1):      # Kaydırma dizinin son elemanından başlanır
    dizi[i+n] = dizi[i]
    dizi[i] = None

# Dizinin son hali yazdırılır
print("\n\nDizinin sağa kaydırıldıktan sonraki durumu:")
for i in range(7):
    print(f"dizi[{i+n}] =", dizi[i+n])

# OUTPUT:
Dizideki sayılar ne kadar sağa doğru kaydırılacak?: 5

Dizinin ilk durumu:
3 5 7 9 11 13 15 

Dizinin sağa kaydırıldıktan sonraki durumu:
dizi[5] = 3
dizi[6] = 5
dizi[7] = 7
dizi[8] = 9
dizi[9] = 11
dizi[10] = 13
dizi[11] = 15
