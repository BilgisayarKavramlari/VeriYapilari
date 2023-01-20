def dizgiTekrarSayisi(dizgi1, dizgi2):
    sayac = 0
    temp= ""

    for i in range(len(dizgi2)-len(dizgi1)+1):
        for j in range(i, i+len(dizgi1)):
            temp += dizgi2[j]
            if temp == dizgi1:
                sayac += 1
            
        temp = ""
    
    return sayac

kelime1 = input("İlk kelimeyi giriniz: ")
kelime2 = input("İkinci kelimeyi giriniz: ")

sonuc = dizgiTekrarSayisi(kelime1, kelime2)

print("Sonuç:", sonuc)

# OUTPUT:
# İlk kelimeyi giriniz: ber
# İkinci kelimeyi giriniz: bir berber bir berbere gel birader beraber berber
# dükkanı açalım demiş
# >>> Sonuç: 8
