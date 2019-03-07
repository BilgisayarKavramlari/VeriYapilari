#include<stdio.h>


int ust_al(int taban,int ust){//üst alma fonksiyonu
	if(ust==0){
		return 1;
	}
	int x,i;
	x=1;
	for(i=0;i<ust;i++){
		x=x*taban;
	}
	return x;
}

int basamak(int x){//int değeri ile sınırlı en fazla 9 basamak gösteriyor.
	int i;
	if(x==0){
		return 1;
	}
	for(i=1;1;i++){
		if(x/ust_al(10,i)==0){
			break;
		}
	}
	return i;
}

int basamak_sayi(int x,int basamak1){//x sayısının istenilen basamağındaki değerini gösteren fonksiyon.
	int i1,i2,i3;
	i3= basamak(x);
	for(i1=i3;i1>=basamak1;i1--){
		i2=x%(ust_al(10,i1));
	}
	i2=i2/(ust_al(10,i1));
	return i2;
	
}

void palindrom(int x){

	int i1,i2,i3,basamak1;
	basamak1=basamak(x);
	i3=(basamak1 / 2); //sayının sağındaki veya solundaki basamak değeri
	for(i1=0;i1<i3;i1++){
		if((basamak_sayi(x,i1+1)) != (basamak_sayi(x,basamak1-i1))){
			printf("Bu sayi palindrom degildir.");
			return;
		}
	}
	printf("Bu sayi palindromdur.");
}




int main(){
	
    int x;
    scanf("%d",&x);
    palindrom(x);
	
	
	
	return 0;
}
