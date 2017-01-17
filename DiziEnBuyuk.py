i = 0
enBuyuk = 0
sinirSayi = int(input("Gireceğiniz sayı miktarını yazınız: "))
while i <= sinirSayi-1:            # i değeri sinirSayi olana kadar bu işlemleri yap, ilk girdiği 0.index olarak aldığı için '-1' yaptık.
     sayi = int(input("Sayı Giriniz: "))
     if sayi > enBuyuk:
        enBuyuk = sayi
     print("Girdiğiniz en büyük sayı: ", enBuyuk)
     i += 1

#feyyazonur
