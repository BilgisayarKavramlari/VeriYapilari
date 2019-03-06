#include<stdio.h>


int main(){
	int i,j,sutun,satir;
	printf("sutun sayisini giriniz:");
	scanf("%d",&sutun);
	printf("satir sayisini giriniz:");
	scanf("%d",&satir);
	
	for(i=0;i<satir;i++){
		for(j=0;j<sutun;j++){
			if((j+i)%2==0){
				printf("0");
			}
			else{
				printf("1");
			}
		}
		if(i!=satir-1){
			printf("\n");
		}
	}
	
	return 0;
}
