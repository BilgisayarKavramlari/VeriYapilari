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
dizi = Array(9, [2, 3, 5, 10, 11, 15, 19, 20, 33])

# Kullanıcıdan çarpacak sayı alma
n = int(input("Dizideki sayıların çarpılmasını istediğiniz sayıyı giriniz: "))

# Dizinin ilk halini ekrana basma
print("\nDizinin ilk durumu:")

for i in range(9):
    print(dizi[i], end=" ")
print()

# Dizideki sayıları tek tek kullanıcının giridği sayı ile çarpma ve tekrar
# diziye yerleştirme
for i in range(9):
    dizi[i] *= n

# Dizinin çarpımdan sonraki halini ekrana basma
print("\nDizinin çarpımdan sonraki durumu:")

for i in range(9):
    print(dizi[i], end=" ")

# OUTPUT:
Dizideki sayıların çarpılmasını istediğiniz sayıyı giriniz: 5

Dizinin ilk durumu:
2 3 5 10 11 15 19 20 33 

Dizinin çarpımdan sonraki durumu:
10 15 25 50 55 75 95 100 165 
