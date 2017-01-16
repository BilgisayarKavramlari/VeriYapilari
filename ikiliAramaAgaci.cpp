#include <iostream>
#include <stdlib.h>

using namespace std;

// elemanımız için kullanacağımız düğüm yapımız
struct dugum {
    int veri;
    dugum* sol;
    dugum* sag;
};

typedef dugum eleman;

eleman*
ekle(eleman* agac, int eklenecekDeger)
{
    // ağacımız tamamen boş ise
    if(agac == NULL) {
        // kökümüzü oluşturuyoruz
        eleman* kok = ( eleman* ) malloc(sizeof(eleman));

        // kökümüzün sağı ve solunu boş olacakları için NULL yapıyoruz
        kok->sag = NULL;
        kok->sol = NULL;

        // eklenecek değerimizi ekliyoruz
        kok->veri = eklenecekDeger;

        // ve yeni kök değerimizi geriye döndürüyoruz
        return kok;
    }

    // eklenecek değer kökten büyükse sağ alt ağaca geçip
    // fonksiyonumuzu orada tekrar işliyoruz (özyineleme)
    if(agac->veri < eklenecekDeger) {
        agac->sag = ekle(agac->sag, eklenecekDeger);
    }
    else  // değer kökten küçükse sol alt ağaca geçiyoruz
    {
        agac->sol = ekle(agac->sol, eklenecekDeger);
    }

    // ağacımızın son halini geriye döndürüyoruz
    return agac;
}

void
soldanSagaDolas(eleman* agac)
{
    // dolaşacak değer kalmadığında geriye dönüyoruz
    if(agac == NULL) {
        return;
    }

    // önce sol alt ağacımıza uğruyoruz
    soldanSagaDolas(agac->sol);

    // sol alt ağaçtaki yaprak düğümümüzü yazdırıyoruz
    cout << agac->veri << " ";

    // sonra sağ alt ağaca geçiyoruz
    soldanSagaDolas(agac->sag);
}

void
koktenSagaDolas(eleman* agac)
{
    // dolaşacak değer kalmadığında geriye dönüyoruz
    if(agac == NULL) {
        return;
    }

    // önce kökümüzü yazdırıyoruz
    cout << agac->veri << " ";

    // sonra sol alt ağacımıza uğruyoruz
    koktenSagaDolas(agac->sol);

    // en son sağ alt ağaca geçiyoruz
    koktenSagaDolas(agac->sag);
}

void
soldanKokeDolas(eleman* agac)
{
    // dolaşacak değer kalmadığında geriye dönüyoruz
    if(agac == NULL) {
        return;
    }

    // önce sol alt ağacımıza uğruyoruz
    soldanKokeDolas(agac->sol);

    // sonra sağ alt ağaca geçiyoruz
    soldanKokeDolas(agac->sag);

    // en son kökümüzü yazdırıyoruz
    cout << agac->veri << " ";
}

int
enKucukDegeriBul(eleman* agac)
{
    eleman* arayici = agac;

    // düğüm solunda çocuk barındırdığı sürece
    // soluna doğru gitmeye devam ediyoruz
    while(arayici->sol != NULL) arayici = arayici->sol;

    // bulduğumuz düğümün değerini geri döndürüyoruz
    return arayici->veri;
}

int
enBuyukDegeriBul(eleman* agac)
{
    eleman* arayici = agac;

    // düğüm sağında çocuk barındırdığı sürece
    // sağına doğru gitmeye devam ediyoruz
    while(arayici->sag != NULL) arayici = arayici->sag;

    // bulduğumuz düğümün değerini geri döndürüyoruz
    return arayici->veri;
}

eleman*
sil(eleman* agac, int silinecekDeger)
{
    // ağacımız tamamen boş ise
    if(agac == NULL) {
        return NULL;
    }

    // silinecek değer kök düğümde ise
    if(silinecekDeger == agac->veri) {
        // kökün çocuk düğümü yoksa
        if(agac->sol == NULL && agac->sag == NULL) {
            return NULL;
        }

        // kökün sağında çocuk düğüm var ise
        if(agac->sag != NULL) {
            // kökün sağ alt ağacındaki en küçük değeri buluyoruz
            // ve yer değiştirme yapıyoruz
            agac->veri = enKucukDegeriBul(agac->sag);

            // sonrasında o değeri siliyoruz
            agac->sag = sil(agac->sag, enKucukDegeriBul(agac->sag));

            return agac;
        }
        // kökün solunda çocuk düğüm var ise
        if(agac->sol != NULL) {
            // kökün sol alt ağacındaki en büyük değeri buluyoruz
            // ve yer değiştirme yapıyoruz
            agac->veri = enBuyukDegeriBul(agac->sol);

            // sonrasında o değeri siliyoruz
            agac->sol = sil(agac->sol, enBuyukDegeriBul(agac->sol));
            return agac;
        }
    }
    // silinecek değer kökten küçük ise sol alt ağaca geçiyoruz
    if(silinecekDeger < agac->veri) {
        // silinecek değeri sol alt ağaçtan sil
        // ve o ağacı yeni sol alt ağaç yap
        agac->sol = sil(agac->sol, silinecekDeger);
        return agac;
    }
    // silinecek değer kökten büyük ise sağ alt ağaca geçiyoruz
    else {
        // silinecek değeri sağ alt ağaçtan sil
        // ve o ağacı yeni sağ alt ağaç yap
        agac->sag = sil(agac->sag, silinecekDeger);
    }

    // ağacımızın son halini geriye döndürüyoruz
    return agac;
}

int
main(int argc, char* argv[])
{
    // ağacımızı oluşturuyoruz
    eleman* agac = NULL;

    // örnek değerlerimizi giriyoruz
    agac = ekle(agac, 15);
    agac = ekle(agac, 6);
    agac = ekle(agac, 3);
    agac = ekle(agac, 2);
    agac = ekle(agac, 4);
    agac = ekle(agac, 7);
    agac = ekle(agac, 13);
    agac = ekle(agac, 18);
    agac = ekle(agac, 17);
    agac = ekle(agac, 20);

    // dolaşma işlemleri
    soldanSagaDolas(agac);
    cout << endl;
    koktenSagaDolas(agac);
    cout << endl;
    soldanKokeDolas(agac);
    cout << endl;

    // en küçük ve en büyük değer bulma işlemleri
    cout << enKucukDegeriBul(agac) << endl;
    cout << enBuyukDegeriBul(agac) << endl;

    // silme işlemleri
    agac = sil(agac, 2);
    soldanSagaDolas(agac);
    cout << endl;

    agac = sil(agac, 20);
    soldanSagaDolas(agac);
    cout << endl;

    agac = sil(agac, 13);
    soldanSagaDolas(agac);
    cout << endl;

    return 0;
}
