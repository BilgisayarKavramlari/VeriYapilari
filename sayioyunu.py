import random

def tahmin(giris):
    global bilgisayar,adım

    if(giris>bilgisayar):
        adım+=1
        giris=int(input("Daha küçük bir sayı dene!"))
        tahmin(giris)

    elif(giris<bilgisayar):
        adım+=1
        giris = int(input("Daha büyük bir sayı dene!"))
        tahmin(giris)

    else:
        print("Doğru tahmin!\n\n")
        print(adım," adımda buldun!")
        if(adım<=5):
            print("Harika!!")
        elif (adım>5&adım<=25):
            print("İdare eder...")
        else:
            print("Biraz zor oldu bu!")


bilgisayar=random.randint(0,100)
adım=1
giris=int(input("Bir sayı dene!"))
tahmin(giris)

