#include <stdio.h>
#include <conio.h>

int main(){
	int girilen;
	int eb = 0;
	printf("10 tane sayi giriniz: ");
	for(int i=0;i<=10;i++){
		scanf("%d",&girilen);
		if(girilen>eb){
			eb = girilen;
		}
	}
	printf("girdiginiz sayilardan en buyugu: %d",eb);
	getch();
}
