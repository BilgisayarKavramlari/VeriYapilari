#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
	int data;
	struct node * next;
}NODE;

NODE * yeniNodeYarat(int data)
{
	NODE * yeniNode = (NODE *)malloc(sizeof(NODE));
	if (yeniNode == NULL)
	{
		printf("Yeni Node Yaratilamadi.");
		exit(0);
	}
	yeniNode->data = data;
	yeniNode->next = NULL;
	return yeniNode;
}

NODE * Ekle(NODE * liste, int* tamSayiDizisi, int elemanSayisi)
{
	NODE * yurume = liste;
	
	for (int i = 0; i < elemanSayisi; i++)
	{
		if (liste == NULL)
		{
			liste = yeniNodeYarat(tamSayiDizisi[i]);
			yurume = liste;
		}
		else
		{
			yurume->next = yeniNodeYarat(tamSayiDizisi[i]);
			yurume = yurume->next;
		}
	}
	return liste;
}

void ekranaBastir(NODE * liste)
{
	while (liste->next != NULL)
	{
		printf("%d -> ", liste->data);
		liste = liste->next;
	}
	printf("NULL");
}

int main()
{
	NODE * bagliListe = NULL;
	int arr[10] = { 5,9,10,100,43,2,77,123,54,93 };

	bagliListe = Ekle(bagliListe, arr, 10);
	ekranaBastir(bagliListe);
	return 0;
}
