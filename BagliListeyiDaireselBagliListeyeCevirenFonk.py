class Node:
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
        r = Node()
        r.x = data
        r.nextt = None
        return r
    
    elif r.x > data:
        temp = Node()
        temp.x = data
        temp.nextt = r
        r = temp
        return temp
    
    iterr = r
    while (iterr.nextt != None) and (iterr.nextt.x < data):
        iterr = iterr.nextt
    
    temp = Node()
    temp.x = data
    temp.nextt = iterr.nextt
    iterr.nextt = temp
    return r

def daireselListeBastir(r):
    if r == None:
        print("Bağlı liste boşşş!")
        return r
    
    iterr = r
    print(iterr.x, end=" ")
    iterr = iterr.nextt
    
    while iterr != r:
        print(iterr.x, end=" ")
        iterr = iterr.nextt
    print()

def daireselListeEkle(r, data):
    if r == None:
        r = Node()
        r.x = data
        r.nextt = r
        return r
    
    iterr = r
    
    while iterr.nextt != r:
        iterr = iterr.nextt
    
    iterr.nextt = Node()
    iterr.nextt.x = data
    iterr.nextt.nextt = r
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

# Bağlı listeyi dairesel bağlı listeye çeviren fonksiyon tanımlamak
def daireselListeyeCevir(r1):
    r2 = None
    
    while r1 != None:
        r2 = daireselListeEkle(r2, r1.x)
        r1 = r1.nextt
    
    return r2

# Oluşturulan fonksiyonu çağırmak
yeni_root = daireselListeyeCevir(root)

# Dairesel bağlı listeyi ekrana bastırmak
daireselListeBastir(yeni_root)
# >>> 1 3 4 5 7 12 16 17 19 20 

# Dairesel bağlı listeye en son elemanı ekrana bastırmak
iterr = yeni_root

while iterr.nextt != yeni_root:
    iterr = iterr.nextt

print("En son eklenen:", iterr.x)
# >>> En son eklenen: 20

# Dairesel bağlı listenin en son elemanından sonraki elemanı bastırmak
print(iterr.nextt.x)
# >>> 1     (20'den sonra root'un gösterdiği 1'i bastırdı, yani listenin başına döndü)
