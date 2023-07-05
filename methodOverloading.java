import java.util.Scanner;

class methodOverloading {
    public static void main(String[] args) {
        int a,b;
        double c,d;
        System.out.println("ENTER THE VALUES OF a AND b:\n");
        Scanner in=new Scanner(System.in);
        a=in.nextInt();
        b=in.nextInt();
        System.out.println("ENTER THE VALUES OF c AND d:\n");
        Scanner inn=new Scanner(System.in);
        c=inn.nextDouble();
        d=inn.nextDouble();
     int r1 = minFunction(a, b);
     double r2 = minFunction(c,d);
     System .out.println("Minimum Value = " + r1);
     System .out.println("Minimum Value = " + r2);
    }
     public static int minFunction(int n1, int n2) {
     int min;
     if (n1 > n2)
     min = n2;
     else
     min = n1;
     return min;
    }
    public static double minFunction(double n1, double n2){
        double min;
        if(n1>n2)
        min=n2;
        else
        min=n1;
        return min;
    }
}