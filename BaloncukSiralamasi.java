/**
 * Created by ahmetturkmen on 1/15/17.
 */
public class BaloncukSiralamasi {

    public static void main(String[] args) {

        int[] dizi = {2,3,6,3,4,1,9,8,2,6};

        siralamayiGerceklestir(dizi);
        for (int i = 0; i < dizi.length; i++) {
            System.out.printf(dizi[i] + " ");

        }
    }

    private static void siralamayiGerceklestir(int[] dizi) {
        int geciciDegisken =0;
        for (int i = 0; i < dizi.length; i++) {

            for (int j = 1; j < (dizi.length - i); j++) {
                if (dizi[j - 1] > dizi[j]) {
                    geciciDegisken = dizi[j - 1];
                    dizi[j - 1] = dizi[j];
                    dizi[j] = geciciDegisken;
                }
            }
        }


    }
}
