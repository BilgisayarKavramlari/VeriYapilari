class Node:
    def __init__(self, data="", sol="", sag=""):
        self.data = data
        self.sol = sol
        self.sag = sag

def ekle(agac, x):
    if agac == None:
        agac = Node()
        agac.data = x
        agac.sol = None
        agac.sag = None
        return agac
    
    elif agac.data < x:
        agac.sag = ekle(agac.sag, x)
        return agac
    
    agac.sol = ekle(agac.sol, x)
    return agac

# LNR olarak dolaşma
def dolas(agac):
    if agac == None:
        return
    
    dolas(agac.sol)
    print(agac.data, end=" ")
    dolas(agac.sag)

toplam = 0

def topla(toplam, sayi):
    toplam += sayi
    return toplam

def tumElemanlar(agac, fonk):
    global toplam
    
    if agac == None:
        return "Ağaç boş!!!"
    
    toplam = fonk(toplam, agac.data)
    tumElemanlar(agac.sol, fonk)
    tumElemanlar(agac.sag, fonk)
    return toplam

root = None

root = ekle(root, 56)
root = ekle(root, 200)
root = ekle(root, 26)
root = ekle(root, 190)
root = ekle(root, 213)
root = ekle(root, 18)
root = ekle(root, 28)
root = ekle(root, 12)
root = ekle(root, 24)
root = ekle(root, 27)

# LNR olarak dolaşma
dolas(root)
# >>> 12 18 24 26 27 28 56 190 200 213 

print("Ağacın tüm elemanları toplamı:", tumElemanlar(root, topla))
# >>> Ağacın tüm elemanları toplamı: 794
