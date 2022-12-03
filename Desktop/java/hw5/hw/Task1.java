import java.util.Scanner;
public class Task1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Введите дробное число:");
        try {
            float num = sc.nextFloat();
            System.out.println(num);
        } catch (java.util.InputMismatchException e) {
            System.out.println("Вы ввели не дробное число, попробуйте снова:");
        }
    }
    
}