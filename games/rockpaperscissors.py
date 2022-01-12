import random

numGames = int(input("How many games would you like to play? "))
print()

wins = 0
losses = 0
ties = 0

moveMap = {0: "rock", 1: "paper", 2: "scissors"}

for i in range(numGames):
  print("Round " + str(i+1) + " of " + str(numGames))
  print("-------------------------")
  playerMove = input("Please enter your move (rock, paper or scissors): ")

  while(playerMove != "rock" and playerMove != "paper" and playerMove != "scissors"):
    playerMove = input("Invalid move. Try again: ")

  cpuMove = moveMap[random.randint(0, 2)]
  print("The computer has chosen " + cpuMove + ".", end=" ")

  if(playerMove == cpuMove):
    ties += 1
    print("You have tied this round!")
  elif((playerMove == "rock" and cpuMove == "scissors") or (playerMove == "scissors" and cpuMove == "paper") or (playerMove == "paper" and cpuMove == "rock")):
    wins += 1
    print("You win this round!")
  else:
    losses += 1
    print("You have lost this round!")

  print("Wins: " + str(wins) + ", losses: " + str(losses) + ", ties: " + str(ties))
  print()