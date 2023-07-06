import java.util.Scanner;

public class methodOverloading {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter two integers
        System.out.println("Enter two integer values:");
        int a = scanner.nextInt();
        int b = scanner.nextInt();

        // Prompt the user to enter two doubles
        System.out.println("Enter two double values:");
        double c = scanner.nextDouble();
        double d = scanner.nextDouble();

        // Call the minFunction method with integer and double parameters
        int minInt = minFunction(a, b);
        double minDouble = minFunction(c, d);

        // Print the minimum values returned by the minFunction method
        System.out.println("Minimum value of integers: " + minInt);
        System.out.println("Minimum value of doubles: " + minDouble);
    }

    // Method to find the minimum of two integers
    public static int minFunction(int n1, int n2) {
        int min;
        if (n1 > n2)
            min = n2;
        else
            min = n1;
        return min;
    }

    // Method to find the minimum of two doubles
    public static double minFunction(double n1, double n2) {
        double min;
        if (n1 > n2)
            min = n2;
        else
            min = n1;
        return min;
    }
} 