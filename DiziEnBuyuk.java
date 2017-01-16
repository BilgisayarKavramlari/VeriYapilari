/**
 * Created by ahmetturkmen on 1/15/17.
 */
public class DiziEnBuyuk {

    public static void main(String[] args){
        int temp=0;
        int [] dizi = {2,3,6,3,4,1,9,8,2,6};
        for (int i = 0; i <dizi.length; i++) {
            if(dizi[i]>temp){
                temp=dizi[i];
            }
        }
            System.out.printf("%d",temp);
    }
}
