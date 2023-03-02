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

# Bağlı listeye hem tek tem çift sayılar içeren karışık sayılar eklemek
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
root = ekle(root, 11)
root = ekle(root, 9)
root = ekle(root, 14)
root = ekle(root, 8)
root = ekle(root, 15)

# Oluşturulan bağlı liste içeriğini ekrana bastırmak
bastir(root)
# 1
# 3
# 4
# 5
# 7
# 8
# 9
# 11
# 12
# 14
# 15
# 16
# 17
# 19
# 20

# Bağlı listedeki çift sayıları silmek
iterr = root

while iterr != None:
    if iterr.x % 2 == 0:
        sil(root, iterr.x)
        print(iterr.x, "silindi..")
    iterr = iterr.nextt

# >>>
# 4 silindi..
# 8 silindi..
# 12 silindi..
# 14 silindi..
# 16 silindi..
# 20 silindi..

# Silme işleminden sonra bağlı listedeki kalan sayıları ekrana basmak
bastir(root)
# >>>
# 1
# 3
# 5
# 7
# 9
# 11
# 15
# 17
# 19
