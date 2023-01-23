def dizgidenDizgiCikarma(dizgi1, dizgi2):
    yeni_metin = ""
    i = 0
    
    while i < len(dizgi2):
        temp = ""
        
        for j in range(i, (i + len(dizgi1))):
            temp += dizgi2[j]
            
            if j == (len(dizgi2) - 1):
                break
        
        if temp == dizgi1:
            i += len(dizgi1) - 1
        else:
            yeni_metin += dizgi2[i]
        
        i += 1
    return yeni_metin

kelime = input("Silinecek kelimeyi giriniz: ")
metin = input("Metini giriniz: ")

sonuc = dizgidenDizgiCikarma(kelime, metin)

print("Sonuç:", sonuc)

# OUTPUT:
# Silinecek kelimeyi giriniz: ber
# Metini giriniz: bir berber bir berbere gel birader beraber bir berber dükkanı
# açalım demiş
# >>> Sonuç: bir  bir e gel birader a bir  dükkanı açalım demiş
