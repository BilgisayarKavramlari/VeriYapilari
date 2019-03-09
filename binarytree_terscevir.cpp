#include<stdio.h>
#include<stdlib.h>

typedef struct n{
	 int x;
	 n * right;
	 n * left;
	 
	
}node;


node * ekle(node * tree,int x){
	if(tree==NULL){
		node * root=(node*)malloc(sizeof(node));
		root->x=x;
		root->left=NULL;
		root->right=NULL;
		return root;
	}
	if(tree->x < x){
		tree->right=ekle(tree->right,x);
		return tree;
	}
	else{
		tree->left=ekle(tree->left,x);
		return tree;
	}
	
	
	
}

void yazdir(node * tree){//RNL yazdırma büyükten küçüğe doğru yazdırır.
	if(tree==NULL){
		return;
	}
	yazdir(tree->right);
	printf("%d",tree->x);
	yazdir(tree->left);
}

node* ters_cevir(node * tree){
	if(tree==NULL){
		return tree;
	}
	node * temp;
	temp=tree->right;
	tree->right=tree->left;
	tree->left=temp;
	tree->left=ters_cevir(tree->left);
	tree->right=ters_cevir(tree->right);
	return tree;
}



int main(){
	
	node * tree;
	tree=NULL;
	tree=ekle(tree,10);
	yazdir(tree);
	tree=ekle(tree,20);
	yazdir(tree);
	tree=ekle(tree,30);
	yazdir(tree);
	tree=ekle(tree,40);
	yazdir(tree);
	tree=ters_cevir(tree);
	yazdir(tree);
	
	
	return 0;
}
