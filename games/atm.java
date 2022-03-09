import java.util.Scanner;


class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    System.out.println("Welcome to the Geek Education ATM!");

    double balance = 0;
    
    while(true){
      System.out.println("----------------------------");
      System.out.print("Enter a command: 'w' for withdrawal, 'd' for deposit, 'c' for check balance and 'q' to quit the application: ");

      String cmd = input.nextLine();

      if(cmd.equals("q")){
        break;
      } else if(cmd.equals("d")){
        
        System.out.print("How much would you like to deposit? ");
        double amt = input.nextFloat();
        input.nextLine();

        while(amt <= 0){
          System.out.print("Must enter a value greater than 0. Please enter a new amount. ");
          amt = input.nextFloat();
          input.nextLine();
        }

        balance += amt;
        System.out.println("Successfully deposited your funds.");
        
      } else if(cmd.equals("w")){

        System.out.print("How much would you like to withdraw? ");
        double amt = input.nextFloat();
        input.nextLine();

        while(amt <= 0){
          System.out.print("Must enter a value greater than 0. Please enter a new amount. ");
          amt = input.nextFloat();
          input.nextLine();
        }

        while(amt > balance){
          System.out.print("Insufficient funds. Please enter a new amount. ");
          amt = input.nextFloat();
          input.nextLine();
        }

        balance -= amt;
        System.out.println("Successfully withdrew your funds.");
        
      } else if(cmd.equals("c")){
        System.out.println("Your balance is $" + balance);
        
      } else {
        System.out.println("Invalid command. Try again.");
      }

      System.out.println();
    }

    System.out.println();
    System.out.println("Thanks for using Geek Education ATM.");
    input.close();
  }
}