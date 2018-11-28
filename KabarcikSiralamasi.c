#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int *randomarraygenerator(int length){
  srand(time(NULL));
  int *arrptr=(int*)malloc(sizeof(int)*length);
  for(int i=0; i<length; i++){
    *(arrptr+i)=rand()%100;
  }
  return arrptr;
}//parametre olarak gonderdigimiz uzunluk random bir liste yaratan ve bunun baslangic degerinin adresini geri donduren foksiyon

void swap(int *xptr, int *yptr){
  int temp=*xptr;
  *xptr=*yptr;
  *yptr=temp;
}//parametre olarak gonderdigimiz degerlerin adreslerinin yerini degistiriyoruz

void selectionsort(int *arrptr, int length){
  int min,i,j;
  for(i=0; i<length-1; i++){
    min=i;
    for(j=i+1; j<length; j++){
      if(arrptr[min]>arrptr[j]){
        min=j;
      }
    }
    swap(&arrptr[i], &arrptr[min]);
  }
  printf("list has sorted\n");
}//listemizi siralayan foksiyon

void print(int *arrptr, int length){
  for(int i=0; i<length; i++){
    printf("%d\t",*(arrptr+i));
  }
  printf("\n");
}

int main(){
  int length;
  printf("dizinin boyutu ne kadar olsun:"); scanf("%d",&length);
  int *arraypointer=randomarraygenerator(length);
  print(arraypointer, length);
  selectionsort(arraypointer, length); print(arraypointer, length);

  return 0;
}