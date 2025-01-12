import java.util.Scanner;

public class UnitConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Unit Converter");
        System.out.println("1. Kilometers to Miles");
        System.out.println("2. Miles to Kilometers");
        System.out.print("Choose an option: ");
        int choice = scanner.nextInt();

        switch (choice) {
            case 1:
                System.out.print("Enter kilometers: ");
                double kilometers = scanner.nextDouble();
                double miles = kilometers * 0.621371;
                System.out.println(kilometers + " kilometers is equal to " + miles + " miles.");
                break;
            case 2:
                System.out.print("Enter miles: ");
                double milesInput = scanner.nextDouble();
                double kilometersResult = milesInput / 0.621371;
                System.out.println(milesInput + " miles is equal to " + kilometersResult + " kilometers.");
                break;
            default:
                System.out.println("Invalid choice.");
                break;
        }

        scanner.close();
    }
}