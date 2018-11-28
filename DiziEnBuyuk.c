#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int *randomarraygenerator(int length){
  int *arrptr=(int*)malloc(sizeof(int)*length);
  srand(time(NULL));
  for(int i=0; i<length; i++){
    *(arrptr+i)=rand()%100;
  }
  return arrptr;
}//parametre olarak gonderdigimiz uzunluk random bir liste yaratan ve bunun baslangic degerinin adresini geri donduren foksiyon

int maxvalue(int *arrptr,int length){
  int max=0;
  for(int i=0; i<length; i++){
    if(*(arrptr+i)>max){
      max=*(arrptr+i);
    }
  }
  return max;
}

int main(){
  int *arraypointer=NULL;
  int maximum;
  arraypointer=randomarraygenerator(20);
  maximum=maxvalue(arraypointer, 20);

  printf("%d",maximum);

  return 0;
}

