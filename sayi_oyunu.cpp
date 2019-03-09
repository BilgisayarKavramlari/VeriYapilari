#include<stdio.h>


int main(){
	
	int i,j1,j2,flag;
	j1=100;
	printf("1-%d arasi bir sayi giriniz:",j1);
	scanf("%d",&i);
	j1=j1/2;
	j2=j1/2;
	while(1){
		printf("Sayiniz %d mi?",j1);
		scanf("%d",&flag);
		if(flag==0){
			printf("aradiginiz sayi %d",j1);
			break;
		}
		else if(flag==1){
			j1=j1+j2;
			if(j2!=1){
					j2=j2/2;
			}
		}
		else if(flag==-1){
			j1=j1-j2;
			if(j2!=1){
					j2=j2/2;
			}
		}
	}
	
	return 0;
}
