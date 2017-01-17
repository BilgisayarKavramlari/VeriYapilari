#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

struct n{
	int data;
	n * next;
};
typedef n node;

node * ekle(node * r, int data){
	//hic eleman olmama durumu 
	if(r==NULL){
		r = (node*)malloc(sizeof(node));
		r -> data = data;
		r -> next = NULL;
		return r;
	}
	//var olan elemanlarin ardina eklenme durumu
	else{
		node * iter = r;
		while(iter -> next != NULL){
			iter = iter -> next;
		}
		node * temp = (node*)malloc(sizeof(node));
		temp -> next = iter -> next;
		iter -> next = temp;
		temp -> data = data;
		return r;
	}
}

void bastir(node * r){
	while(r!=NULL){
		printf("%d ",r->data);
		r = r->next;
	}
	printf("\n");
}

int main(){
	node * root;
	root = NULL;
	root = ekle(root, 2);
	root = ekle(root, 3);
	root = ekle(root, 6);
	root = ekle(root, 3);
	root = ekle(root, 4);
	root = ekle(root, 1);
	root = ekle(root, 9);
	root = ekle(root, 8);
	root = ekle(root, 2);
	root = ekle(root, 6);	
	bastir(root);
	getch();
}
