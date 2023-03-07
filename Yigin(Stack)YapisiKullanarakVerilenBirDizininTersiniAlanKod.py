# LINKED LIST (BAĞLI LİSTE) ÜZERİNDE STACK YAPISI

# Düğüm sınıf yapısı oluşturmak
class Node:
    def __init__(self, data="", nextt=""):
        self.data = data
        self.nextt = nextt

# Stack dizisinden eleman çıkarma fonksiyonu tanımlamak
def popItem(r):
    if r.data == "":
        return "Stack boş!!!"
    
    elif r.nextt == None:
        rvalue = r.data
        r.data = ""
        return rvalue
    
    iterr = r
    
    while iterr.nextt.nextt != None:
        iterr = iterr.nextt
    
    rvalue = iterr.nextt.data
    iterr.nextt = None
    return rvalue

# Stack dizisine eleman ekleme fonksiyonu tanımlamak
def pushItem(r, a):
    if r.data == "":
        r.data = a
        return
    
    while r.nextt != None:
        r = r.nextt
    
    r.nextt = Node()
    r.nextt.data = a
    r.nextt.nextt = None

# Stack dizisinin elemanlarını ekrana bastırma fonksiyonu tanımlamak
def bastir(r):
    while r != None:
        if r.data != "":
            print(r.data, end=" ")
        r = r.nextt
    print()

# İki adet 2 boyutlu Stack dizisi oluşturmak
s1 = Node()
s1.nextt = None

s2 = Node()
s2.nextt = None

# s1 dizisine 0'dan 90'a kadar for döngüsüyle 10 adet eleman eklemek
for i in range(10):
    pushItem(s1, i * 10)

# s1 ve s2 dizilerini ekrana bastırmak
bastir(s1)
# >>> 90 80 70 60 50 40 30 20 10 0 

bastir(s2)
# >>> 

# s1 dizisindeki elemanları tek tek diziden çıkarmak ve pop() edilenleri s2
# dizisine eklemek
for i in range(10):
    pushItem(s2, popItem(s1))

# s1 ve s2 dizilerini ekrana bastırmak
bastir(s1)
# >>> 

bastir(s2)
# >>> 90 80 70 60 50 40 30 20 10 0 
