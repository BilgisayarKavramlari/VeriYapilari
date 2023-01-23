email = input("E-posta adresinizi giriniz: ")

kullanici_adi = ""
host = ""

index = 0

for i in range(len(email)):
    if email[i] == "@":
        index = i

for i in range(index):
    kullanici_adi += email[i]

for i in range(index + 1, len(email)):
    host += email[i]

print("Kullanıcı adı:", kullanici_adi)
print("Hostu:", host)
