// Create Date: 2021-01-06 22:00:00

import java.util.Scanner; // Import the Scanner class from the java.util package

public class AreaCircleInheritance {
    /*
    This is a program that has superclass AreaCircleInheritance and subclass AreaRectangle.
    The superclass has a method that calculates the area of a circle and the subclass has a method that calculates the area of a rectangle.
    The subclass inherits the superclass and uses the method to calculate the area of a rectangle.
    */
    public static void main(String[] args) {
        AreaRectangle areaRectangle = new AreaRectangle(); // Create an object of the AreaRectangle class
        areaRectangle.areaCircle(); // Call the areaCircle method of the AreaRectangle class
        areaRectangle.areaRectangle(); // Call the areaRectangle method of the AreaRectangle class
    }

    public static class AreaCircle {
        public void areaCircle() {
            double area;
            int radius;
            double pi = 3.14; // Declare and initialize the value of pi
            System.out.println("Enter the radius of the circle: ");
            Scanner in = new Scanner(System.in); // Create a Scanner object to read input from the user
            radius = in.nextInt(); // Read the radius from the user
            area = pi * radius * radius; // Calculate the area of the circle
            System.out.println("Area of the circle is: " + area); // Print the area of the circle
        }
    }

    public static class AreaRectangle extends AreaCircle {
        public void areaRectangle() {
            int length;
            int breadth;
            System.out.println("Enter the length of the rectangle: ");
            Scanner in = new Scanner(System.in); // Create a Scanner object to read input from the user
            length = in.nextInt(); // Read the length from the user
            System.out.println("Enter the breadth of the rectangle: ");
            breadth = in.nextInt(); // Read the breadth from the user
            int area = length * breadth; // Calculate the area of the rectangle
            System.out.println("Area of the rectangle is: " + area); // Print the area of the rectangle
        }
    }
}