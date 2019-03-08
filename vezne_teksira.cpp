#include<stdio.h>

int sira=1;
int islem=1;

int  sira_al(){
	printf("\n siraniz: %d",sira);
	++sira;
	if(sira==1001){
		sira=0;
	}
}
int hizmet_ver(){
	if(islem==sira){
		printf("bekleyen sira yok.");
		return 0;
	}

	printf("\n %d numarali kisiye hizmet verebilirsiniz",islem);
	++islem;
	    if(islem==1001){
    	islem=0;
	}
}

int main(){

    sira_al();
    sira_al();
    sira_al();
    sira_al();
    hizmet_ver();
    hizmet_ver();
    hizmet_ver();
    sira_al();
    sira_al();
    sira_al();
    sira_al();
    sira_al();
    sira_al();
    hizmet_ver();
    

	return 0;
}
