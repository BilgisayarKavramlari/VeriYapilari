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

def ciftMi(sayi):
    if sayi % 2 == 0:
        return True
    else:
        return False

def tekMi(sayi):
    if sayi % 2 != 0:
        return True
    else:
        return False

def filtrele(agac, fonk):
    if agac == None:
        return "Ağaç boş!!!"
    
    if fonk(agac.data) == True:
        print(agac.data, end=" ")
    
    if filtrele(agac.sol, fonk) == True:
        print(agac.data, end=" ")
    
    if filtrele(agac.sag, fonk) == True:
        print(agac.data, end=" ")

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

filtrele(root, ciftMi)
# >>> 56 26 18 12 24 28 200 190 

filtrele(root, tekMi)
# >>> 27 213 
