import java.util.Scanner;

public class MailAyirma 
{
    public static void main(String[] args) 
    {
        Scanner girdi = new Scanner(System.in);
        System.out.print("Mail giriniz = ");
        String mail = girdi.next();
        
        System.out.println("Kullanıcı = " + mail.substring(0,mail.indexOf("@")));
        System.out.println("Host = " + mail.substring(mail.indexOf("@")+1, mail.length()));
    }
}
