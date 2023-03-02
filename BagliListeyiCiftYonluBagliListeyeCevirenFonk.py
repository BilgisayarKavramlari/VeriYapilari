class SinglyNode:
    def __init__(self, x="", nextt=""):
        self.x = x
        self.nextt = nextt

def bagliListeBastir(r):
    if r == None:
        print("Bağlı liste boşşş!")
        return r
    
    while r != None:
        print(r.x, end=" ")
        r = r.nextt
    print()

def bagliListeEkle(r, data):
    if r == None:
        r = SinglyNode()
        r.x = data
        r.nextt = None
        return r
    
    elif r.x > data:
        temp = SinglyNode()
        temp.x = data
        temp.nextt = r
        r = temp
        return temp
    
    iterr = r
    while (iterr.nextt != None) and (iterr.nextt.x < data):
        iterr = iterr.nextt
    
    temp = SinglyNode()
    temp.x = data
    temp.nextt = iterr.nextt
    iterr.nextt = temp
    return r

class DoublyNode:
    def __init__(self, x="", nextt="", prev=""):
        self.x = x
        self.nextt = nextt
        self.prev = prev

def ciftBagliListeBastir(r):
    if r == None:
        print("Bağlı liste boşşş!")
        return r
    
    while r != None:
        print(r.x, end=" ")
        r = r.nextt
    print()

def ciftBagliListeEkle(r, data):
    if r == None:
        r = DoublyNode()
        r.x = data
        r.nextt = None
        r.prev = None
        return r
    
    iterr = r
    
    while iterr.nextt != None:
        iterr = iterr.nextt
    
    iterr.nextt = DoublyNode()
    iterr.nextt.x = data
    iterr.nextt.nextt = None
    iterr.nextt.prev = iterr
    return r

# Bağlı listenin ilk elemanını gösterecek root'u tanımlayıp None değerini atamak
root = None

# Bağlı listeye hem tek tem çift sayılar içeren karışık sayılar eklemek
root = bagliListeEkle(root, 7)
root = bagliListeEkle(root, 20)
root = bagliListeEkle(root, 4)
root = bagliListeEkle(root, 1)
root = bagliListeEkle(root, 17)
root = bagliListeEkle(root, 5)
root = bagliListeEkle(root, 12)
root = bagliListeEkle(root, 19)
root = bagliListeEkle(root, 3)
root = bagliListeEkle(root, 16)

# Oluşturulan bağlı liste içeriğini ekrana bastırmak
bagliListeBastir(root)
# >>> 1 3 4 5 7 12 16 17 19 20 

# Bağlı listeyi çift yönlü bağlı listeye çeviren fonksiyon tanımlamak
def ciftBagliListeyeCevir(r1):
    r2 = None
    
    while r1 != None:
        r2 = ciftBagliListeEkle(r2, r1.x)
        r1 = r1.nextt
    
    return r2

# Oluşturulan fonksiyonu çağırmak
yeni_root = ciftBagliListeyeCevir(root)

# Dairesel bağlı listeyi ekrana bastırmak
ciftBagliListeBastir(yeni_root)
# >>> 1 3 4 5 7 12 16 17 19 20 

# Çift yönlü bağlı listenin 3. elemanını ekrana bastırmak
iterr = yeni_root

for i in range(2):
    iterr = iterr.nextt

print("3. eleman:", iterr.x)
# >>> 3. eleman: 4

# Çift yönlü bağlı listedeki 3 elemandan önceki ve sonraki elemanı bastırmak
print("2. eleman:", iterr.prev.x)
# >>> 2. eleman: 3

print("4. eleman:", iterr.nextt.x)
# >>> 4. eleman: 5

# listenin herhangi bir sıradaki elemanına erişip daha sonra liste içerisinde
# ileriye ve geriye hareket edeibliyoruz.
