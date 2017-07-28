class DizidekiEnBuyukDeger
{
    public static void main(String[] args) 
    {
        int enBuyuk = 0; //en büyük sayının tutulacağı değişkeni tanımladık
        int[] dizi = {2,8,3,7,5}; //dizimizi tanımlayıp değerlerini atadık
        
        for (int i = 0; i < dizi.length; i++) //dizinin eleman sayısı kadar dönecek for döngüsünü yazdık
        {
            if (dizi[i] > enBuyuk) //buradaki "if" bloğu, dizideki elemanlardan "enBuyuk" değişkenindeki değerden büyükse "enBuyuk" değişkenine -->  
            {
                enBuyuk = dizi[i]; // --> burada eşitleyerek dizideki en büyük değeri buluyor
            }
        }
        
        System.out.println("Dizideki en büyük sayı = " + enBuyuk); //dizideki en büyük sayıyı da burada yazdırdık
    }
}
