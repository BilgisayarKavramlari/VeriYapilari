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
# >>>
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

# Kullanıcıdan yeni bağlı listeye atanacak eleman sayısını istemek
n = int(input("Bağlı listedeki kaç eleman yeni bağlı listeye atansın: "))

# Bağlı listedeki kullanıcının girdiği sayıdaki eleman yeni bağlı listeye koyan
# fonksiyon tanımlamak
yeni_root = None

def ilk_N_Eleman(r1, r2):
    iterr = r1
    
    for i in range(n):
        r2 = ekle(r2, iterr.x)
        iterr = iterr.nextt
    
    return r2

# Oluşturulan fonksiyonu çağırmak
yeni_root = ilk_N_Eleman(root, yeni_root)

# Yeni bağlı listeyi ekrana bastırmak
bastir(yeni_root)

# OUTPUT:
# Bağlı listedeki kaç eleman yeni bağlı listeye atansın: 3
# 1
# 3
# 4

# OUTPUT 2:
# Bağlı listedeki kaç eleman yeni bağlı listeye atansın: 7
# 1
# 3
# 4
# 5
# 7
# 8
# 9
