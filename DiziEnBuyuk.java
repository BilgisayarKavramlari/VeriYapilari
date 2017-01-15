
package dizienbuyuk;

import java.util.Random;
public class DiziEnBuyuk 
{
    public static void main(String[] args)
    {
     int a[] = new int[10];
        Random r = new Random();
        for (int i = 0; i < 10; i++)
        {
           
            a[i]=r.nextInt(1000);
            System.out.println(a[i]);

        }
     int enbuyuk=a[0];
        for (int i = 0; i < 10; i++)
        {
            if (a[i]>enbuyuk) 
            {
                enbuyuk=a[i];    
            }
        }
                    System.out.println("En Büyük Sayı: "+enbuyuk);
    }
}
