number = int(input("Bir sayı girin: "))

temp = number
total = 0

while temp > 0:
    total *= 10
    total += temp % 10
    temp //= 10

if number == total:
    print("Girdiğiniz sayı 'Polindromik Sayı'dır..")
else:
    print("Girdiğiniz sayı 'Polindromik Sayı' değildir!..")

# II. YOL (Alternatif Çözüm);

sayi = input("Bir sayı girin: ")

tersi = sayi[::-1]

if sayi == tersi:
    print("Girdiğiniz sayı 'Polindromik Sayı'dır..")
else:
    print("Girdiğiniz sayı 'Polindromik Sayı' değildir!..")
