#include <iostream>

using namespace std;
int main()
{
//////örnek giriş;
//////10
//////39 49 20 49 20 19 483 291 49 43
	int min = 0, max = 0, mi =0, ma=0;
	int arc; cin >> arc;
	int *arr;
	arr = new int[arc];
	for (int i = 0; i < arc; i++)
	{
		cin >> arr[i];
		if (arr[i] > max) { max = arr[i]; ma = i; }
		if (i == 0)min = arr[i];
		if (arr[i] < min) { min = arr[i]; mi = i; }
	}
	cout << min << " " << max;
	return 0;
}
