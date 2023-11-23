import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.useDelimiter("-");

        int d = sc.nextInt();
        int m = sc.nextInt();
        int y = sc.nextInt();

        System.out.printf("%d.%d.%d", y, d, m);
    }
}