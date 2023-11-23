import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String s = sc.next();
        String[] str_arr = s.split("-");
        
        System.out.print(str_arr[0] + str_arr[1]);
    }
}