import java.util.Scanner;
import java.util.Random;

class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    Random rand = new Random();

    System.out.println("Welcome to the advanced guessing game!");
    System.out.println("What is the maximum number you can guess?");
    int maxNumber = input.nextInt();
    input.nextLine();

    System.out.println("How many guesses do you have?");
    int numGuesses = input.nextInt();
    input.nextLine();

    int goldenNumber = rand.nextInt(maxNumber) + 1;
    System.out.println();

    for(int i = 1; i <= numGuesses; i++){
      System.out.println("Round " + i + " of " + numGuesses + ":");
      System.out.println("Please enter your guess between 1 and " + maxNumber + ":");
      int guess = input.nextInt();
      input.nextLine();

      if(guess == goldenNumber){
        System.out.println("That's correct! You win!");
        System.exit(0);
      }

      System.out.println("Incorrect! Try again.");
      System.out.println();
    }

    System.out.println("You ran out of guesses! The correct number was " + goldenNumber);

    input.close();
  }
}