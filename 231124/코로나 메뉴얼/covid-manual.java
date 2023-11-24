import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A_num = 0;

        char yn_1 = sc.next().charAt(0);
        int tem_1 = sc.nextInt();
        char yn_2 = sc.next().charAt(0);
        int tem_2 = sc.nextInt();
        char yn_3 = sc.next().charAt(0);
        int tem_3 = sc.nextInt();

        if (yn_1 == 'Y' && tem_1 >= 37) A_num += 1;
        if (yn_2 == 'Y' && tem_2 >= 37) A_num += 1;
        if (yn_3 == 'Y' && tem_3 >= 37) A_num += 1;

        if (A_num >= 2) {
            System.out.print("E");
        } else {
            System.out.print("N");
        }

    }
}