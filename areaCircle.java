import java.util.Scanner;
public class areaCircle {
        public static void main(String[] args) {
        double area;
        int radius;
        double pi = 3.14;
        System.out.println("Enter the radius of the circle: ");
        Scanner in = new Scanner(System.in);
        radius = in.nextInt();
        area = pi * radius * radius;
        System.out.println("Area of the circle is: " + area);
    }  
}
