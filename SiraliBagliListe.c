#include <stdio.h>
#include <stdlib.h>

typedef struct Node_type
{
    int node_data;
    struct Node_type * node_next;
}Node_type;

//Return root
Node_type* add_list(Node_type* root, int data)
{
    Node_type * iter = (Node_type*)malloc(sizeof(Node_type));
    iter = root;
    if(0 == iter->node_data)
    {
        //iter = (Node_type*)malloc(sizeof(Node_type));
        iter->node_next = NULL;
        iter->node_data = data;
        return root;
    }
    else if(data <= iter->node_data)
    {
        Node_type * temp = (Node_type*)malloc(sizeof(Node_type));
        temp->node_data = data;
        temp->node_next = root;
        return temp;
    }
    else
    {
        while((NULL != iter->node_next) && (data >= iter->node_next->node_data))
        {
            iter = iter->node_next;
        }
        Node_type * temp = (Node_type*)malloc(sizeof(Node_type));
        temp->node_next = iter->node_next;
        iter->node_next = temp;
        temp->node_data = data;
        return root;
    }
}

void print_list(Node_type* root)
{
    while (NULL != root)
    {
        printf("%d ",root->node_data);
        root = root->node_next;
    }
    printf("\n");
}
int main()
{
    int array[10] = {2,3,6,3,4,1,9,8,2,6};
    int len = (int)(sizeof(array)/sizeof(array[0]));
    Node_type * root;
    root = (Node_type*)malloc(sizeof(Node_type));
    root->node_data = 0;
    root->node_next = NULL;
    for(int i = 0; i < len; i++)
    {
        //printf("Array element = %d\n", array[i]);
        root = add_list(root, array[i]);
    }
    print_list(root);
    return 0;
}
