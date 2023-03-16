# ARRAY (DİZİ) ÜZERİNDE STACK YAPISI

# Stack dizisi için sınıf yapısı oluşturma
class Stack:
    def __init__(self, boyut):
        self.boyut = boyut
        self.tepe = 0
        self.dizi = []
        
        for i in range(self.boyut):
            self.dizi.append(None)

# Stack dizisinden eleman çıkarma fonksiyonu tanımlama
def popItem(s):
    if s.tepe == 0:
        return "Stack boş!!!"
    
    elif s.tepe <= (s.boyut / 4):
        s.boyut = int(s.boyut / 2)
        
        for i in range(s.tepe):
            s.dizi.pop()
    
    s.tepe -= 1
    return s.dizi[s.tepe]

# Stack dizisine eleman ekleme fonksiyonu tanımlama
def pushItem(s, a):
    if s.tepe >= s.boyut:
        s.boyut *= 2
        
        for i in range(s.boyut - s.tepe):
            s.dizi.append(None)
    
    s.dizi[s.tepe] = a
    s.tepe += 1

# Stack dizisindeki elemanları ekrana bastırma fonksiyonu tanımlama
def bastirStack(s):
    for i in range(s.tepe):
        print(s.dizi[i], end=" ")
    print()

# Stack dizisindeki elemanları ekrana tersten bastırma fonksiyonu tanımlama
def tersBastirStack(s):
    for i in range(s.tepe-1, -1, -1):
        print(s.dizi[i], end=" ")

# Stack sınıfından iki tane dizi nesnesi oluşturma
que_front = Stack(2)
que_end = Stack(2)

# İki adet stack (yığın) kullanarak double-ended queue (çift yönlü sıra) oluşturma

# Çift yönlü sıranın başından eleman çıkarma
def dequeFront():
    if que_front.tepe == 0:
        if que_end.tepe != 0:
            temp = Stack(2)
            
            for i in range(que_end.tepe-1):
                pushItem(temp, popItem(que_end))
            
            pushItem(que_front, popItem(que_end))
            
            for i in range(temp.tepe):
                pushItem(que_end, popItem(temp))
        
        else:
            return "Queue boş!!!"
    
    return popItem(que_front)

# Çift yönlü sıranın sonundan eleman çıkarma
def dequeEnd():
    if que_end.tepe == 0:
        if que_front.tepe != 0:
            temp = Stack(2)
            
            for i in range(que_front.tepe-1):
                pushItem(temp, popItem(que_front))
            
            pushItem(que_end, popItem(que_front))
            
            for i in range(temp.tepe):
                pushItem(que_front, popItem(temp))
        
        else:
            return "Queue boş!!!"
    
    return popItem(que_end)

# Çift yönlü sıranın başına eleman ekleme
def enqueFront(x):
    pushItem(que_front, x)

# Çift yönlü sıranın sonuna eleman ekleme
def enqueEnd(x):
    pushItem(que_end, x)

# Çift yönlü sıranın elemanlarını ekrana bastırma
def bastir():
    if (que_front.tepe != 0) or (que_end.tepe != 0):
        tersBastirStack(que_front)
        bastirStack(que_end)

# OUTPUT:
# Çift yönlü sıranın boş (ilk) halini ekrana bastırma
bastir()
# >>> 

# Çift yönlü sıranın başından eleman çıkarma
print(dequeFront())
# >>> Queue boş!!!

# Çift yönlü sıranın sonundan eleman çıkarma
print(dequeEnd())
# >>> Queue boş!!!

# Çift yönlü sıranın sonuna rasgele 3 tane sayı ekleme
enqueEnd(50)
enqueEnd(60)
enqueEnd(70)

# Çift yönlü sıranın elemanlarını ekrana bastırma
bastir()
# >>> 50 60 70 

# Çift yönlü sıranın başına rasgele 3 tane  sayı ekleme
enqueFront(40)
enqueFront(30)
enqueFront(20)

# Çift yönlü sıranın elemanlarını ekrana bastırma
bastir()
# >>> 20 30 40 50 60 70 

# Çift yönlü sıranın başına ve sonuna birer sayı ekleme
enqueFront(10)
enqueEnd(80)

# Çift yönlü sıranın elemanlarını ekrana bastırma
bastir()
# >>> 10 20 30 40 50 60 70 80 

# Çift yönlü sıranın başından eleman çıkarma
print(dequeFront())
# >>> 10

# Çift yönlü sıranın elemanlarını ekrana bastırma
bastir()
# >>> 20 30 40 50 60 70 80 

# Çift yönlü sıranın sonundan eleman çıkarma
print(dequeEnd())
# >>> 80

# Çift yönlü sıranın elemanlarını ekrana bastırma
bastir()
# >>> 20 30 40 50 60 70 

# Çift yönlü sıranın başına ve sonuna birer sayı ekleme
enqueEnd(80)
enqueFront(10)

# Çift yönlü sıranın elemanlarını ekrana bastırma
bastir()
# >>> 10 20 30 40 50 60 70 80 

# Çift yönlü sıranın başından 8 kere eleman çıkarma
for i in range(8):
    print(dequeFront())

# >>>
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80

# Çift yönlü sıranın elemanlarını ekrana bastırma
bastir()
# >>>

# Çift yönlü sıranın başından eleman çıkarma
print(dequeFront())
# >>> Queue boş!!!

# Çift yönlü sıranın sonundan eleman çıkarma
print(dequeEnd())
# >>> Queue boş!!!

# Çift yönlü sıranın başına ve sonuna rasgele sayılar ekleme
enqueEnd(50)
enqueEnd(60)
enqueEnd(70)
enqueFront(40)
enqueFront(30)
enqueFront(20)
enqueEnd(80)
enqueFront(10)

# Çift yönlü sıranın elemanlarını ekrana bastırma
bastir()
# >>> 10 20 30 40 50 60 70 80 

# Çift yönlü sıranın sonundan 8 kere eleman çıkarma
for i in range(8):
    print(dequeEnd())

# >>>
# 80
# 70
# 60
# 50
# 40
# 30
# 20
# 10
