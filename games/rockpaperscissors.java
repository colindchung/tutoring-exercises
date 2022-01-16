import java.util.Scanner;
import java.util.Random;

class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    Random rand = new Random();
    String[] moves = {"rock", "paper", "scissors"};
    
    System.out.println("How many games do you want to play?: ");
    int numGames = input.nextInt();
    input.nextLine();

    int wins = 0, losses = 0, ties = 0;

    for(int i = 1; i <= numGames; i++){
      System.out.println("Round " + i + " of " + numGames);

      System.out.println("Enter your move (rock, paper or scissors): ");
      String playerMove = input.nextLine();
      while(!playerMove.equals("rock") && !playerMove.equals("paper") && !playerMove.equals("scissors")){
        System.out.println("Invalid move. Please try again: ");
        playerMove = input.nextLine();
      }

      String cpuMove = moves[rand.nextInt(3)];
      System.out.print("The computer chose " + cpuMove + ". ");

      if(cpuMove.equals(playerMove)){
        ties++;
        System.out.println("You tied this round!");
      } else if(
        (cpuMove.equals("rock") && playerMove.equals("paper")) ||
        (cpuMove.equals("paper") && playerMove.equals("scissors")) ||
        (cpuMove.equals("scissors") && playerMove.equals("rock"))
      ){
        wins++;
        System.out.println("You won this round!");
      } else {
        losses++;
        System.out.println("You lost this round!");
      }

      System.out.println("Wins: " + wins + ", losses: " + losses + ", ties: " + ties);
      System.out.println();
    }

    input.close();
  }
}