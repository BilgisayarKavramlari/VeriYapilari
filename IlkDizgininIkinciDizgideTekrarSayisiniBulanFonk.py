def dizgiTekrarSayisi(dizgi1, dizgi2):
    sayac = 0

    for i in range(len(dizgi2)-1):
        if (dizgi2[i] + dizgi2[i+1]) == dizgi1:
            sayac += 1
    
    return sayac

kelime1 = input("İlk kelimeyi giriniz: ")
kelime2 = input("İkinci kelimeyi giriniz: ")

sonuc = dizgiTekrarSayisi(kelime1, kelime2)

print("Sonuç:", sonuc)
