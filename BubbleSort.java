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
