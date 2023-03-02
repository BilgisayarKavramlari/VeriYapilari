class Node:
    def __init__(self, x="", nextt=""):
        self.x = x
        self.nextt = nextt

def bastir(r):
    if r == None:
        print("Bağlı liste boşşş!")
        return r
    
    while r != None:
        print(r.x, end=" ")
        r = r.nextt
    print()

def oneEkle(r, data):
    if r == None:
        r = Node()
        r.x = data
        r.nextt = None
        return r
    
    temp = Node()
    temp.x = data
    temp.nextt = r
    r = temp
    return temp

def siraliEkle(r, data):
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

# Bağlı listenin ilk elemanını gösterecek root'u tanımlayıp None değerini atamak
root = None

# Bağlı listeye karışık sayılar eklemek
root = siraliEkle(root, 7)
root = siraliEkle(root, 20)
root = siraliEkle(root, 4)
root = siraliEkle(root, 1)
root = siraliEkle(root, 17)
root = siraliEkle(root, 5)
root = siraliEkle(root, 12)
root = siraliEkle(root, 19)
root = siraliEkle(root, 3)
root = siraliEkle(root, 16)

# Oluşturulan bağlı liste içeriğini ekrana bastırmak
bastir(root)
# >>> 1 3 4 5 7 12 16 17 19 20 

# Bağlı listeyi ters çeviren fonksiyon tanımlamak
def tersCevir(r1):
    """
    Bağlı listeyi ters çevirip yeni bağlı listeye atayan fonksiyon
    """
    r2 = None
    
    while r1 != None:
        r2 = oneEkle(r2, r1.x)
        r1 = r1.nextt
    
    return r2

# Oluşturulan fonksiyonu çağırmak
yeni_root = tersCevir(root)

# Terse çevrilen bağlı listeyi ekrana bastırmak
bastir(yeni_root)
# >>> 20 19 17 16 12 7 5 4 3 1 
