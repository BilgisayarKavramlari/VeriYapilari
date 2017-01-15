#include <iostream>
using namespace std;

struct Node{ //Düğüm yapısı
	int data;
		Node * next;
		Node(int data = int(), Node * next = NULL){
			this->data = data;
			this->next = next;
		}
};

class LinkedList{ //BağlıListe Sınıfı
	private: 
		Node * root; //Listeyi gösteren baş düğüm 
		int size;
		
	public:
		LinkedList(){
			root = new Node();
		}
		Node * firstNode(){ //Baş düğümün gösterdiğini düğümü döndürür
			return root->next;
		}
		void add(const int& newData){ //int değerini listeye ekler
			Node * tmp = root;
			while(tmp->next != NULL){
				tmp = tmp->next;
			}
			tmp->next = new Node(newData);
		}
		void addArray(int array[],int len){ //Diziyi alır ve listeye ekler
			for(int i=0;i<len;i++){
				this->add(array[i]);
			}
		}
		const int& get(int location){ //Belirtilen konumdaki düğümün verisini döndürür
			int index = 0;
			Node * tmp = root;
			while(tmp->next != NULL && location!=index++){
				tmp = tmp->next;
			}
			return tmp->data;
		}
		
		friend ostream& operator<<(ostream& screen, LinkedList &right){ //<< operatörünün aşırı yüklenmesi 
			Node * node = right.firstNode();						//bütün listeyi ekrana basar
			while(node->next!= NULL){
				screen<<node->data<<" ";
				node = node->next;
			}
			screen<<node->data;
			return screen;
		}
};

int main(){
	int arrayLength;
	LinkedList * list = new LinkedList();
	
	cout<<"Listeye kac deger ekliyeceksiniz? : ";
	cin>>arrayLength;
	int intArray[arrayLength];
	
	for(int i=0;i<arrayLength;i++){
		cout<<i+1<<". Degeri giriniz : ";
		cin>>intArray[i];
	}
	
	list->addArray(intArray,arrayLength);
	
	cout<<*list;
	
	
	return 0;
}
