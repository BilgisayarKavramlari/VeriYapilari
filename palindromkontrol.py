x=int(input("Sayıyı giriniz:"))

def palindrom(sayi):
    sayibasamak=list(str(sayi))
    i=0

    while i<=((len(sayibasamak)/2)):
        if(sayibasamak[i] != sayibasamak[-(i+1)]):
            return False
        else:
            i=i+1



if(palindrom(x)!= False):
    print("Satı palindrom sayısıdır.")

else:
    print("Sayı palindrom sayısı değildir.")
