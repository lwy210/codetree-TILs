import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, a, b, c;

        a = b = c = 0;
        n = sc.nextInt();

        for (int i=1; i<=n; i++) {
            if (i % 12 == 0) c += 1;
            else if (i % 3 == 0) b += 1;
            else if (i % 2 == 0) a += 1;
        }

        System.out.print(a + " " + b + " " + c);


        
    }
}