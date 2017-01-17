import java.util.ArrayList;

// Queue basit bir veri tipidir. İlk giren veri ilk çıkar.
public class Queue<V> {
    // Sırayı tutacağımız bir ArrayList tanımlıyoruz.
    ArrayList<V> arrayList = new ArrayList<>();
    
    // Sıraya veri eklemeye yarayan fonksiyon.
    public void push(V veri) {
        // Listeye veriyi ekliyoruz.
        arrayList.add(veri);
    }
    
    // Sıradan veri çıkarmaya yarayan fonksiyon.
    public V pop() {
        // İlk giren veriyi alıp bir değişkene atıyoruz.
        V response = arrayList.get(0);
        // Daha sonra ilk veriyi listeden siliyoruz.
        arrayList.remove(0);
        // Veriyi çağırana gönderiyoruz.
        return response;
    }
}
