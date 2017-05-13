liste = [12,4,21,73,91,87,25,88,36,905,663,774,125]
siralandi = False
while not siralandi: #Sıralanmadığı sürece döngü devam edecek.
    siralandi = True #Döngünün içerisine girildiğinde sıralanmış kabul ediyoruz.
    iterator = 0
    for iterator in range(len(liste) - 1):
        if liste[iterator] > liste[iterator + 1]:
            liste[iterator], liste[iterator + 1] = liste[iterator + 1], liste[iterator]
            siralandi = False #Sıralama yapılmadığı için bu değişkeni tekrar False yapıyoruz.
print(liste) #sıralanmış listeyi yazdırırıyoruz.
