import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b, res;

        a = sc.nextInt();
        b = sc.nextInt();
        res = 1;

        for (int i=1; i<=b; i++) {
            if (i % a == 0) res *= i;
        } System.out.print(res);

        
    }
}