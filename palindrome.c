#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {

	if(argc!=2){
		fprintf(stderr,	"Kullanım: %s <sayı>\n", argv[0]);
		return	(EXIT_FAILURE);
	}

	int sayi, basamak = 0, sabit;
	char *dizi = NULL;
	sayi = atoi(argv[1]);

	if ( sayi < 10 ) {
		printf("Tek basamaklı sayılar her zaman Palindrome'dur !\n\n");
		return (EXIT_SUCCESS);
	}
	while(10 <= sayi) {
		sayi /= 10;
		basamak++;
	}
	dizi = (char*)malloc(sizeof(char)*basamak);

	for (sabit = basamak; 0 <= basamak; --basamak) {
		dizi[sabit - basamak] = argv[1][basamak];
	}
	sayi = 1;
	
	for (int i = 0; i <= sabit; ++i) {
		if(argv[1][i] != dizi[i])
		{ sayi = 0; break;}
	}
	if ( sayi == 1 )
	{ printf("Sayi Palindrome'dur !\n\n"); }
	else
	{ printf("Sayi Palindrome değildir!\n\n"); }

	return (EXIT_SUCCESS);
}
