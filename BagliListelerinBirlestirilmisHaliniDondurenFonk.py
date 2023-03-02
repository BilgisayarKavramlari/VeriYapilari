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

# Bağlı listelerin ilk elemanını gösterecek root'ları tanımlayıp None değerini atamak
root1 = None
root2 = None

# 1. bağlı listeye karışık sayılar eklemek
root1 = ekle(root1, 3)
root1 = ekle(root1, 7)
root1 = ekle(root1, 1)
root1 = ekle(root1, 9)
root1 = ekle(root1, 5)

# 2. bağlı listeye karışık sayılar eklemek
root2 = ekle(root2, 8)
root2 = ekle(root2, 4)
root2 = ekle(root2, 10)
root2 = ekle(root2, 6)
root2 = ekle(root2, 2)

# Oluşturulan bağlı listelerin içeriğini ekrana bastırmak
bastir(root1)
# >>>
# 1
# 3
# 5
# 7
# 9

bastir(root2)
# >>>
# 2
# 4
# 6
# 8
# 10
#%%
# İki bağlı listeyi birleştiren fonksiyon tanımlamak
def birlestir(r1, r2):
    """
    İki bağlı listeyi birleştirip birleşmiş halini ekrana basan fonksiyon
    """
    
    while r1 != None:
        print(r1.x)
        r1 = r1.nextt
    
    while r2 != None:
        print(r2.x)
        r2 = r2.nextt

# Oluşturulan fonksiyonu çağırmak
birlestir(root1, root2)

# >>>
# 1
# 3
# 5
# 7
# 9
# 2
# 4
# 6
# 8
# 10

# İki bağlı listeyi birleştirip yeni bağlı listeye atayan fonksiyon tanımlamak
def birlestir2(r1, r2):
    """
    İki bağlı listeyi birleştirip birleşmiş halini yeni bir bağlı listeye
    atayan fonksiyon
    """
    
    r3 = None
    
    while r1 != None:
        r3 = ekle(r3, r1.x)
        r1 = r1.nextt
    
    while r2 != None:
        r3 = ekle(r3, r2.x)
        r2 = r2.nextt
    
    return r3

root3 = birlestir2(root1, root2)

bastir(root3)
# >>>
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
