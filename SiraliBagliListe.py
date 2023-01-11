class Node:
    def __init__(self, data="", nextt=""):
        self.data = data
        self.nextt = nextt

def ekleSirali(r, v):
    if r == None:
        r = Node()
        r.data = v
        r.nextt = None
        return r
    
    elif r.data > v:
        temp = Node()
        temp.data = v
        temp.nextt = r
        return temp
    
    iterr = Node()
    iterr = r
    
    while (iterr.nextt != None) and (iterr.nextt.data < v):
        iterr = iterr.nextt
    
    temp = Node()
    temp.data = v
    temp.nextt = iterr.nextt
    iterr.nextt = temp
    return r

def bastir(r):
    while r != None:
        print(r.data, end=" ")
        r = r.nextt

root = None

dizi = [2, 3, 6, 3, 4, 1, 9, 8, 2, 6]

for i in dizi:
    root = ekleSirali(root, i)


bastir(root)

# OUTPUT:
# 1 2 2 3 3 4 6 6 8 9 
