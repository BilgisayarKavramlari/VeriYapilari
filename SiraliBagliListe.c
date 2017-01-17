#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

struct n{
	int data;
	n * next;
};
typedef n node;

node * ekleSirali(node *r, int data){
	//hic eleman olmama durumu 
	if(r==NULL){
		r = (node*)malloc(sizeof(node));
		r -> next = NULL;
		r -> data = data;
		return r;
	}
	//en basa eklenme durumu
	if(r -> data > data){
		node * temp = (node*)malloc(sizeof(node));
		temp -> data = data;
		temp -> next = r;
		return temp;
	}
	//sona veya ortaya eklenme durumu
	node * iter = r; 
	while(iter -> next != NULL && iter -> next -> data < data){
		iter = iter -> next;
	}
	node * temp = (node*)malloc(sizeof(node));
	temp -> next = iter -> next;
	iter -> next = temp;
	temp -> data = data;
	return r;
}

void bastir(node *r){
	while(r != NULL){
		printf("%d ",r->data);
		r = r -> next;
	}
	printf("\n");
}

int main(){
	node * root;
	root = NULL;
  //projects kisminda verilen sayilar sirasi ile:
	root = ekleSirali(root,2);
	root = ekleSirali(root,3);
	root = ekleSirali(root,6);
	root = ekleSirali(root,3);
	root = ekleSirali(root,4);
	root = ekleSirali(root,1);
	root = ekleSirali(root,9);
	root = ekleSirali(root,8);
	root = ekleSirali(root,2);
	root = ekleSirali(root,6);
	bastir(root);
	getch();
}
