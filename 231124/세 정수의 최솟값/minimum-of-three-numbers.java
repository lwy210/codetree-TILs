import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int minimum = a > (b > c ? c : b) ? (b > c ? c : b) : a;

        System.out.println(minimum);
    }
}