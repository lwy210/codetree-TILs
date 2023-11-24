import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int midterm = sc.nextInt();
        int finals = sc.nextInt();

        if (midterm >= 90 && finals >= 95) {
            System.out.print(100000);
        } else if (midterm >= 90 && finals >= 90) {
            System.out.print(50000) ;
        } else {
            System.out.print(0);
        }
    }
}