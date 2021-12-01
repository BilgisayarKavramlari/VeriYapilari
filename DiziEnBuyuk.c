#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    time_t t;
    int array[10];
    int max;

    srand((unsigned)time(&t));
    for(int i = 0; i<10; i++)
    {
        array[i] = (rand()%100);
        printf("%d ", array[i]);
    }
    printf("\n");
    max = array[0];
    for(int i = 0; i<10; i++)
    {
        if(max < array[i])
        {
            max = array[i];
        }
    }

    printf("Biggest number in array: %d\n", max);

    return 0;
}
