# ARRAY (DİZİ) ÜZERİNDE STACK YAPISI

# Stack sınıf yapısı oluşturmak
class Stack:
    def __init__(self, boyut):
        self.boyut = boyut
        self.tepe = 0
        self.dizi = []
        
        for i in range(self.boyut):
            self.dizi.append(None)

# Stack dizisinden eleman çıkarma fonksiyonu tanımlamak
def popItem(s):
    if s.tepe == 0:
        return "Stack boş!!!"
    
    elif s.tepe <= (s.boyut / 4):
        s.boyut = int(s.boyut / 2)
        
        for i in range(s.tepe):
            s.dizi.pop()
    
    s.tepe -= 1
    return s.dizi[s.tepe]

# Stack dizisine eleman ekleme fonksiyonu tanımlamak
def pushItem(s, a):
    if s.tepe >= s.boyut:
        s.boyut *= 2
        
        for i in range(s.boyut - s.tepe):
            s.dizi.append(None)
    
    s.dizi[s.tepe] = a
    s.tepe += 1

# Stack dizisi oluşturmak
s = Stack(2)

# Palindrome kontrolü yapılacak örnek sayıların listesi:
liste = [3, 5, 7, 7, 5, 3]

# Palindrome kontrolü için sayıların yarısı stack dizine koymak
if len(liste) % 2 == 0:
    n = int(len(liste) / 2)
else:
    n = int(len(liste) / 2) + 1

for i in range(n):
    pushItem(s, liste[i])

# Stack dizisine konulmayan, geriye kalan sayılarla stack'ten alınan 'pop()'
# değerleri karşılaştırmak
if len(liste) % 2 == 0:
    for i in range(n, len(liste)):
        sonuc = popItem(s)
        
        if sonuc == liste[i]:
            flag = True
        else:
            flag = False
            break
else:
    for i in range(n-1, len(liste)):
        sonuc = popItem(s)
        
        if sonuc == liste[i]:
            flag = True
        else:
            flag = False
            break

if flag:
    print("Palindrome’dur")
else:
    print("Palindrome Değildir")

# OUTPUT:
liste = [3, 5, 7, 7, 5, 3]
# >>> Palindrome’dur

# OUTPUT 2:
liste = [1, 2, 3, 4, 5, 6]
# >>> Palindrome Değildir
