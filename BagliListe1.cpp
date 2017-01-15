#include<iostream>
using namespace std;

// tek yonlu bagli liste isimizi gorecektir.

class Dugum
{
public: 
	int data;
	Dugum* next;

	Dugum()
	{
		data = NULL;
		next = NULL;
	}
};


void Ekle(Dugum*, int);

void Bas(Dugum*);

Dugum* kok = NULL;

int main()
{
		 
	int index = NULL;

	cout << "Kac eleman gireceksiniz :";
	
	cin >> index;
	
	system("cls");
	
	cout << "Elemanlar :";

	int* dizi = new int[index];		// heap alanda girilen index kadar dizi olustur.

	for (int i = 0;i < index;i++)cin >> dizi[i];		// kullanicidan elemanlari al

	system("cls");

	for (int i = 0;i < index;i++)
	{
		Ekle(kok, dizi[i]);		// her bir elemani bagli listeye ekle
	}

	Bas(kok);		// diziyi ekrana bas

	delete[] dizi;		// heap alandaki diziyi kaldir
	delete kok;			// bagli listeyi heap den kaldir.


	return 0;
}
void Ekle(Dugum* lb, int veri)
{
	Dugum* yeni = new Dugum();

	yeni->data = veri;
	
	Dugum* iter = lb;

	if (kok == NULL)
	{
		kok = yeni;
		return;
	}

	while (iter->next != NULL)
	
	{
	
		iter = iter->next;
	}

	iter->next = yeni;
	

}
void Bas(Dugum* lb)
{
	Dugum* iter = lb;
	
	while (iter!= NULL)
	{
		cout << iter->data << " ";
	
		iter = iter->next;
	} 
	cout << endl;
}
