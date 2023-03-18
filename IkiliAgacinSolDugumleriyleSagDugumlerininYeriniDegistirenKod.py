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

# Dolaşmada Kullanılan Yapılar
    # Infix     = LNR, RNL
    # Prefix    = NLR, NRL
    # Postfix   = LRN, RLN

# LNR olarak dolaşma
def dolas(agac):
    if agac == None:
        return
    
    dolas(agac.sol)
    print(agac.data, end=" ")
    dolas(agac.sag)

# NLR olarak dolaşma
def dolas2(agac):
    if agac == None:
        return
    
    print(agac.data, end=" ")
    dolas2(agac.sol)
    dolas2(agac.sag)

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

# NLR olarak dolaşma
dolas2(root)
# >>> 56 26 18 12 24 28 27 200 190 213 

def degistir(agac):
    if agac == None:
        return
    
    degistir(agac.sol)
    temp = agac.sol
    agac.sol = agac.sag
    agac.sag = temp
    degistir(agac.sol)

degistir(root)

# LNR olarak dolaşma
dolas(root)
# >>> 213 200 190 56 28 27 26 24 18 12 

# NLR olarak dolaşma
dolas2(root)
# >>> 56 200 213 190 26 28 27 18 24 12 
