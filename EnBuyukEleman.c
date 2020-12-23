#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void dizi_olustur(int dizi[],int boyut){
    srand(time(NULL));
    for(int i=0;i<10;i++){
        dizi[i]= rand()%100;
    }
}

int en_buyuk_eleman(){
    int boyut=10;
    int dizi[boyut];
    
    dizi_olustur(dizi,boyut);
    
    int en_buyuk = dizi[0];
    for(int i=1;i<boyut;i++){
        if(en_buyuk<dizi[i]){
            en_buyuk = dizi[i];
        }
    }
    return en_buyuk;
}

int main(){
    printf("%d",en_buyuk_eleman());
    return 0;
}
