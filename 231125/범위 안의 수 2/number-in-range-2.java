import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cnt, sum, temp;
        cnt = sum = 0;

        for (int i=0; i<10; i++) {
            temp = sc.nextInt();
            if (temp >= 0 && temp <= 200) {
                cnt += 1;
                sum += temp;
            }
        }
        System.out.printf("%d %.1f", sum, (double)sum/cnt);

    }
}