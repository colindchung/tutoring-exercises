public import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    
    while(true){
      System.out.println();  
      System.out.print("Enter your first number: ");  
      int num1 = input.nextInt();
      input.nextLine();
      System.out.print("Enter your operator (+, -, * or /): ");  
      String operator = input.nextLine();
      System.out.print("Enter your second number: "); 
      int num2 = input.nextInt();
      input.nextLine();

      if(operator.equals("+")){
        System.out.println("The answer is: " + (num1+num2));
      } else if(operator.equals("-")){
        System.out.println("The answer is: " + (num1-num2));
      } else if(operator.equals("*")){
        System.out.println("The answer is: " + (num1*num2));
      } else if(operator.equals("/")){
        System.out.println("The answer is: " + ((double)num1/(double)num2));
      } else {
        System.out.println("Invalid operator.");
      }

      System.out.println("----------------");
    }
  }
}
