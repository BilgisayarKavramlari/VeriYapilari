#include <stdio.h>
#include <stdlib.h>

void dizi_olustur(int dizi[],int boyut){
    srand(time(NULL));
    for(int i=0;i<boyut;i++){
        dizi[i]=1+rand()%10;
    }
}
void yazdir(int dizi[],int boyut){
    for(int i=0;i<boyut;i++){
        printf("%d ",dizi[i]);
    }
    printf("\n");
}

void kabarcik_sirala(int dizi[],int boyut){
    int gecici;
    for(int i=0;i<boyut-1;i++){
        for(int j=i;j<boyut;j++){
            if(dizi[i]>dizi[j]){
                gecici=dizi[j];
                dizi[j]=dizi[i];
                dizi[i]=gecici;
            }
        }
    }
    yazdir(dizi,boyut);
}

int main(){
    
    int dizi[10];
    dizi_olustur(dizi,10);
    yazdir(dizi,10);
    kabarcik_sirala(dizi,10);
    return 0;
}
