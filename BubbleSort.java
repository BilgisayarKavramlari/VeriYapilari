public class Sorting 
{
    public static void bubbleSort(int[] a)
    {
        int hold;
        boolean swapped;

        for(int pass=0; pass<a.length-1; pass++)
        {
            swapped = false;
            for(int i=0; i<a.length-1; i++)
            {
                if(a[i] > a[i+1])
                {
                    hold = a[i];
                    a[i] = a[i+1];
                    a[i+1] = hold;
                    
                    swapped = true;
                }
            }
            
            if(swapped == false)
                break;
        }
    }  
    
}

import java.util.Arrays;

public class TestSorting 
{
    public static void main(String[] args) 
    {
        System.out.println("*******************Bubble Sort****************************");
        
        int[] myArray_1 = {10, 1, 7, 19, 3, 14, 6, 8, 13, 17};
		
        System.out.println("Before sorting myArray_1 : " + Arrays.toString(myArray_1));

        Sorting.bubbleSort(myArray_1);

        System.out.println("After sorting myArray_1  : "  + Arrays.toString(myArray_1));      
    }
}
