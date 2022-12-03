package hw;

public class Task4 {
    public static void main(String[] args) {
        name(null);
    }
    public static void name(Integer a){
        try {
            System.out.println(a.toString());
        } catch (NullPointerException e) {
            System.out.println("Строка не может быть пустой");
        }

    }
}
