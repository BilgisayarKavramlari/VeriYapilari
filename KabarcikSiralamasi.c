#include <stdio.h>
#include <conio.h>

int main(){
	int a[] = {2,3,6,3,4,1,9,8,2,6};
	int tmp; //temporary gecici
	int n = 10;
	for(int i=0;i<n;i++){
		for(int j=n-1;j>i;j--){
			if(a[j-1]>a[j]){
				tmp=a[j-1];
				a[j-1]=a[j];
				a[j]=tmp;
			}
		}
	}//duzenlenmis halini yazdiralim
	for(int x=0;x<n;x++){
		printf("%d ",a[x]);
	}
	getch();
}
