#include<stdio.h>

int sira1=1,sira2=500;
int islem1=1,islem2=500;


int  sira_al(int x){
	switch(x){
    case 1:	{
	printf("\n siraniz: %d",sira1);
	++sira1;
	if(sira1==500){
		sira1=0;}
		break;
	}
	case 2:{
	printf("\n siraniz: %d",sira2);
	++sira2;
	if(sira2==1001){
		sira2=500;}
		break;
}
	}
	}

int hizmet_ver(int x){
	switch(x){
	case 1:{

	if(islem1==sira1){
		printf("bekleyen sira yok.");
		return 0;
	}

	printf("\n %d numarali kisiye hizmet verebilirsiniz",islem1);
	++islem1;
	    if(islem1==500){
    	islem1=0;
	}	
	break;
}
	case 2:{
	if(islem2==sira2){
		printf("bekleyen sira yok.");
		return 0;
	}

	printf("\n %d numarali kisiye hizmet verebilirsiniz",islem2);
	++islem2;
	    if(islem2==1001){
    	islem2=500;
	}
	break;
}
}
}

int main(){
     
  int hizmet,islem;
  printf("islem turunuzu seciniz\n1.sira al \n2.hizmet ver");
  scanf("%d",&hizmet);
  switch(hizmet){
  
  case 1:{
  	printf("isleminizi seciniz\n1.havale, fatura odemesi ve cari hesap islemleri \n2.yatirim islemleri ve vadeli hesaplar");
    scanf("%d",&islem);
  	sira_al(islem);
	
	  }
  	
	break;

  
  case 2:{
  	
  	printf("isleminizi seciniz\n1.havale, fatura odemesi ve cari hesap islemleri \n2.yatirim islemleri ve vadeli hesaplar");
    scanf("%d",&islem);
  	sira_al(islem);
  	
	break;
  }
  
}
    
	return 0;
}
