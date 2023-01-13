number1 = int(input("1. sayıyı giriniz: "))
number2 = int(input("2. sayıyı giriniz: "))

def ikiSayıyıTopla(a, b):
    return a + b

print(f"\nGirdiğiniz iki sayının toplamı: {number1} + {number2} =",
      ikiSayıyıTopla(number1, number2))

# OUTPUT:
1. sayıyı giriniz: 15
2. sayıyı giriniz: 25

Girdiğiniz iki sayının toplamı: 15 + 25 = 40
