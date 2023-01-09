class Node:
    def __init__(self, data="", nextt=""):
        self.data = data
        self.nextt = nextt

def bastir(r):
    while r != None:
        print(r.data, end=" ")
        r = r.nextt

def ekle(r, v):
    while r.nextt != None:
        r = r.nextt
    
    r.nextt = Node()
    r.nextt.data = v
    r.nextt.nextt = None

dizi = [2, 3, 6, 3, 4, 1, 9, 8, 2, 6]

root = Node()
root.data = dizi[0]
root.nextt = None

for i in range(1, len(dizi)):
    ekle(root, dizi[i])

bastir(root)

# OUTPUT:
# 2 3 6 3 4 1 9 8 2 6 
