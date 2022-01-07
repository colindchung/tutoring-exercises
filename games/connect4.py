import turtle, time

screen = turtle.Screen()
screen.title("Connect 4")
screen.setup(width=600, height=500)
screen.bgcolor("blue")
turtle = turtle.Turtle()
turtle.shape("square")
turtle.shapesize(0.1,0.1,0.1)
turtle.width(1)
turtle.color("black")

board = [
  [" ", " ", " ", " ", " ", " ", " ",],
  [" ", " ", " ", " ", " ", " ", " ",],
  [" ", " ", " ", " ", " ", " ", " ",],
  [" ", " ", " ", " ", " ", " ", " ",],
  [" ", " ", " ", " ", " ", " ", " ",],
  [" ", " ", " ", " ", " ", " ", " ",]
]


def drawBoard():
  turtle.penup()
  turtle.fillcolor("grey")
  turtle.speed(0)
  turtle.goto(250,187.5)
  turtle.setheading(90)
  turtle.pendown()

  for i in range(6):
    for j in range(7):
      turtle.begin_fill()
      turtle.circle(25)
      turtle.end_fill()
      turtle.penup()
      turtle.left(90)
      turtle.forward(75)
      turtle.right(90)
      turtle.pendown()
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(525)
    turtle.setheading(270)
    turtle.forward(75)
    turtle.setheading(90)
    turtle.pendown()

def printBoard():
  for row in board:
    print(row)

def drawPiece(row, column, symbol):
  xcor = -200 + (column * 75)
  ycor = 187.5 - (row * 75)

  turtle.penup()
  turtle.goto(xcor, ycor)
  turtle.fillcolor("red" if symbol == "R" else "yellow")
  turtle.begin_fill()
  turtle.circle(25)
  turtle.end_fill() 

def move(player):
  symbol = "R" if player == 1 else "Y"
  column = int(input("Player " + str(player) + ", enter a column: "))
  while(column < 0 or column > 6 or board[0][column] != " "):
    column = int(input("Player " + str(player) + ", please enter a valid column"))
  
  row = 5
  while board[row][column] != " ":
    row -= 1
  board[row][column] = symbol
  drawPiece(row, column, symbol)


def startGame():
  drawBoard()
  moves = 0

  while True:
    playerNum = (moves % 2) + 1
    move(playerNum)
    moves += 1


startGame()