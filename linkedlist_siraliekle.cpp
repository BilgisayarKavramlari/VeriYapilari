#include<stdio.h>
#include<stdlib.h>

typedef struct n{
	int x;
	n * next;
	n * prev;
}node;

node* sirali_ekle(node *root,int a){
	if(root==NULL){
		node * temp;
		temp=(node*)malloc(sizeof(node));
		temp->next=NULL;
		temp->prev=NULL;
		temp->x=a;
		return temp;
	}
	if(root->x > a){
		node * temp;
		temp=(node*)malloc(sizeof(node));
		temp->next=root;
		temp->prev=NULL;
		temp->x=a;
		return temp;
	}
	node * iter;
	iter=root;
	while((iter->next != NULL) && (iter->next->x < a)){
		iter=iter->next;
	}
	if(iter->next==NULL){
		node * temp;
		temp=(node*)malloc(sizeof(node));   
		temp->next=iter->next;
		temp->prev=iter;
		iter->next=temp;
		temp->x=a;
		return root;
	
	}
	else{
	
		node * temp;
		temp=(node*)malloc(sizeof(node));   
		temp->next=iter->next;
		temp->next->prev=temp;
		temp->prev=iter;
		iter->next=temp;
		temp->x=a;
		return root;
		}
	
	int main(){
	
	node * root;
	root=(node*)malloc(sizeof(node));
	root->x=15;
    root->next=NULL;
    root->prev=NULL;
	root=sirali_ekle(root,40);
    root=sirali_ekle(root,200);
    root=sirali_ekle(root,250);
    root=sirali_ekle(root,17);
    root=sirali_ekle(root,150);
	
	return 0;
}
	

}
