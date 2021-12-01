#include <stdio.h>

int main()
{
    int array[10] = {2,3,6,3,4,1,9,8,2,6};

    int len = (int)(sizeof(array)/sizeof(array[0]));
    
    for(int j = 0; j<len; j++)
    {
        for(int i= 0; i < len-1; i++)
        {
            if (array[i] > array[i+1])
            {
                int temp = array[i];
                array[i] = array[i+1];
                array[i+1] = temp;
            }
        }
    }
    for(int i= 0; i < len; i++)
    {
        printf("%d ", array[i]);
    }
    
return 0;
}
