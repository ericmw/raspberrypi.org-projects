#!/bin/python3

from turtle import *
from random import randint

speed(0)
#penup() "lifts the pen up" so no line appears  
penup()
goto(-140,140)
#write() writes text to the screen
for step in range(15):
    write(step, align = "center")
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

#1st line creates a turtle,next lines set the colour and shape of turtle
redTurtle = Turtle()
redTurtle.color("red")
redTurtle.shape("turtle")
redTurtle.penup()
redTurtle.goto(-160,100)
redTurtle.pendown()

blueTurtle = Turtle()
blueTurtle.color("blue")
blueTurtle.shape("turtle")
blueTurtle.penup()
blueTurtle.goto(-160,70)
blueTurtle.pendown()

greenTurtle = Turtle()
greenTurtle.color("green")
greenTurtle.shape("turtle")
greenTurtle.penup()
greenTurtle.goto(-160,40)
greenTurtle.pendown()

yellowTurtle = Turtle()
yellowTurtle.color("yellow")
yellowTurtle.shape("turtle")
yellowTurtle.penup()
yellowTurtle.goto(-160,10)
yellowTurtle.pendown()
  
for steps in range(100):
  redTurtle.forward(randint(1,5))
  blueTurtle.forward(randint(1,5))
  greenTurtle.forward(randint(1,5))
  yellowTurtle.forward(randint(1,5))
  
  
  
