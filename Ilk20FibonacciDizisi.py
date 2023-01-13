liste = []

a = 1
b = 1

liste.append(a)
liste.append(b)

sayac = 2

while sayac < 20:
    c = a + b
    liste.append(c)
    a = b
    b = c
    
    sayac += 1

print(liste)

# OUTPUT:
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
