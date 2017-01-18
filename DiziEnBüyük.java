
/*	Please Read the following case.

	My Array : {4, 8, 3, 1, 18, 9, 21, 20, 5, 17}
	Result   : Max = 21

	>>>Genel ifade<<<
  
	"Dizinin büyüğünü küçüğünü bulmak istersen 2 adımı takıp etmelisin"
	  1 ) ->Max veya min değerine dizinin ilk elemanı atılır
	  2 ) ->Tüm dizi for ile dolaşılır ve tek tek kontrol et.Eğer dolaşırken daha büyük değer bulursan max değerini güncelle.
    
*/
public class DiziEnBüyük {

	public static void main(String[] args)
	{
		//İnitialize the array.
		int [] a = {4, 8, 3, 1, 18, 9, 21, 20, 5, 17};

		int i, max, size;
		size = 10; // -> size of array

		max = a[0]; // -> Setting max [!Pay attention :always first value of a array]
		for (i = 1; i < size; ++i) {
			if (a[i] > max)
				max = a[i];
		}

		//İnformation about Result
		System.out.printf("Dizinin en büyük elemanı = %d\n", max);
	}
}
