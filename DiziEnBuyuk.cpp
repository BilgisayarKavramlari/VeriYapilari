#include<iostream>
#include<time.h>
using namespace std;

int main()
{
  srand(time(0)); // random besleme fonksiyonu
  
  int temp=NULL;
  
  int dizi[10];   // dizi tanımlama
    
  for(int i=0;i<10;i++)   // diziye rastgele deger atama dongusu
  dizi[i]=rand()%10+1;    // 0-10 (dahil) arasında deger ata.
  
  cout<<"--------Before--------"<<endl;
  for(int i=0;i<10;i++)                   // diziyi ekrana bas.
  cout<<dizi[i]<<" ";
  
  cout<<endl<<"--------After--------"<<endl;
  
  temp=dizi[0];
  
  for(int i=0;i<10;i++)
  {
      for(int j=0;j<10;j++)
      {
         if(dizi[i] < dizi[j])    
         {
            temp=dizi[j];
            dizi[j]=dizi[i];          // yer degistirme islemleri yapiliyor.
            dizi[i]=temp;
            
         }
      }
  }
  for(int i=0;i<10;i++)                   // diziyi ekrana bas.
  cout<<dizi[i]<<" ";
  
  
  
  

return 0;
}
