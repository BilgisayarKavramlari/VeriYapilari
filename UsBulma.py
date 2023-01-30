x = int(input("Üssünü bulmak istediğiniz sayıyı giriniz: "))
y = int(input("Üssü giriniz: "))

def usBulma(a, b):
    return a ** b

sonuc = usBulma(x, y)

print(f"\n{x} sayısının {y}. kuvvetinin değeri:", sonuc)

# OUTPUT:
Üssünü bulmak istediğiniz sayıyı giriniz: 3
Üssü giriniz: 4

3 sayısının 4. kuvvetinin değeri: 81
