public class Main {
    public static void main(String[] args) {
        double ft_cm, ft, mi;
        int mi_cm;
        ft_cm = 30.48; mi_cm = 160934;
        ft = 9.2; mi = 1.3;

        System.out.printf("%.1fft = %.1fcm\n", ft, ft * ft_cm);
        System.out.printf("%.1fmi = %.1fcm\n", mi, mi * mi_cm);
    }
}