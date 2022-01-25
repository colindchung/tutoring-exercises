import turtle
screen = turtle.Screen()
screen.title("File Art")
screen.setup(width=500, height=500)
turtle = turtle.Turtle()
turtle.shape("square")
turtle.shapesize(0.1,0.1,0.1)
turtle.width(1)
turtle.color("black")

colorCodes = {
  "R": "red",
  "O": "orange",
  "Y": "yellow",
  "G": "green",
  "B": "blue",
  "P": "purple",
  "W": "white"
}

def drawBoard():
  turtle.penup()
  turtle.goto(-200, 200)
  turtle.setheading(0)
  turtle.pendown()
  for i in range(4):
    turtle.forward(400)
    turtle.right(90)


drawBoard()
with open("test1.txt", "r") as f:

  numLines = 0
  maxLineSize = 0
  lines = []
  for line in f:
    numLines += 1
    maxLineSize = max(maxLineSize, len(line) - 1)
    lines.append(line[:-1])
  
  pixelSize = 400 / max(numLines, maxLineSize)
  turtle.speed(0)
  
  for line in lines:
    for c in line:
      turtle.fillcolor(colorCodes[c])
      turtle.begin_fill()
      for i in range(4):
        turtle.forward(pixelSize)
        turtle.right(90)
      turtle.end_fill()
      turtle.forward(pixelSize)
    turtle.penup()
    turtle.goto(-200, turtle.ycor() - pixelSize)
    turtle.pendown()

  f.close()