# ÇÖZÜM 1:

def harfDondurme(dizgi, sayi):
    return dizgi[sayi]

kelime = input("Bir kelime giriniz: ")
n = int(input("Bir sayı giriniz: "))

harfDondurme(kelime, n)

##########################################################

# ÇÖZÜM 2:

def harfDondurme(dizgi, sayi):
    return dizgi[sayi]

kelime = input("Bir kelime giriniz: ")

while True:
    n = input(f"Bir sayı giriniz (1 ilâ {len(kelime)} arası): ")
    
    if (not n.isnumeric()) or (int(n) == 0):
        print("Lütfen bir sayı giriniz!..")
    
    elif (int(n) > 0) and (int(n) < len(kelime)):
        n = int(n)
        break
    
    else:
        print(f"""Girdiğiniz sayı girilen kelimenin harf sayısından büyük olamaz!!!
Lütfen 1 ilâ {len(kelime)} arası bir sayı giriniz""")

harfDondurme(kelime, n-1)
