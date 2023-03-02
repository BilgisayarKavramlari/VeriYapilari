class Node:
    def __init__(self, x="", nextt=""):
        self.x = x
        self.nextt = nextt

def bastir(r):
    if r == None:
        print("Bağlı liste boşşş!")
        return r
    
    while r != None:
        print(r.x)
        r = r.nextt

def ekle(r, data):
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

def sil(r, data):
    if r == None:
        print("Boşşş!")
        return r
    
    iterr = r
    
    if r.x == data:
        temp = r
        r = r.nextt
        del temp
        return r
    
    while (iterr.nextt != None) and (iterr.nextt.x != data):
        iterr = iterr.nextt
    
    if iterr.nextt == None:
        print("Sayı bulunamadı!..")
        return r
    
    temp = iterr.nextt
    iterr.nextt = iterr.nextt.nextt
    del temp
    return r

# Bağlı listenin ilk elemanını gösterecek root'u tanımlayıp None değerini atamak
root = None

# Bağlı listeye karışık sayılar eklemek
root = ekle(root, 7)
root = ekle(root, 20)
root = ekle(root, 4)
root = ekle(root, 1)
root = ekle(root, 17)
root = ekle(root, 5)
root = ekle(root, 12)
root = ekle(root, 19)
root = ekle(root, 3)
root = ekle(root, 16)

# Oluşturulan bağlı liste içeriğini ekrana bastırmak
bastir(root)
# >>>
# 1
# 3
# 4
# 5
# 7
# 12
# 16
# 17
# 19
# 20

# Bağlı listedeki elemanların iki mislini alan ve ekrana basan fonksiyon tanımlamak
def ikiMisliEkranaBas(r):
    """
    Bağlı listedeki sayıların iki mislini ekrana basar, bağlı liste içeriğinde
    değişiklik olmaz, sayılar aynı kalır.
    """
    iterr = r
    
    while iterr != None:
        print(iterr.x * 2)
        iterr = iterr.nextt

# Oluşturulan fonksiyonu çağırmak
ikiMisliEkranaBas(root)
# >>>
# 4
# 12
# 16
# 20
# 28
# 48
# 64
# 68
# 76
# 80

# Bağlı listeyi ekrana bastırmak
bastir(root)
# >>>
# 1
# 3
# 4
# 5
# 7
# 12
# 16
# 17
# 19
# 20

# Bağlı listedeki elemanların iki mislini alan fonksiyon tanımlamak
def ikiMisli(r):
    """
    Bağlı listedeki sayıların iki mislini alır, bağlı liste içeriğinde
    değişiklik yapılır, yeni bağlı listedeki sayılar iki misli olur.
    """
    iterr = r
    
    while iterr != None:
        iterr.x *= 2
        iterr = iterr.nextt

# Oluşturulan fonksiyonu çağırmak
ikiMisli(root)

# Güncellenen yeni bağlı liste ekrana bastırmak
bastir(root)
# >>>
# 4
# 12
# 16
# 20
# 28
# 48
# 64
# 68
# 76
# 80
