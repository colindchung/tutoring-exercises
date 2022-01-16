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
