def harfTekrariDondurme(dizgi, s):
    sayac = 0
    
    for i in dizgi:
        if i == harf:
            sayac += 1
    
    return sayac

kelime = input("Bir kelime giriniz: ")
harf = input("Bir sayı giriniz: ")

harfTekrariDondurme(kelime, harf)
