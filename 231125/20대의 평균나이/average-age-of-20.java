import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, sum, temp;
    
        n = sum = 0;

        while (true) {
            temp = sc.nextInt();
            if (temp >= 30) break;
            else {
                sum += temp;
                n += 1;
            }
        }
        System.out.printf("%.2f", (double)sum/n);
    }
}