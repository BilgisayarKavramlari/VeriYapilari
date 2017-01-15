#include <iostream>
using namespace std;

void bubbleSort(int arr[], int size)
{
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++) {
			if (arr[i] < arr[j]) swap(arr[i], arr[j]);
		}
	}
}

void bastir(int arr[], int size)
{
	for (int i = 0; i < size; i++)
	{
		cout << arr[i] << endl;
	}
}

int main()
{
	int arr[] = { 0,90,32,66,22,11,754,12,23,5 };
	int size = sizeof(arr) / sizeof(int);
	bubbleSort(arr, size);

	bastir(arr, size);
	return 0;
}
