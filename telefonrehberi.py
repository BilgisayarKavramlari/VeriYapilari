while True:
    def kayitekle(isim,numara):
        spaces=50-len(isim)-len(numara)
        space=spaces*" "


        dosya = open("telefonrehberi.txt", "a+")

        dosya.write(isim+space+numara+"\n")
        dosya.flush()
        print("Kayıt eklendi!")


    def kayitarama(aranan):
        with open('telefonrehberi.txt', 'r') as searchfile:
            for line in searchfile:
                if aranan in line:
                    print(line)



    print("\n\n===========TELEFON REHBERİ===========\n\n")
    secenek=int(input("1=Rehbere yeni kayıt ekle.\n2=Rehberde arama yap.\n"))


    if(secenek==1):
        isim=input("İsim giriniz:")
        numara = input("Numara giriniz:")
        kayitekle(isim,numara)

    elif(secenek==2):
        aranan=input("Aramak istediğiniz isimi giriniz:")
        kayitarama(aranan)

    else:
        print("Lütfen geçerli bir seçenek giriniz.")

