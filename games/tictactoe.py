import turtle, time

screen = turtle.Screen()
screen.title("Tic Tac Toe")
screen.setup(width=500, height=500)
turtle = turtle.Turtle()
turtle.shape("square")
turtle.shapesize(0.1,0.1,0.1)
turtle.width(1)
turtle.color("black")

board = ["", "", "", "", "", "", "", "", ""]

coordinates = [
  [-100,100],
  [0,100],
  [100,100],
  [-100,0],
  [0,0],
  [100,0],
  [-100,-100],
  [0,-100],
  [100,-100],
]

winCombinations = [
  [0,1,2],
  [3,4,5],
  [6,7,8],
  [0,3,6],
  [1,4,7],
  [2,5,8],
  [0,4,8],
  [2,4,6]
]

def drawGrid():
  turtle.penup()
  turtle.goto(-50,150)
  turtle.pendown()
  turtle.goto(-50,-150)

  turtle.penup()
  turtle.goto(50,150)
  turtle.pendown()
  turtle.goto(50,-150)

  turtle.penup()
  turtle.goto(-150,50)
  turtle.pendown()
  turtle.goto(150,50)

  turtle.penup()
  turtle.goto(-150,-50)
  turtle.pendown()
  turtle.goto(150,-50)

  turtle.penup()
  turtle.goto(-60, 50)
  turtle.write("0")
  turtle.goto(40, 50)
  turtle.write("1")
  turtle.goto(140, 50)
  turtle.write("2")
  turtle.goto(-60, -50)
  turtle.write("3")
  turtle.goto(40, -50)
  turtle.write("4")
  turtle.goto(140, -50)
  turtle.write("5")
  turtle.goto(-60, -150)
  turtle.write("6")
  turtle.goto(40, -150)
  turtle.write("7")
  turtle.goto(140, -150)
  turtle.write("8")

def drawX():
  turtle.pendown()
  turtle.setheading(45)
  turtle.forward(50)
  turtle.backward(100)
  turtle.forward(50)
  turtle.setheading(135)
  turtle.forward(50)
  turtle.backward(100)
  turtle.forward(50)

def drawO():
  turtle.penup()
  turtle.setheading(270)
  turtle.forward(35)
  turtle.setheading(0)
  turtle.pendown()
  turtle.circle(35)

def drawSymbol(symbol, position):
  turtle.penup()
  turtle.goto(coordinates[position][0], coordinates[position][1])

  if symbol == "x":
    drawX()
  else:
    drawO()

def checkGame(symbol, position, pname):
  for c in winCombinations:
    if board[c[0]] == symbol and board[c[1]] == symbol and board[c[2]] == symbol:
      print(pname + " wins the game!")

      turtle.penup()
      turtle.goto(coordinates[c[0]][0], coordinates[c[0]][1])
      turtle.width(4)
      turtle.color("red")
      turtle.pendown()
      turtle.goto(coordinates[c[2]][0], coordinates[c[2]][1])

      time.sleep(1)
      quit()


def startGame():
  drawGrid()
  print("Welcome to Tic Tac Toe!")
  p1Name = input("Player 1, what is your name? ")
  print("Welcome " + p1Name + "!")
  p2Name = input("Player 2, what is your name? ")
  print("Welcome " + p2Name + "!")

  moves = 0

  while moves < 9: 
    symbol = "x"
    nextMove = 0
    name = p1Name

    if moves % 2 == 0:
      nextMove = int(input(name + ", please enter your move: "))
      while(nextMove < 0 or nextMove > 8 or board[nextMove] != ""):
        nextMove = int(input("Please enter a valid move: "))
    else:
      symbol = "o"
      name = p2Name
      nextMove = int(input(name + ", please enter your move: "))
      while(nextMove < 0 or nextMove > 8 or board[nextMove] != ""):
        nextMove = int(input("Please enter a valid move: "))

    board[nextMove] = symbol
    drawSymbol(symbol, nextMove)
    checkGame(symbol, nextMove, name)

    moves += 1

  print("It is a draw!")

startGame()