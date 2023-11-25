import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean res = true;
        int temp;

        for (int i=0; i<5; i++) {
            temp = sc.nextInt();
            if (temp % 3 != 0) res = false;
        }

        if (res == true) System.out.print(1);
        else System.out.print(0);

    }
}