import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    String[] menu = {"Coffee", "Tea", "Donut", "Bagel", "Sandwich"};
    int[] prices = {1, 1, 2, 4, 7};
    
    System.out.println("Welcome to the Geek Education Coffee Shop!");
    System.out.println("Take a look at our menu:");

    for(int i = 0; i < menu.length; i++){
      System.out.println("- " + menu[i] + " - $" + prices[i]);
    }
    System.out.println("Enter 'quit' when you are finished your order.");
    System.out.println();

    int total = 0;
    while(true){
      System.out.print("What item would you like to order? ");
      String item = input.nextLine();

      if(item.equals("quit")){
        break;
      }

      int index = isOnMenu(menu, item);
      if(index == -1){
        System.out.println("That item is not on our menu.");
        System.out.println();
        continue;
      }

      System.out.print("How many would you like? ");
      int quantity = input.nextInt();
      input.nextLine();

      while(quantity <= 0){
        System.out.print("You must order at least 1. How many would you like? ");
        quantity = input.nextInt();
        input.nextLine();
      }

      System.out.println("Added " + item + " x" + quantity + " to your cart.");
      total = total + (prices[index] * quantity);

      System.out.println();
    }    

    System.out.println("Your total is $" + total);
    System.out.println("Thanks for choosing the Geek Education Coffee Shop! Please come again.");

    input.close();
  }

  public static int isOnMenu(String[] menu, String item){
    for(int i = 0; i < menu.length; i++){
      if(item.toLowerCase().equals(menu[i].toLowerCase())){
        return i;
      }
    }

    return -1;
  }
}