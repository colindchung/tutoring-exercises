import turtle, random

screen = turtle.Screen()
screen.title("Hangman")
screen.setup(width=500, height=500)

turtle = turtle.Turtle()
turtle.shape("square")
turtle.shapesize(0.1,0.1,0.1)
turtle.width(1)
turtle.color("black")

words = ["apple", "chair", "money", "house", "queen", "stage", "space", "grass", "brown", "clock", "metal", "enemy", "wheel", "bench", "piano"]

def drawBoard():
  turtle.penup()
  turtle.pensize(3)

  turtle.goto(200,-50)
  turtle.setheading(180)
  turtle.pendown()
  turtle.forward(150)
  turtle.backward(75)

  turtle.right(90)
  turtle.forward(250)
  turtle.left(90)
  turtle.forward(75)
  turtle.left(90)
  turtle.forward(30)

  turtle.penup()
  turtle.setheading(0)
  turtle.goto(-200,50)
  for i in range(5):
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(15)

def printWord(word, guesses):
  for c in word:
    if c in guesses:
      print(c, end="")
    else:
      print("_", end="")
  print()

def drawHead():
  turtle.penup()
  turtle.goto(50, 170)
  turtle.setheading(180)
  turtle.pendown()
  turtle.circle(20)

def drawBody():
  turtle.penup()
  turtle.goto(50,130)
  turtle.setheading(270)
  turtle.pendown()
  turtle.forward(60)

def drawLeftArm():
  turtle.penup()
  turtle.goto(50,115)
  turtle.setheading(225)
  turtle.pendown()
  turtle.forward(30)

def drawRightArm():
  turtle.penup()
  turtle.goto(50,115)
  turtle.setheading(315)
  turtle.pendown()
  turtle.forward(30)

def drawLeftLeg():
  turtle.penup()
  turtle.goto(50,70)
  turtle.setheading(225)
  turtle.pendown()
  turtle.forward(40)

def drawRightLeg():
  turtle.penup()
  turtle.goto(50,70)
  turtle.setheading(315)
  turtle.pendown()
  turtle.forward(40)

def drawFailLetter(numFails, letter):
  turtle.penup()
  turtle.goto(-220, -75)
  turtle.setheading(0)
  turtle.forward(numFails * 20)
  turtle.write(letter, font=("Verdana", 15, "normal"))

def drawLetters(word, letter):
  turtle.penup()
  turtle.setheading(0)
  turtle.goto(-195,50)

  for c in word:
    if c == letter:
      turtle.write(letter, font=("Verdana", 15, "normal"))
    turtle.forward(35)

def drawFail(numFails, letter):
  drawFailLetter(numFails, letter)

  if numFails == 1:
    drawHead()
  elif numFails == 2:
    drawBody()
  elif numFails == 3:
    drawLeftArm()
  elif numFails == 4:
    drawRightArm()
  elif numFails == 5:
    drawLeftLeg()
  elif numFails == 6:
    drawRightLeg()

def drawGameOver():
  turtle.penup()
  turtle.goto(40,120)
  turtle.setheading(0)
  turtle.color("red")
  turtle.pensize(4)
  turtle.pendown()
  turtle.forward(20)

def startGame():
  drawBoard()

  gameOver = False
  guesses = []
  word = words[random.randint(0, len(words) - 1)]
  numFails = 0

  lettersRemaining = []
  for c in word:
    if c not in lettersRemaining:
      lettersRemaining.append(c)

  while not gameOver:    
    guess = input("Guess a letter! ")

    while len(guess) != 1 or (not guess.isalpha() or guess in guesses):
      guess = input("Invalid guess! Try again. ")

    guesses.append(guess)

    if guess in lettersRemaining:
      lettersRemaining.remove(guess)
      drawLetters(word, guess)

      if lettersRemaining == []:
        print("You win! The word was " + word + ".")
        gameOver = True
    else:
      numFails += 1
      drawFail(numFails, guess)

      if numFails == 7:
        print("You ran out of guesses! The word was " + word + ".")
        drawGameOver()
        gameOver = True
 

startGame()
