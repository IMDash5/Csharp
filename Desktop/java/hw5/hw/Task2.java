package hw;

public class Task2 {
    public static void main(String[] args) {
        int[] intArray = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        try {
            int d = 0;
            double catchedRes1 = intArray[10] / d;
            System.out.println("catchedRes1 = " + catchedRes1);
            } 
            catch (ArithmeticException e) {
            System.out.println("Catching exception: " + e);
            }
            catch (ArrayIndexOutOfBoundsException e){
                System.out.println("Индекс массива слишком большой");
            }
         
    }
    
}