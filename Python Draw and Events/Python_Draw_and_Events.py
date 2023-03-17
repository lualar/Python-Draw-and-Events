import random
from turtle import Turtle, Screen
#from ColorSearch import convert_rgb_to_names, randomColor

#Function to move forward the turtle
def moveForward(iDistance=10):
    theTurtle.forward(iDistance)

def moveBackward(iDistance=10):
    theTurtle.backward(iDistance)

def moveClockwise(iDistance=10):
    newHeading = theTurtle.heading() - iDistance
    theTurtle.setheading(newHeading)

def moveCounterClockwise(iDistance=10):
    newHeading = theTurtle.heading() + iDistance
    theTurtle.setheading(newHeading)

def cleanScreen():
    theScreen.clearscreen()
    theTurtle.clear()
    theTurtle.color("black")

#Create Turtle object and asign a shape
theTurtle = Turtle()
#Open Tturtle Screen Window
theScreen = Screen()
theScreen.listen()

#create Turtle
theTurtle.color("black")

#Keys W(Forward)  S(Backwards) A(Counter Clockwise) D (Clockwise)  C(Clear Screen and Turtle on center of screen)

#Lower Caps Options
theScreen.onkey(key="w",fun=moveForward)   #This is a sample of a higher order function
theScreen.onkey(key="s",fun=moveBackward)   #This is a sample of a higher order function
theScreen.onkey(key="a",fun=moveCounterClockwise)   #This is a sample of a higher order function
theScreen.onkey(key="d",fun=moveClockwise)   #This is a sample of a higher order function
theScreen.onkey(key="c",fun=cleanScreen)   #This is a sample of a higher order function
##Upper Caps Options
theScreen.onkey(key="W",fun=moveForward)   #This is a sample of a higher order function
theScreen.onkey(key="S",fun=moveBackward)   #This is a sample of a higher order function
theScreen.onkey(key="A",fun=moveCounterClockwise)   #This is a sample of a higher order function
theScreen.onkey(key="D",fun=moveClockwise)   #This is a sample of a higher order function
theScreen.onkey(key="C",fun=cleanScreen)   #This is a sample of a higher order function

theScreen.colormode(255)
theScreen.exitonclick()