/* 
   Created by Hüseyin Karakullukçu on 19.01.2017
   Contact: karakullukcuhuseyin@gmail.com 
*/

// Basit bir node yaratıyoruz.
// İçinde bir veri ve sıradakı node'u tutan bir değişken tanımlıyoruz.
// Not: Element bir generic type. Yani onu biz uydurduk yerine herhangi bir veri yapısı gelebilir.
public class Node<Element> {
  init() {}
  var data: Element?
  var nextNode: Node<Element>?
}

// LinkedList sınıfımızı oluşturuyoruz.
public class LinkedList<Element> {
  // Iterator tanımlıyoruz.
  var iter: Node<Element>
  // Ve constant yani hiç değişmeyen bir root tanımlıyoruz.
  let root = Node<Element>()

  init() {
    // Iterator root ile aynı node'a bağlıyoruz.
    iter = root
  }

  // Basit bir listenin sonuna ekleme fonksiyonu. Herhangi bir veri tipini alıp
  // listenin sonuna ekliyoruz.
  func add(_ givenData: Element) {
    // Iterator'ı listenin son node'una kadar götürüyoruz.
    while iter.nextNode != nil {
      iter = iter.nextNode!
    }

    // Son node'a veriyi ekliyoruz.
    iter.data = givenData
    // Sıradaki node'u da tanımlıyoruz.
    iter.nextNode = Node<Element>()
  }

  // Belirtilen indeksten veri döndürme fonksiyonu. Bir sayı alıp, bir optional döndürüyor.
  func getItem(_ index: Int) -> Element? {
    // Döndüreceğimiz veriyi optional olarak tanımlıyoruz.
    // Böylece biz bir şey atamadıkça içerisindeki veri null olacak.
    var item: Element?
    // Iterator'ı en baş node'a getiriyoruz.
    iter = root
    // 0'dan verilen indekse kadar bir loop başlatıyoruz.
    for _ in 0..<index {
      // Iterator'ı verilen indekse kadar götürmeye çalışıyoruz.
      if iter.nextNode != nil {
        iter = iter.nextNode!
      } else {
        // Eğer null değer ile karşılaştıysak listede belirtilen indeks kadar uzun değil.
        // İçinde null olan item değişkenini döndürüyoruz ve fonksiyon bitiyor.
        return item
      }
    }
    // Buraya geldiysek indeks litenin içinde. Değeri iteme atayıp dönrüyoruz.
    item = iter.data
    return item
  }

}
