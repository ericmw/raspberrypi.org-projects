#import all the functions from the turtle and random module
from turtle import *
from random import *

#function that gives the turtle shape a random color
def randomColor():
  #colormode fixes the issue with TurtleGraphicsError: bad color sequence
  colorMode = colormode(255)
  red = randint(0,255)
  green = randint(0,255)
  blue = randint(0,255)
  color(red,green,blue)

#function that gives the turtle shape a random position
def randomPlace():
  penup()
  x = randint(-100, 100)
  y = randint(-100, 100)
  goto(x,y)
  pendown()

shape("turtle")
speed(0)

#draws a turtle at a random position with a random color
def randomTurtle():
  randomColor()
  randomPlace()
  randomheading = randint(1,360)
  #makes the turtle permanent on the screen
  stamp()

for i in range(30):
  randomTurtle()
            
#hideturtle() hides the drawn shapes, clear() clears the screen \
#and setheading() returns the turtle icon to its default position
hideturtle()
clear()
setheading(0)

#draws a rectangle at a random position with a random color and size
def randomRectangle():
 randomColor()
 randomPlace()
 length = randint(10, 100)
 height = randint(10, 100)
 begin_fill()
 for i in range(2):
   forward(length)
   right(90)
   forward(height)
   right(90)
 end_fill()

for i in range(30):
  randomRectangle()

hideturtle()
clear()
setheading(0)

#draws a circle at a random position with a random color and size
def randomCircle():
  randomColor()
  randomPlace()
  begin_fill()
  circle(randint(10,100))
  end_fill()

for i in range(30):
  randomCircle()

hideturtle()
clear()
setheading(0)

#draws a star at a random position with a random color
def randomStar():
  randomColor()
  randomPlace()
  begin_fill()
  for side in range(5):
    #left(randint(100,150))
    #forward(randint(10,50))
     left(144)
     forward(50)
  end_fill()

for i in range(30):
  randomStar()



